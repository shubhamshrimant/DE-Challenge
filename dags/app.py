from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from data_generator import DataGenerator
from economic_data import EconomicDataFetcher
from data_merge import DataIntegrator
from data_validator import DataValidator
import logging
from utils import setup_logging

# Set up logging for Airflow tasks
setup_logging()

# Default DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

# Define the DAG
with DAG(
    "sales_pipeline_dag",
    default_args=default_args,
    description="A monthly pipeline for updating sales and economic data",
    schedule_interval="0 0 1 * *",  # Runs at midnight on the 1st of every month
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Task 1: Generate synthetic sales data
    def generate_sales_data():
        DataGenerator.generate_sales_data()
        logging.info("Sales data generation completed.")

    generate_data_task = PythonOperator(
        task_id="generate_sales_data",
        python_callable=generate_sales_data,
    )

    # Task 2: Fetch economic data
    def fetch_economic_data():
        fetcher = EconomicDataFetcher()
        start_date = "2024-01-01"  # Replace with dynamic logic if needed
        end_date = "2024-12-31"
        fetcher.fetch_and_save(start_date=start_date, end_date=end_date)
        logging.info("Economic data fetching completed.")

    fetch_data_task = PythonOperator(
        task_id="fetch_economic_data",
        python_callable=fetch_economic_data,
    )

    # Task 3: Merge the data
    def validate_data():
        DataValidator.validate_data()
        logging.info("Data validation completed.")

    validate_data_task = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )
    
    # Task 4: Validate the data
    def merge_data():
        DataIntegrator.merge_data()
        logging.info("Data merging completed.")

    merge_data_task = PythonOperator(
        task_id="merge_data",
        python_callable=merge_data,
    )


    # Define task dependencies
    generate_data_task >> fetch_data_task >> validate_data_task >> merge_data_task
