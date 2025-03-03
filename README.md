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

## Results

- **Fare Comparison**
  - **Uber:** Highest average fare at **$20.58**.
  - **Lyft:** Average fare of **$19.97**.
  - **Yellow Taxis:** Lowest average fare at **$13.04**.

- **Trip Duration Analysis**
  - **Lyft:** Longest average trip duration at **17.93 minutes**.
  - **Yellow Taxis:** Shortest trip distances, indicating variability in service efficiency.

---

## Conclusion & Future Work

- **Service Optimization:**  
  Insights from the analysis can be used to optimize driver allocation, routes, and pricing strategies for ride-hailing services.

- **Real-Time Data Integration:**  
  Future work could incorporate real-time data streams to provide dynamic insights and improve decision-making.

- **Machine Learning Applications:**  
  There is potential to apply machine learning algorithms for predicting future ride-hailing patterns and implementing dynamic pricing models based on demand and external factors such as weather.

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

3. **Run the ETL Pipeline**
   - Use the provided MAGE scripts to extract, transform, and load the data.
   - Verify that the transformed data is successfully loaded into Google BigQuery.

4. **View Dashboards**
   - Open the PowerBI and Looker Studio dashboards to interact with the visualizations.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Data Source:** NYC Taxi and Limousine Commission (TLC) for providing the trip data.
- **Tools & Communities:** Thanks to the teams behind Google Cloud Platform, MAGE, Python, PowerBI, and Looker Studio for their exceptional support and tools.
