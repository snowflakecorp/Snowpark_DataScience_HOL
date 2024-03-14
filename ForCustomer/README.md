## This folder has everything needed to share with your customer.

This is a **multi-phased end-to-end hands-on Snowpark lab**. It includes preparing/transforming data, modeling data, deploying a model, and operationalizing data in a Snowflake in Streamlit app.

- **Part 0:** Overview (HOL setup)
- **Part 1**: prepare and transform data using Snowpark Python and Snowpark ML APIs
- **Part 2**: create simple ML-powered forecast using Snowflake Cortex
- **Part 3**: model your data using Snowpark ML APIs
- **Part 4**: deploy your model using Snowpark ML Model Registry
- **Part 5**: operationalize your deployed model using [SiS with Snowpark Geospatial features](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/SiS_application.py), st_point and st_distance
  - When using SiS, remember to include all required SiS packages. Attendees will need to add packages pydeck and snowflake-ml-python.

## Have the customer select one (1) Python environment for the workshop that attendees will all use and follow. This is a really critical suggestion based on delivering multiple customer Snowpark workshops. Use one Python tool for the workshop.

Included in this repo are links to access **Snowflake Notebooks**, or **Hex** or **Jupyter** notebooks. 

The benefit with Hex is that you don't need to validate the Python environment prior to the workshop.
## If you select Jypyter or VS Code (or another Python IDE), ensure you validate both end-to-end notebooks run without errors SEVERAL DAYS prior to the workshop.

To make the hands-on-lab more engaging, we recommend **offering at least two different skill-level notebooks**. 
For instance, the **"Easy Path"** is the solution. Attendees just need to update their Snowflake account connection details and can click through each cell without adjustments.
The **"Intermediate Path"** is recommended to engage Python-savvy attendees. They will need to update the connection to Snowflake and make adjustments to add critical variables in order for cells to run.

# Ensure attendees know where to access relevant Snowflake documentation
- [Snowflake Notebooks](https://docs.snowflake.com/LIMITEDACCESS/snowsight-notebooks/ui-snowsight-notebooks-about)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/latest/index)
- [Training Machine Learning Models with Snowpark Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/python-snowpark-training-ml)
- [Snowpark ML Model Registry](https://docs.snowflake.com/en/developer-guide/snowpark-ml/snowpark-ml-mlops-model-registry#deleting-models)
  
# Two lab levels are available for participants to choose from based on Snowpark and Python experience:

**- Easy Path: directions and code is ready to be executed**
- [**Snowflake Notebooks** link](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/Snowflake_Notebook_EasyPath_app.ipynb):
  
  <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/241d436f-f265-4a10-a75e-e6acadee500d" width=600>
  
  - When using Snowflake Notebooks, ensure you add the following **Packages** _before running the code_. Add **matplotlib**, **plotly**, **seaborn** and **snowflake-ml-python**.
  
    <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/b587ec88-5168-466b-bc13-ae58ddf2bd96" width=350>

  
- [**Hex** notebook link](https://app.hex.tech/snowflake/hex/749432f0-7366-4875-b51d-18247d9724f0):

 <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/dba6c410-c3a3-473a-91c6-ebfd1e2dc341" width=600>

  
- [**Jupyter** notebook link](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/End-to-End%20Data%20Science%20using%20Snowpark%20-%20Easy%20Path.ipynb):

  <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/79988a20-e518-4518-b025-e92c7e421438" width=600>

**- Intermediate Path: directions and some critical code is missing**
- [**Snowflake Notebooks** link](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/Snowflake_Notebook_IntermediatePath_app.ipynb):

 <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/ad10f4dd-35a1-4426-b9b4-770895c76c04" width=600>
 
  - When using Snowflake Notebooks, ensure you add the following **Packages** _before running the code_. Add **matplotlib**, **plotly**, **seaborn** and **snowflake-ml-python**.
  
    <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/b587ec88-5168-466b-bc13-ae58ddf2bd96" width=350>

  
- [**Hex** notebook link](https://app.hex.tech/snowflake/hex/c916014e-667b-4a02-a037-1aa470c5a5fe):

  <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/d7406579-cb24-40bb-a5bf-bbb4556c3b95" width=600>

  
- [**Jupyter** notebook link](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/End-to-End%20Data%20Science%20using%20Snowpark%20-%20Intermediate%20Path.ipynb):

  <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/9de5a014-2b12-48d6-a433-b2fbaae7498f" width=600>


# Please following the following instructions if you are using a Hex notebook for the workshop
Note: Hex is already configured with all the necessary Python libraries. If you select Jupyter or another Python IDE, ensure your Python environment includes [repo_meta.yaml](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/.github/repo_meta.yaml) configurations.
  
**Step 1:** choose the lab difficulty level and access the corresponding notebook
- [Easy Path](https://app.hex.tech/snowflake/hex/77904453-b834-455e-936d-c694ee757fe3/latest)
- [Intermediate Path](https://app.hex.tech/snowflake/hex/77904453-b834-455e-936d-c694ee757fe3/latest)

**Step 2:** make a duplicate of the notebook
- <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/8c5af55d-1a86-4f23-b5eb-d9e27eb1ac97" width=500>


**Step 3:** complete the Hex connection details
- <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/82b7a63c-021d-4b04-87aa-4a1b55e74a19" width=500>
- See [hol_auth.json](https://github.com/snowflakecorp/Snowpark_DataScience_HOL/blob/main/ForCustomer/hol_auth.json) for Jupyter or other Python IDE connection configuration
- <img src="https://github.com/snowflakecorp/Snowpark_DataScience_HOL/assets/120119246/3ea7ff52-38a1-47b4-ad1c-a9b6cbd56d62" width=500>

- Name: [enter your Snowflake account]
- Description: [enter a description]
- Account name: [enter your Snowflake account identifier. Ensure you use a hyphen "-", not a dot "." in your account identifier.]
  - TIP: Trying to determine your Snowflake account name? Log into Snowflake. Click your account on the bottom left corner. Select the account to expose the details. Click to copy account identifier. Replace the "." with "-". For example, NXAAXGQ.LRB86899 should be NXAAXGQ-LRB86899.
- Warehouse: WHxxx
- Database: HOL
- Schema: SCHEMAxxx
- Username: USERxxx
- Password: XXXX
- User role: ROLExxx
- Integrations: check Snowpark
- Writeback: check Allow use in writeback cells
  
**Step 4:** follow the notebook and execute completed code blocks. Run each code block as "Cell only". 
- To select "Cell only" run mode, go to the bottom right corner of your Hex notebook. Select Run mode. Then select "Cell only".

<img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/6b25d27c-91bf-4d74-a25b-04495363ee75" width=350>

- You can also select to "Cell only" run mode for each code block.

<img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/ab9afaf5-386e-4346-b5a2-5173468fa195" width=350>


**Step 5:** ensure to update the htk.get_data_connection name to match your Hex connection name
- <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/49dfbd6b-5cc2-41f2-95e7-ed1895d0b57b" width=500>


**Step 6:** complete missing code each time you see "YOUR TURN"
- <img src="https://github.com/sfc-gh-DShaw98/Snowpark_DataScience_HOL/assets/120119246/55bde225-4795-41b4-8128-358c28352449" width=500>
