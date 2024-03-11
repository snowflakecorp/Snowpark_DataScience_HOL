# Snowpark Immersion Day Workshop: including End-to-End Data Science Hands-on-Lab

Here is a ["pitch" slide](https://docs.google.com/presentation/d/13earSi8o6H1x94T5g_5NJaFxQ6-jIJg6p_Q30olV3eA/edit?usp=sharing)  you could use to position the Snowpark Immersion Day Workshop.

**Workshop Objective:**
The goal of this 2hr+ customer workshop is to help all attendees:
- Understand that Snowflake is NOT just a SQL warehouse (native support Python, Java, Scala)
- Understand that Snowflake is a powerful engine for all Transformations (5x faster than Spark)
- Understand Snowflake’s AI and Apps-focused roadmap
- Enable users with ready-to-use code viabu Hands-On-Lab

Snowflake Summit introduced several new capabilities supporting AI/ML using Snowpark. Snowflake has created a “choose your own adventure” hands-on-workshop allowing attendees to fill in missing code to complete an example end-to-end data science project. This multi-phased experience includes hearing from experts and then completing hands-on activities to prepare, model, deploy, and operationalize your data.

During this Snowpark Hands-on-Workshop, your customer will:
- Leverage **one** of the following Python environments:
  - **Snowflake Notebooks\***,
  - **Hex\***,
  - **Visual Studio Code, Jupyter or another Python IDE of their choice**
- Choose between an "Easy Path" or "Intermediate Path" based on their Python skills
- Leverage Snowpark ML APIs to prepare, transform, and model data
- Apply Snowflake’s new Model Registry to deploy a machine learning model(s)
- Operationalize model predictions using a Snowflake in Streamlit app

💡 **NOTE: Preferred notebooks are identified with * due to pre-installed packages, simpler user authentication, no local environments, and great for large audiences**. 

⚠ **CAUTION:** If you select VS Code/Jupyter/etc, there is a 100% chance attendees will miss installing required packages. Typically this causes ~50% of HOL time spent getting users started instead of learning about Snowpark and the value of Snowflake. 

# Suggested 2hr Hands-on-Workshop Agenda
- **Welcome** (Account AE)
- **Snowpark Intro - 15min**
  - Why did Snowflake create Snowpark and what is Snowpark (Account SE) - 5min
  - Snowpark for Data Engineering (FCTO or Snowpark Expert) - 5min
  - Snowpark for ML / AI FCTO or Snowpark Expert) - 5min
- **Snowpark Data Science end-to-end Hands-on-Lab:**
  - Part 1: Data preparation & transformations using Snowpark ML API
  - Part 2: Create simple ML-powered forecast using Cortex ML
  - Part 3: Create ML model in Snowpark using Snowpark ML API
  - Part 4: Register and operationalize ML model using Snowpark ML API
  - Part 5: Create interactive Streamlit application leveraging Snowpark model using SiS and Snowpark ML API
- **Next Steps**
  - What new use cases are they interested in testing/piloting or migrating to Snowpark?
  
**Additional popular topics to include (plan to run more than 2hrs)**
- Snowflake Roadmap (FCTO or Snowpark Expert) - 15min
  - Potential items might include Feature Store, Experiment Tracking, Git Integration, etc.
- Navigating the Snowflake Platform - (Account SE) - 10min
  - Potential items might include SF virtual warehouses, databases/schemas, Universal search, resource monitors, etc.

