import altair as alt
import pandas as pd
from datetime import date, timedelta
from snowflake.snowpark.functions import col
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import when_matched, when_not_matched
session = get_active_session()

st.set_page_config(layout="wide")
class SnowflakeData:
    
    @classmethod
    @st.cache_data(show_spinner=False)
    def get_district_managers(cls):
        session = get_active_session()
        return session.table('finance.customer.snowflake_account_revenue').select(col('DM').alias('DM'), col('AE').alias('AE'))\
        .filter(col('RVP')=='Brian Daniels').distinct().to_pandas()

    @classmethod
    @st.cache_data(show_spinner=False)
    def get_filtered_accounts(cls, dm, ae):
        session = get_active_session()
        return session.table('finance.customer.snowflake_account_revenue').select(col('SALESFORCE_ACCOUNT_NAME').alias('SALESFORCE_ACCOUNT_NAME'))\
        .filter((col('RVP')=='Brian Daniels')&(col('AE')==ae)& (col('DM')==dm)).distinct().to_pandas()[['SALESFORCE_ACCOUNT_NAME']]
    
    @classmethod
    @st.cache_data(show_spinner=False)
    def get_snowpark_data (cls,account:str,dm:str,ae:str,dt_start:str,dt_end:str):
        account_credits = session.table('finance.customer.snowflake_account_revenue')\
                            .filter((col('DM')==dm)&(col('AE')==ae)\
                                    &(col('GENERAL_DATE')>=dt_start)&(col('GENERAL_DATE')<=dt_end)\
                                   &(col('SALESFORCE_ACCOUNT_NAME')==account))\
                            .select(col('GENERAL_DATE'),col('SALESFORCE_ACCOUNT_NAME'),col('SALESFORCE_ACCOUNT_ID'), col('COMPUTE_CREDITS'))\
                            .group_by(col('GENERAL_DATE'),col('SALESFORCE_ACCOUNT_NAME'),col('SALESFORCE_ACCOUNT_ID') )\
                            .sum(col('COMPUTE_CREDITS'))
        snowpark_credits = session.table('sales.sales_engineering.partner_credit_usage').filter((col('TOOL')=='Snowflake')\
                                                                                                &(col('client')=='Snowpark'))

                                                                                                
        results = account_credits.join(snowpark_credits, on= (account_credits['SALESFORCE_ACCOUNT_ID'] == snowpark_credits['SALESFORCE_ACCOUNT_ID']) \
                                       & (account_credits['GENERAL_DATE'] == snowpark_credits['DS'])).to_pandas()
        return results
        
    @classmethod
    @st.cache_data(show_spinner=False)
    def get_workshops(cls, account):
        session = get_active_session()
        return session.table('temp.dshaw.SNOWPARK_WORKSHOPS').filter(col('SALESFORCE_ACCOUNT_NAME')==account).to_pandas()
    
    @classmethod
    def merge_data(cls, source_df):

        source_sdf = session.createDataFrame(source_df)
        target_df = session.table('temp.dshaw.SNOWPARK_WORKSHOPS')
        target_df.merge(source_sdf,\
                        (target_df['SALESFORCE_ACCOUNT_NAME'] == source_sdf['SALESFORCE_ACCOUNT_NAME']) &\
                        (target_df['GENERAL_DATE'] == source_sdf['GENERAL_DATE']),
                        [when_matched().update({"WORKSHOP_NAME":source_sdf['WORKSHOP_NAME'],"ATTENDEES":source_sdf['ATTENDEES'] }),\
                         when_not_matched().insert({"SALESFORCE_ACCOUNT_NAME":source_sdf['SALESFORCE_ACCOUNT_NAME'],\
                                                    "GENERAL_DATE":source_sdf['GENERAL_DATE'],\
                                                    "WORKSHOP_NAME":source_sdf['WORKSHOP_NAME'],\
                                                    "ATTENDEES":source_sdf['ATTENDEES'] }\
                                                  )])

        
