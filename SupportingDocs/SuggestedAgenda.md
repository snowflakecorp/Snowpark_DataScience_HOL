# Here is a suggested agenda for a 2hr workshop:

- **Welcome** (Account AE)
  
- **Snowpark for ML / AI** (Account SE) - 15 min
  - Snowflake Intro (think Joe Cramer slides)
  - Snowpark
  - Cortex

- **Roadmap & Environment Setup** - (FCTO) - 10 min
  - Environments (setup)
  - Potential items might include Feature Store, Experiment Tracking, Git Integration, etc.

- **Navigating the Snowflake Platform** - (Account SE) - 5 min
  - Potential items might include SF virtual warehouses, databases/schemas, Universal search, resource monitors, etc.

- **Snowpark Data Science HOL** - (Snowpark Expert/FCTO/Account SE) - 1 hr 30 min
  - Part 1: Data preparation & transformations using Snowpark ML API
  - Part 2: Create simple ML-powered forecast -- (quick 1min mention, can do on own time)
  - Part 3: Create ML model in Snowpark
  - Part 4: Register and operationalize ML model using Snowpark
  - Part 5: Create interactive Streamlit application leveraging Snowpark model
 
## **Notes for the Snowflake Team:**
The **Welcome** gives the Snowflake team a chance to introduce the Snowpark Expert and/or FCTO to their customers.
This is a great chance to learn of the customer has new Snowflake users.
This is a great chance to confirm the customer's AI/ML/Data Science maturity.

The **Snowpark for ML / AI** gives the Snowflake team a chance to rebrand Snowflake as a PLATFORM and not a tool, particularly not just a data warehousing tool.
This is a great time to mention the new Cortex ML and LLM features highlighted during Snowday.
Ask if these attendees attended BUILD or if they are planning to attend the next Data 4 Breakfast, Summit or Build event.

The **Roadmap & Environment Setup** is needed to hightlight that we can work from all types of Python environments. For the purpose of this HOL, we needed to pick one.
Since the HOL tends to run long, this might be a good time to address Snowflake Roadmap items you know are important.

The **Navigating the Snowflake Platform** is critical step. Don't skip this. You likely have new users. You might still have users on the original Snowflake GUI.
This is a great time to highlight some new features in Snowsight and Snowflake's ease of use.

Finally, the **Snowpark Data Science HOL** is chunked into five parts to make it easier to consume and check-in with attendees. Plan ahead with the Snowpark Expert/FCTO on where to spend your time and where to quick run through content.
If they are all strong Data Scientists, I would recommend skipping part 2.
Part 2 is a great option if they are not very mature with data science and could benefit from Cortex's easy-to-use general features. 
Part 4 is showcasing our Model Registry and what's coming with Feature Store. This might be too deep for your audience.
Part 5 is showcasing how to use Streamlit directly in Snowflake. Often customers have experience with Streamlit but not SiS. This part also includes Snowflake Geospatial features to improve the app.
  