## Recommended Customer Workshop Approach
## Days BEFORE the workshop:
- Identify a Snowpark/HOL expert. Consider reaching out to SE Enablement (Diana Shaw, Chris Jackson, Chris Skirde, Dan Iacono) and/or local FCTO
- Meet with your customer with ACCOUNTADMIN access to complete the [PreWork requirements](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/tree/main/PreWorkForSnowflakeTeam)
- Select one Python environment for the hands-on-lab. Preferred options include Snowflake Notebooks and Hex (see comments above)
- Make a copy of this [Snowpark Hands-on-Lab Workshop Deck](https://docs.google.com/presentation/d/1YGm2U-PyNofoA8KRTF7oA9_K046BkNNHOoJ4abhYmnk/edit?usp=sharing) and update for your customer workshop

## Day of the workshop:
- Use your copy of this [deck](https://docs.google.com/presentation/d/1YGm2U-PyNofoA8KRTF7oA9_K046BkNNHOoJ4abhYmnk/edit?usp=sharing)
- Customer-aligned Account Executive should open the meeting and setup the overall expectations for this workshop (~5mins)
- Customer-aligned Sales Engineer should walk through **"Why Snowflake created Snowpark"** (~10mins)
- Snowpark/HOL expert to remind attendees to the workshop focus
- Snowflake Team should engage the customer to ask about potential Data Science use cases or experience. If this is known prior to the meeting, take this time to validate if those use cases are still relevant. The Snowpark/HOL expert should note the validate use cases and relate to them throughout the workshop. This will ensure the Tasty Bytes demo content can be shown as a relevant flow to match the customer needs.
- Once use cases are know, the Snowpark/HOL expert should walk through hands-on-lab setup slides
- Customer-aligned Sales Engineer share access to the **"Easy Path" and "Intermediate Path" notebooks**
- Stop sharing. Get attendees to show and validate they can access the workshop notebook.
- Snowpark/HOL expert to walk through "Connect to Snowflake"
- Stop sharing. Get attendees to show and validate they can access the workshop notebook.
- When the Snowpark/HOL expert starts to work through the balance of the workshop content, we recommend the following:
  - Use a split screen with slides on one side and the notebook on the other. This provides a "you are here" map for attendees through the workshop. For each part of the workshop, use the corresponding Reference Material slides (slides 26 to 44) to set up what the attendees will review.
  - Do not rerun the code. The Snowpark/HOL expert should use pre-run code and focus their time on explaining the value Snowflake brings, not that the code run.
  - Recommend having a FCTO or two Snowpark experts deliver this content. It makes the experience more engaging for attendees.
  - Stop and ask questions OFTEN.
  - Customer-aligned SE and AE should monitor and respond to the questions and stop the Snowpark/HOL expert as needed.

  **Workshop Best Practices: Use a split display to show both the ppt and the notebook.** This helps attendees with a "you are here" map.
![image](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/faaf42bb-fb14-43a9-9b1c-b6e583730c34)


  **Workshop Best Practices: Pause often and engage the attendees with the following questions:**
  - Does this flow follow their typical data science flow?
  - Do they have any questions?
  - Are they starting the understand how Snowpark works?
  - Do they perceive any value with using Snowpark instead of pure Pandas?
  - Do they have any upcoming projects they could try using Snowpark?
  - Do they see themselves reusing this flow and notebook during their next data science effort?

  **Workshop Best Practices: Plan for at least 10min to close the Workshop:**
  - Customer-aligned Account Executive should open remind them of the overall expectations of this workshop
  - Customer-aligned Sales Engineer should walk through what they accomplished: they used Snowpark to prepare, model, deploy, and operationalize data using runtimes and libraries that securely deploy and process non-SQL code in Snowflake.
  - Snowpark/HOL expert should offer suggestions on how to use this workshop/example to start planning how to leverage Snowpark for their new data science use cases.


## Days/Months AFTER the workshop:
- Account Team should add newly identify used cases in SFDC
- SE should track and monitor Snowpark usage. Consider using [Account360](https://a360.snowflake.com/) or the [Snowpark Immersion Day Initiative SiS app](https://app.snowflake.com/sfcogsops/snowhouse_aws_us_west_2/#/streamlit-apps/TEMP.DSHAW.VM4EPAUIQEGBA6M6?ref=snowsight_shared). You will need to use the SALES_ENGINEER role to access.
![image](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3ced26a3-a634-41ff-9230-bd707b4c19f6)


- Option: Enterprise Southeast Team used the following [SiS Snowhouse app](https://app.snowflake.com/sfcogsops/snowhouse_aws_us_west_2/#/streamlit-apps/TEMP.DSHAW.VM4EPAUIQEGBA6M6?ref=snowsight_shared) to track post-workshop Snowpark utilization. Use SALES_ENGINEER role to access. Here is the [SiS app code](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/SiS_application.py)
- Please provide feedback on this workshop to [Diana Shaw](diana.shaw@snowflake.com)


## Snowpark Data Science Hands-on-Workshop includes two skill-level notebooks for participants to choose from based on your Snowpark and Python experience:

**- Easy Path: directions and code is ready to be executed**
- [**Snowflake Notebooks link**](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/ForCustomer/Notebooks/Snowflake_Notebook_EasyPath_app.ipynb) ![Snowflake Easy Path](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/241d436f-f265-4a10-a75e-e6acadee500d)
  - When using Snowflake Notebooks, ensure you add the following **Packages** _before running the code_. Add **matplotlib**, **plotly**, **seaborn** and **snowflake-ml-python**. <img width="512" alt="image" src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/b587ec88-5168-466b-bc13-ae58ddf2bd96" width="150">

  
- Hex [notebook link](https://app.hex.tech/snowflake/hex/749432f0-7366-4875-b51d-18247d9724f0) option: ![EasyPath](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/dba6c410-c3a3-473a-91c6-ebfd1e2dc341)

  
- Jupyter [notebook link](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/ForCustomer/Notebooks/End-to-End%20Data%20Science%20using%20Snowpark%20-%20Easy%20Path.ipynb) option: ![Easy Path](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/79988a20-e518-4518-b025-e92c7e421438)


**- Intermediate Path: directions and some critical code is missing**
- [**Snowflake Notebooks link**](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/ForCustomer/Notebooks/Snowflake_Notebook_IntermediatePath_app.ipynb)

 ![Snowflake Intermediate Path](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/ad10f4dd-35a1-4426-b9b4-770895c76c04)
  - When using Snowflake Notebooks, ensure you add the following **Packages** _before running the code_. Add **matplotlib**, **plotly**, **seaborn** and **snowflake-ml-python**. <img width="512" alt="image" src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/b587ec88-5168-466b-bc13-ae58ddf2bd96" width="150">

  
- Hex [notebook link](https://app.hex.tech/snowflake/hex/c916014e-667b-4a02-a037-1aa470c5a5fe) option: ![Intermediate_Path](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/d7406579-cb24-40bb-a5bf-bbb4556c3b95)

  
- Jupyter [notebook link](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/blob/main/ForCustomer/Notebooks/End-to-End%20Data%20Science%20using%20Snowpark%20-%20Intermediate%20Path.ipynb) option: ![Intermediate Path](https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/9de5a014-2b12-48d6-a433-b2fbaae7498f)
