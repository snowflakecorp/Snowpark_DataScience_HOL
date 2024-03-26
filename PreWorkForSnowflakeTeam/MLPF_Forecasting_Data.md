**Get Cybersyn Government Essentials listing in your account**

**Step 1: Loading Holiday Data from the Snowflake Marketplace**
- Log into your Snowflake account as the ACCOUNTADMIN or similar role
- Click on ‘Marketplace' on the left hand banner
- In the search bar, search for ‘Cybersyn Government Essentials'
- Click on the first listing, with the same title ‘Cybersyn Government Essentials'
- Click on get, and on the pop-up screen, rename the database to FROSTBYTE_CS_PUBLIC (in all caps). 
- Note - if prompted, you may need to fill in your details before being able to get access. 
- Grant access to the PUBLIC role in the dropdown menu
![image](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/418f8432-7448-43e1-ae19-eeb2851ddf38)


**Step 2: Creating Objects, Load Data, & Set Up Tables**
- Create a new worksheet by clicking on the ‘Worksheets' tab on the left hand side.
- Paste and run the following SQL commands in the worksheet to create the required Snowflake objects, ingest sales data from S3, and update your Search Path to make it easier to work with the MLPFs.

```
-- SnowparkImmersionDayWorkshop MLPF Forecast Data Setup Code

USE ROLE ACCOUNTADMIN;

-- Create development database, schema for our work: 
CREATE OR REPLACE DATABASE quickstart;
CREATE OR REPLACE SCHEMA mlpf;

-- Use appropriate resources: 
USE DATABASE quickstart;
USE SCHEMA mlpf;

-- Create warehouse to work with: 
CREATE OR REPLACE WAREHOUSE quickstart_wh;
USE WAREHOUSE quickstart_wh;

-- Set search path for MLPFs:
ALTER ACCOUNT
SET SEARCH_PATH = '$current, $public, SNOWFLAKE.ML';


-- Create a csv file format: 
CREATE OR REPLACE FILE FORMAT frostbyte_tasty_bytes_dev.analytics.csv_ff
type = 'csv'
SKIP_HEADER = 1,
COMPRESSION = AUTO;

-- Create an external stage pointing to s3, to load sales data: 
CREATE OR REPLACE STAGE s3load 
COMMENT = 'Quickstart S3 Stage Connection'
url = 's3://sfquickstarts/frostbyte_tastybytes/mlpf_quickstart/'
file_format = frostbyte_tasty_bytes_dev.analytics.csv_ff;

-- Define Tasty Byte Sales Table
CREATE OR REPLACE table frostbyte_tasty_bytes_dev.analytics.sales(
  	DATE TIMESTAMP_NTZ,
	PRIMARY_CITY VARCHAR(16777216),
	MENU_ITEM_NAME VARCHAR(16777216),
	TOTAL_SOLD NUMBER(17,0)
);

-- Ingest data from s3 into our table
COPY INTO frostbyte_tasty_bytes_dev.analytics.sales 
FROM @s3load/mlpf_quickstart_vancouver_daily_sales.csv;

-- Create Table containing the latest years worth of sales data: 
CREATE OR REPLACE view frostbyte_tasty_bytes_dev.analytics.sales_forecast_input AS (
    SELECT
        to_timestamp_ntz(date) as timestamp,
        primary_city,
        menu_item_name,
        total_sold
    FROM
        frostbyte_tasty_bytes_dev.analytics.sales 
    WHERE
        date > (SELECT max(date) - interval '1 year' FROM frostbyte_tasty_bytes_dev.analytics.sales)
    GROUP BY
        all
);

select * from frostbyte_tasty_bytes_dev.analytics.sales_forecast_input limit 100;
```
![image](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/0bac24da-58cd-43cd-8d10-ff7a13b29691)

Run the code and ensure the output looks like:
![image](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/4c7033c0-632c-48f2-8330-9c71a0ba3137)
