Project: Automated Sales and Economic Data Integration Pipeline

This project provides an automated pipeline for generating synthetic sales data, integrating it with external economic indicators, and storing the merged data locally and in an Airflow setup. The pipeline is designed to handle regular updates, ensure data integrity, and provide logging for monitoring.

### Synthetic sales data creation
- Synthetic data generation -> weekly sales data for 50 products.
- includes fields like weekly start date, product id, etc
- also considered discounts

### Economic Data Integration
- Fetches weekly gas and CPI using FRED api
- merges this data with sales by week

### Automation
- automated pipeline using airflow which will run monthly
- data saved both locally and in airflow env

### Data integrity checks
- ensured null values are dropped.
- logs for duplicates or missing data.

### Logging
- logs all operations into central log file
- Tracks errors and warnings and status of each task.


### Setup Instructions

1. Install docker, docker-compose and requirements.txt (pip install -r requirements.txt)
2. Python 3.8 or higher. I have used 3.10
3. Setup environment variable.
4. setup docker compose and airflow ->
 1. docker-compose up airflow-init
 2. docker-compose up
5. to run the airflow locally use http://localhost:8080 (username passwords are default - airflow, airflow)
6. Enable the dag of pipeline sales_pipeline_dag and trigger it.
7. Monitor the execution and logs.

### Usage
DAG can be run manually from airflow or it is scheduled monthly.

### Data
locally data is generated in generated_files folder, whilst in apache those are is container  /opt/airflow/generated_files/

### Testing

Have written a testcase due to time availabilty, and can be run using pytest tests


To run this code without airflow, open only dags folder and run app.py. Folder structure should be managed.