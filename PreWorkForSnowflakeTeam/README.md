# Instruction for Snowflake (SE) team to complete PRIOR to running this end-to-end Snowpark hands-on-lab with customers

# Step 1: Determine which Snowflake account the customer plans to use.
Option 1: Using Snowflake Trial account(s) either one per attendee or one account for many attendees. PRO: role/access/features are easy to enable for all. CON: Snowpark consumption not tied to their account and they lose the example.
Option 2: Use their Snowflake account. PRO: Snowpark consumption tied to their account and they maintain this end-to-end example. CON: plan for how attendees to access the data, create/user model registry, create/use SiS application.

# Step 2: Ensure the following data is loaded in the workshop account
[Snowpark101_Data](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/Snowpark101_Data.md) is needed for Parts 1, 3, 4 and 5 is **frostbyte_tasty_bytes_v2.analytics.shift_sales**. This is Tasty Bytes VERSION 2 data. If you need additional help to correctly setup this data, go to the [Tasty Bytes - Snowpark 101 for Data Science Quickstart](https://quickstarts.snowflake.com/guide/tasty_bytes_snowpark_101_for_data_science/index.html)

[MLPF_Forecast_Data](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/MLPF_Forecasting_Data.md) is needed for Part 2.

**If running Snowflake Notebooks, consider loading the images in this repo's [ForCustomer/assets](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/tree/main/ForCustomer/assets) directory to a Snowflake Managed Stage. This will ensure the images load in this [Snowflake Notebook with pictures](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/End-to-End%20Data%20Science%20using%20Snowpark%20-%20Presenter%20-%20With%20Images.ipynb)**

<img src="https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/2b3f4824-ff81-4007-afd7-706876cd08dc" width="600">


# Step 3: Ensure all attendees have data read/write access, can create/register models, and can create SiS applications.
See this [HOL_SF_Setup](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/HOL_SF_Setup.md) code to create one database with multiple schemas (one per attendee) with cloned data.
- Update line 34 based on the number of attendees.
- Update line 35 with the password to assign to each workshop attendee.


# Step 4: Ensure the Python environment is correctly configured
Select **one Python environment** and validate it works correctly. 

Preferred notebooks include Snowflake Notebooks and Hex. Please note that Snowflake Notebooks and Hex have all the required packages pre-installed. They offer simpler user authentication. There are no headaches with local environments. They are great for large audiences. 

If Hex is the selected workshop Python environment, please connect with [Ariel Zahler](aharnik@hex.tech) or [Armin Efendic](aefendic@hex.tech) for creating your **dedicated hands-on-lab Hex instance**. This will ensure **GDPR complicance** and **no data leakage** relative to attendee names or email addresses. **Plan ahead**, it still requires some planning to ensure attendees can successfully sign into Hex, duplicate the notebook, and successfully run the Hex notebooks.

Alternatively, you could select Visual Studio Code, Jupyter or another Python IDE of their choice. Please see this [yaml file](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/.github/repo_meta.yaml) for all the required Python and Snowpark packages to be conda or pip installed in the customer Python environment using VS Code/Jupyter/etc.

# Step 5 (Optional): Create a BUDGET and/or RESOURCE MONITOR to ensure healthy adoption of this Snowpark Immersion Day Asset
Create Budget using Snowsight GUI:

<img src="https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3d36e224-2008-405b-8bab-7234d6ebf249" width="600">


Create Budget using code:
```
CALL "HOL"."PUBLIC"."SNOWPARKIMMERSIONDAYWORKSHOPBUDGET"!ADD_RESOURCE(SELECT SYSTEM$REFERENCE('DATABASE', '"HOL"', 'SESSION', 'APPLYBUDGET'));
```

Create Resource Monitor using Snowsight GUI:

<img src="https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3f57245e-e0fc-4c45-b60c-8ce193392afe" width="600">


Create Resource Monitor using code:
```
create RESOURCE MONITOR IDENTIFIER('"SNOWPARKIMMERSIONDAYWORKSHOP"') CREDIT_QUOTA = 500 FREQUENCY = 'MONTHLY' START_TIMESTAMP = 'IMMEDIATELY' TRIGGERS ON 90 PERCENT DO SUSPEND ON 100 PERCENT DO SUSPEND_IMMEDIATE ON 75 PERCENT DO NOTIFY

alter WAREHOUSE IDENTIFIER('"WH0"') set RESOURCE_MONITOR = 'SNOWPARKIMMERSIONDAYWORKSHOP'
(repeat for other WH'n' created)
alter WAREHOUSE IDENTIFIER('"WH30"') set RESOURCE_MONITOR = 'SNOWPARKIMMERSIONDAYWORKSHOP'
```

# Approximate Snowflake compute and data storage needed to complete this workshop:
- setup uses <15 credits 
- running the notebook and SiS app uses <2 credit/attendee
- data storage uses <50MB

<img src="https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/6453de88-01f7-4625-aae2-5c3e71cbcae6" width="600">