if 'select_ae' not in st.session_state:
    st.session_state['selected_ae'] = ''

mysidebar = st.sidebar

dm = mysidebar.selectbox('District Manager', options=sorted(set([i for i in SnowflakeData.get_district_managers()['DM']])), key='selected_dm')
ae = mysidebar.selectbox('Account Executive', options=SnowflakeData.get_district_managers().loc[SnowflakeData.get_district_managers()['DM']== st.session_state['selected_dm']][['AE']].sort_values(by='AE'))

filtered_accounts = SnowflakeData.get_filtered_accounts(dm,ae).sort_values(by='SALESFORCE_ACCOUNT_NAME')
with st.spinner("Refreshing Account List"):
    account = mysidebar.selectbox('Account',options=filtered_accounts)
date_start = mysidebar.date_input('Starting Date',value=(date.today()-timedelta(days=280)))
date_end = mysidebar.date_input('Ending Date')

if account and dm and ae and date_start and date_end:
    data=SnowflakeData.get_snowpark_data(account=account,dm=dm, ae=ae, dt_start=str(date_start), dt_end=str(date_end))
    workshops = SnowflakeData.get_workshops(account=account)
    workshops = workshops.astype({"GENERAL_DATE":str})
    
    data = data.rename(columns={ 'SUM(COMPUTE_CREDITS)':'TOTAL_CREDITS', 'CREDITS':'SNOWPARK_CREDITS'})
    data = data.sort_values(by='GENERAL_DATE')
    
    def get_chart(data):
        hover = alt.selection_single(
            fields=["GENERAL_DATE"],
            nearest=True,
            on="mouseover",
            empty="none",
        )
    
        line1 = alt.Chart(data, title="Total vs Snowpark Consumption").mark_line().encode(
                x="GENERAL_DATE",
                y="TOTAL_CREDITS",
                color=alt.value('#29B5E8')
            )
       
    
        bar1 = alt.Chart(data, title="Total vs Snowpark Consumption").mark_bar().encode(
                x="GENERAL_DATE:T",
                y="SNOWPARK_CREDITS:Q",
                color= alt.value('#71D3DC')
            )
        
    
        # Draw a rule at the location of the selection
        tooltips = (
            alt.Chart(data)
            .mark_rule()
            .encode(
                x="GENERAL_DATE:T",
                y=alt.Y("TOTAL_CREDITS", title=None),
                opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                tooltip=[
                    alt.Tooltip("GENERAL_DATE"),
                    alt.Tooltip("TOTAL_CREDITS"),
                ],
            )
            .add_selection(hover)
        )
        return (bar1+line1 + tooltips).resolve_scale(y='independent')
    
    chart = get_chart(data)
     
    # Create a chart with annotations
    annotation_layer = (
        alt.Chart(workshops)
        .mark_text(size=25, text="🏂",  align="center")
        .encode(
            x="GENERAL_DATE:T",
            y=alt.Y("ATTENDEES:Q",title=None, scale=alt.Scale(domain=[0,200])),
            tooltip=["WORKSHOP_NAME"],
        )
    )
    
    st.title('Southeast Enterprise X-Games: Snowpark Initiative')
    st.metric(label="Selected Account", value=account)
    
    
    st.altair_chart(
        (chart + annotation_layer).properties(height=400).interactive(),
        theme="streamlit",
        use_container_width=True
    )

    st.caption('The line chart shows overall Snowflake daily credit consumption. The bar chart reflects daily Snowpark credit consumption. The snowboarder identifies Snowpark workshop dates.')
    
    # Create editable Snowpark Workshop Table to save in Snowflake
    st.subheader('Update Relevent Snowpark Workshops')
    # df= annotations_df.drop(["X"], axis=1)
    edited_annotations = st.experimental_data_editor(workshops, num_rows='dynamic')
    
    
    if st.button('Update Snowflake Table'):
        with st.spinner("Merging Data"):
            SnowflakeData.merge_data(source_df=edited_annotations)
