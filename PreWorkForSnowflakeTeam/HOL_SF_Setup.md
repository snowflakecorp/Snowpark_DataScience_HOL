**HOP Setup Code**
The following code to create one database (HOL) and multiple schemas, one per attendee (SCHEMA0 to SCHEMA'n') using cloned data. 
The code also creates a user, role and warehouse per attendee: (USER0 to USER'n', ROLE0 to ROLE'n', and WH0 to WH'n')
Ensure you update lines 34 and 35 to reflect the number of attendees to create and what password to assign.

```
-- Ensure you have the [Snowpark101 data](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/Snowpark101_Data) loaded in your HOL account
-- Ensure you have the [MLPF Forecast data](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/PreWorkForSnowflakeTeam/MLPF_Forecasting_Data) loaded into your HOL Account

-- RUN THIS ONE-TIME-SETUP AS ADMIN IN THE MAIN HOL ACCOUNT to create multiple users
-- create the setup_wh & utility DB
create or replace warehouse setup_wh with warehouse_size = 'xsmall' auto_suspend = 300;
grant ownership on warehouse setup_wh to role securityadmin;
grant usage on warehouse setup_wh to role securityadmin;
create or replace database utility;

-- create a SP to loop queries for N users
-- it replaces the placeholder XXX with N in the supplied query
create or replace procedure utility.public.loopquery (QRY STRING, N FLOAT)
  returns float
  language javascript
  strict
as
$$
  for (i = 0; i <= N; i++) {
    snowflake.execute({sqlText: QRY.replace(/XXX/g, i)});
  }

  return i-1;
$$;

grant usage on procedure utility.public.loopquery (string, float) to role securityadmin;
grant usage on database utility to role securityadmin;
grant usage on schema utility.public to role securityadmin;

----------------------------------------------------------------------------------
-- Set up the HOL environment for the first time
----------------------------------------------------------------------------------

set num_users = 30; --> adjust number of attendees here
set lab_pwd = 'Snowparki$@we$ome!'; --> enter an attendee password here

show roles;

-- Cleanup
call utility.public.loopquery('drop database if exists HOLXXX;', $num_users);
call utility.public.loopquery('drop user if exists userXXX;', $num_users);
call utility.public.loopquery('drop role if exists roleXXX;', $num_users);

-- set up the roles
use role securityadmin;
create or replace role hol_parent comment = "HOL parent role";
use role accountadmin;
create or replace database HOL;
call utility.public.loopquery('create or replace role roleXXX comment = "HOLXXX User Role";', $num_users);
grant role hol_parent to role accountadmin;

show users like '%user%';

-- set up the users
call utility.public.loopquery('create or replace user userXXX default_role=roleXXX password="' || $lab_pwd || '";', $num_users);
call utility.public.loopquery('grant role roleXXX to user userXXX;', $num_users);
call utility.public.loopquery('grant role hol_parent to role roleXXX;', $num_users);
call utility.public.loopquery('grant role roleXXX to role accountadmin;', $num_users);

-- grant account permissions
use role accountadmin;
create warehouse if not exists tasty_dsci_wh warehouse_size='XSmall' min_cluster_count=1 max_cluster_count=5 auto_suspend=300 auto_resume=true;
grant create warehouse on account to role hol_parent;
grant usage on warehouse tasty_dsci_wh to role hol_parent;

-- set up the warehouses and grant permissions
call utility.public.loopquery('create or replace warehouse whXXX warehouse_size = \'xsmall\' AUTO_SUSPEND = 300;', $num_users);
call utility.public.loopquery('grant all on warehouse whXXX to role roleXXX;', $num_users);

-- set up the databases and grant permissions
call utility.public.loopquery('create or replace schema HOL.schemaXXX clone frostbyte_tasty_bytes_dev.analytics;', $num_users);
call utility.public.loopquery('grant usage, modify on database HOL to role roleXXX;', $num_users);
call utility.public.loopquery('grant ownership on schema HOL.schemaXXX to role roleXXX;', $num_users);
call utility.public.loopquery('grant usage, modify on future schemas in database HOL to role roleXXX;', $num_users);
call utility.public.loopquery('grant all on all tables in schema HOL.schemaXXX to role roleXXX;', $num_users);
call utility.public.loopquery('grant all on all views in schema hol.schemaXXX to role roleXXX;', $num_users);
call utility.public.loopquery('grant all on future views in schema hol.schemaXXX to role roleXXX;', $num_users);
call utility.public.loopquery('GRANT SELECT ON VIEW hol.schemaXXX.sales_forecast_input TO ROLE roleXXX', $num_users);

show users;
```
![image](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/8219df1d-952f-49e5-a680-563ea0d0b836)

Run this code and ensure the output looks like:
![image](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/fa4d8977-03af-44e5-b05d-1839ae31c104)
