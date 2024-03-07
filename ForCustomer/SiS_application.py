# Import Python packages
import streamlit as st
import pydeck as pdk
import numpy as np


# Import Snowflake modules
from snowflake.snowpark import Session
import snowflake.snowpark.functions as F
from snowflake.snowpark import Window
from snowflake.snowpark.context import get_active_session
from snowflake.ml.registry import Registry
import snowflake.ml.modeling.preprocessing as snowmlpp


# Set Streamlit page config
st.set_page_config(
    page_title="Streamlit App: Snowpark 101", 
    page_icon=":truck:",
    layout="wide",
)


# Add header and a subheader
st.header("Predicted Shift Sales by Location")
st.subheader("Data-driven recommendations for food truck drivers.")
 


# Connect to Snowflake
# session = init_connection()
session = get_active_session()
 
# Create input widgets for cities and shift
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # Drop down to select city
        city = st.selectbox(
            "City:",
            session.table("HOL.SCHEMA0.SHIFT_SALES_V")
            .select("city")
            .distinct()
            .sort("city"),
        )
 
    with col2:
        # Select AM/PM Shift
        shift = st.radio("Shift:", ("AM", "PM"), horizontal=True)


    n_trucks = st.selectbox('How many food trucks would you like to schedule today?', np.arange(1,10))


    if n_trucks > 1:
        range = st.slider('What is the minimum distance in kilometers between food trucks?', 0, 20, 1)
        st.write('You are requesting a minimum distance of ', range, 'km')
        st.write('Click **:blue[Update]** to get the ', n_trucks, ' highest predicted Shift_Sales food truck locations.')
    else:
        st.write('Click **:blue[Update]** to get one food truck location predicted to have the Shift_Sales')
        
# Get predictions for city and shift time
def get_predictions(city, shift):
    # Get data and filter by city and shift
    snowpark_df = session.table(
        "HOL.SCHEMA0.SHIFT_SALES_V"
    ).filter((F.col("shift") == shift) & (F.col("city") == city))
 
    # Get rolling average
    window_by_location_all_days = (
        Window.partition_by("location_id")
        .order_by("date")
        .rows_between(Window.UNBOUNDED_PRECEDING, Window.CURRENT_ROW - 1)
    )
 
    snowpark_df = snowpark_df.with_column(
        "avg_location_shift_sales",
        F.avg("shift_sales").over(window_by_location_all_days),
    ).cache_result()
 
    # Get tomorrow's date
    date_tomorrow = (
        snowpark_df.filter(F.col("shift_sales").is_null())
        .select(F.min("date"))
        .collect()[0][0]
    )
 
    # Filter to tomorrow's date
    snowpark_df = snowpark_df.filter(F.col("date") == date_tomorrow)
 
    # Impute
    snowpark_df = snowpark_df.fillna(value=0, subset=["avg_location_shift_sales"])


    for colname in snowpark_df.columns:
        new_colname = str.upper(colname)
        snowpark_df = snowpark_df.with_column_renamed(colname, new_colname)
 
    # Encode
    snowpark_df = snowpark_df.with_column("shift_oe", F.iff(F.col("shift") == "AM", 0, 1))\
                             .with_column("shift_oe", F.iff(F.col("shift") == "PM", 1, 0))

    # Scale
    mm_target_columns = ["CITY_POPULATION"]
    mm_target_cols_out = ["CITY_POPULATION_NORM"]
    snowml_mms = snowmlpp.MinMaxScaler(input_cols=mm_target_columns, 
                                       output_cols=mm_target_cols_out)
    snowml_mms.fit(snowpark_df)
    snowpark_df = snowml_mms.transform(snowpark_df)
    
    # Get all features
    feature_cols = ["SHIFT_OE", 
                    "CITY_POPULATION_NORM", 
                    "MONTH", 
                    "DAY_OF_WEEK",
                    "LATITUDE",
                    "LONGITUDE",
                    "AVG_LOCATION_SHIFT_SALES",
                    "LOCATION_ID"]


    snowpark_df = snowpark_df.select(feature_cols)

    native_registry = Registry(session=session, database_name="HOL", schema_name="SCHEMA0")
    model_ver = native_registry.get_model("SHIFT_SALES_PREDICTION").version('v0')
    result_sdf = model_ver.run(snowpark_df, function_name="predict")
    return result_sdf

# Update predictions and plot when the "Update" button is clicked
if st.button(":blue[Update]"):
    # Get predictions
    with st.spinner("Getting predictions..."):
        predictions_sdf = get_predictions(city, shift)
        predictions = predictions_sdf.to_pandas()
 
    # Plot on a map
    st.subheader("Predicted Shift Sales for position")
    predictions["PRED_SHIFT_SALES"].clip(0, inplace=True)
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=predictions["LATITUDE"][0],
                longitude=predictions["LONGITUDE"][0],
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=predictions,
                    get_position="[LONGITUDE, LATITUDE]",
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=predictions,
                    get_position="[LONGITUDE, LATITUDE]",
                    get_color="[200, 30, 0, 160]",
                    get_radius=200,
                ),
            ],
        )
    )
    
    max_x = predictions.loc[predictions["PRED_SHIFT_SALES"].idxmax()]
    st.write("Maximum Predicted Sales are expected at the following location:", max_x)
    #st.dataframe(predictions_sdf)
    
    location_id = max_x["LOCATION_ID"]
    lat = max_x["LATITUDE"]
    long = max_x["LONGITUDE"]

    st.subheader("The following chart is generated using the st_point and st_distance Snowflake Geospatial features")

    if n_trucks == 1:
        st.write("Have your only food truck positioned at Location ID ", location_id, " to maximize SHIFT_SALES")
    elif n_trucks > 1:
        best_locations = [location_id]
        available_locations_sdf = predictions_sdf
    
        st_distance = F.function('st_distance')
        st_point = F.function('st_point')
    
        for truck_n in np.arange(0,n_trucks - 1):
            available_locations_sdf = available_locations_sdf.with_column("DISTANCE_TO_TRUCK", 
                                        st_distance(
                                            st_point(F.lit(float(long)), F.lit(float(lat))),
                                            st_point(F.col("LONGITUDE"), F.col("LATITUDE"))
                                        )/1609
                                       ).filter(F.col("DISTANCE_TO_TRUCK") >= range/1.609).order_by("PRED_SHIFT_SALES", ascending=False)
            max_x = available_locations_sdf.limit(1).to_pandas()
            try:
                location_id = max_x["LOCATION_ID"].iloc[0]
                lat = max_x["LATITUDE"].iloc[0]
                long = max_x["LONGITUDE"].iloc[0]
            except:
                break
            best_locations.append(location_id)


        selected_locations = predictions[predictions["LOCATION_ID"].isin(best_locations)]
        st.map(selected_locations)
        st.dataframe(selected_locations)
