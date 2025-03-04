# Urban Taxi Data Analytics

This project analyzes 85 million trip records from NYC yellow taxis, Uber, and Lyft for the third quarter of 2023. The goal is to uncover hidden trends in pricing, trip duration, and profitability to improve service quality, while providing an interactive interface for comparing ride-hailing options in real time.

---

## Skills & Tools Used

- **Google Cloud Platform (GCP)**
  - Google Cloud Storage: Data storage in Parquet format.
  - Google BigQuery: SQL-based data analysis.
- **MAGE**
  - Building and managing the ETL (Extract, Transform, Load) pipeline.
- **Google Colab & Python**
  - Data cleaning, transformation, and pre-processing.
- **PowerBI & Looker Studio**
  - Visualization of results and creation of interactive dashboards.

---

## Project Description

- **Data Source:**  
  Trip data was sourced from the NYC Taxi and Limousine Commission (TLC).

- **Objective:**  
  - Uncover hidden trends in pricing, trip duration, and profitability.
  - Develop an interface for real-time comparison of ride-hailing options based on cost and duration.
  - Create interactive visualizations to help users make informed decisions.

---

## Project Workflow

1. **Data Collection**
   - Trip data is stored in Google Cloud Storage in Parquet format.
2. **ETL Pipeline**
   - Built with MAGE to extract, clean, and transform the data.
   - Transformed data is then loaded into Google BigQuery for further analysis.
3. **Data Modeling**
   - Designed two fact tables and three dimension tables (trip details, vendors, and locations) using a star schema.
4. **Visualization & Dashboard**
   - PowerBI dashboards and Looker Studio visualizations were created to display the analysis and insights.

---

## Conclusion & Future Work

- **Service Optimization:**  
  Insights from the analysis can be used to optimize driver allocation, routes, and pricing strategies for ride-hailing services.

- **Real-Time Data Integration:**  
  Future work could incorporate real-time data streams to provide dynamic insights and improve decision-making.

- **Machine Learning Applications:**  
  There is potential to apply machine learning algorithms for predicting future ride-hailing patterns and implementing dynamic pricing models based on demand and external factors such as weather.

---
## Repository Files

1. **Analytics_SQL_Scripts.txt**  
   Contains advanced SQL queries used for in-depth analysis of the taxi dataset (e.g., daily revenue, hourly trends, top locations).

2. **BDA Presentation.pptx**  
   A presentation file summarizing the Big Data Analytics project scope, methodology, and findings.

3. **BDA Project Report.docx**  
   A detailed project report describing the data sources, objectives, analyses, and results of the taxi data project.

4. **BigDataYellowTaxiCleaning.ipynb**  
   A Jupyter notebook demonstrating the data cleaning process for NYC Yellow Taxi data, tailored for big data environments.

5. **Data_Cleaning_Final.ipynb**  
   The finalized data cleaning pipeline in a Jupyter notebook, ensuring quality and consistency before loading into the data warehouse.

6. **Dimension Data.zip**  
   A compressed file containing dimension data (e.g., CSVs or scripts) that define the star schema structure (vendor, date, rate code, etc.).

7. **ER_Diagram.png**  
   An Entity Relationship Diagram illustrating the star schema design for the taxi data warehouse, showing fact and dimension tables.

8. **Join_SQL_Script.txt**  
   SQL scripts demonstrating how to join the fact and dimension tables, creating unified views or materialized tables for analytics.

9. **README.md**  
   The main documentation file providing an overview of this repository and instructions on how to use its contents.

10. **data_dictionary_trip_records_yellow_taxi.csv**  
    A CSV file that describes each field in the NYC Yellow Taxi trip records, including data types and definitions.

11. **data_sourcing_api.py**  
    A Python script for sourcing or ingesting data from an external API, used in the pipeline to fetch and prepare taxi trip data.

12. **requirements.txt**  
    A list of Python dependencies required to run the notebooks and scripts (use `pip install -r requirements.txt`).

13. **script_schedule_job.txt**  
    Documentation or instructions for scheduling jobs (e.g., via cron or other schedulers) to automate data processing tasks.

14. **trip_record_user_guide.pdf**  
    A user guide explaining how to interpret and work with the taxi trip record dataset, including usage tips and best practices.


---


## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/nyc-ridehailing-data-analysis.git

2. **Install Dependencies**
   - Ensure you have Python 3.x installed.
   - Install necessary libraries:
     ```bash
     pip install -r requirements.txt
     ```
---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Data Source:** NYC Taxi and Limousine Commission (TLC) for providing the trip data.
- **Tools & Communities:** Thanks to the teams behind Google Cloud Platform, MAGE, Python, PowerBI, and Looker Studio for their exceptional support and tools.
