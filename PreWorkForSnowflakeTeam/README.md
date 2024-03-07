# Instruction for Snowflake (SE) team to complete PRIOR to running this end-to-end Snowpark hands-on-lab with customers

# Step 1: Determine which Snowflake account the customer plans to use.
Option 1: Using Snowflake Trial account(s) either one per attendee or one account for many attendees. PRO: role/access/features are easy to enable for all. CON: Snowpark consumption not tied to their account and they lose the example.
Option 2: Use their Snowflake account. PRO: Snowpark consumption tied to their account and they maintain this end-to-end example. CON: plan for how attendees to access the data, create/user model registry, create/use SiS application.

# Step 2: Ensure the following data is loaded in the workshop account
[Snowpark101_Data](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/Snowpark101_Data.md) is needed for Parts 1, 3, 4 and 5 is **frostbyte_tasty_bytes_v2.analytics.shift_sales**. This is Tasty Bytes VERSION 2 data. If you need additional help to correctly setup this data, go to the [Tasty Bytes - Snowpark 101 for Data Science Quickstart](https://quickstarts.snowflake.com/guide/tasty_bytes_snowpark_101_for_data_science/index.html).

[MLPF_Forecast_Data](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/MLPF_Forecasting_Data.md) is needed for Part 2.

# Step 3: Ensure all attendees have data read/write access, can create/register models, and can create SiS applications.
See this [HOL_SF_Setup](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/HOL_SF_Setup.md)) code to create multiple databases (one per attendee) using cloned data. 
- Update line 34 based on the number of attendees.
- Update line 35 with the password to assign to each workshop attendee.

# Step 3 (Optional): Create a BUDGET and/or RESOURCE MONITOR to ensure healthy adoption of this Snowpark Immersion Day Asset
Create Budget using Snowsight GUI:
![image](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3d36e224-2008-405b-8bab-7234d6ebf249)


Create Budget using code:
```
CALL "HOL"."PUBLIC"."SNOWPARKIMMERSIONDAYWORKSHOPBUDGET"!ADD_RESOURCE(SELECT SYSTEM$REFERENCE('DATABASE', '"HOL"', 'SESSION', 'APPLYBUDGET'));
```

Create Resource Monitor using Snowsight GUI:
![image](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3f57245e-e0fc-4c45-b60c-8ce193392afe)


Create Resource Monitor using code:
```
create RESOURCE MONITOR IDENTIFIER('"SNOWPARKIMMERSIONDAYWORKSHOP"') CREDIT_QUOTA = 500 FREQUENCY = 'MONTHLY' START_TIMESTAMP = 'IMMEDIATELY' TRIGGERS ON 90 PERCENT DO SUSPEND ON 100 PERCENT DO SUSPEND_IMMEDIATE ON 75 PERCENT DO NOTIFY

alter WAREHOUSE IDENTIFIER('"WH0"') set RESOURCE_MONITOR = 'SNOWPARKIMMERSIONDAYWORKSHOP'
(repeat for other WH'n' created)
alter WAREHOUSE IDENTIFIER('"WH30"') set RESOURCE_MONITOR = 'SNOWPARKIMMERSIONDAYWORKSHOP'
```

# Step 4: Ensure the Python environment is correctly configured
See the [repo_metal.yaml](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/.github/repo_meta.yaml) file for all Python and Snowpark requirements.

If Hex is the selected workshop Python environment, please connect with your local Hex rep. They can help create a Hex account the customer can access. In the US, please contact [Ariel Zahler](aharnik@hex.tech) for assistance. They can provide guidance on how best to share notebook access with the attendees. **Plan ahead**, it still requires some planning to ensure attendees can successfully sign into Hex, duplicate the notebook, and successfully run the Hex notebooks.
