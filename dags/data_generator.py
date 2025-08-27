'''
This module will generate random data for sales.
'''

import pandas as pd
import random
from datetime import datetime, timedelta
from config_ import SALES_DATA_PATH
import logging
import os
LOCAL_FILE_DIR = "/opt/airflow/dags/generated_files"  # This is the directory inside the container
os.makedirs(LOCAL_FILE_DIR, exist_ok=True)
class DataGenerator:
    @staticmethod
    def generate_sales_data(output_path=SALES_DATA_PATH):
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 31)
        num_products = 50
        product_names = [f"Product_{i}" for i in range(1, num_products + 1)]
        products = {f"PID_{i}": product_names[i-1] for i in range(1, num_products + 1)}

        data = []
        current_date = start_date
        while current_date <= end_date:
            for product_id, product_name in products.items():
                units_sold = random.randint(10, 500)
                base_price = random.uniform(5, 100)
                discount = random.choice([0, 0.1, 0.15, 0.2])
                revenue = units_sold * base_price * (1 - discount)
                data.append({
                    "Week Start Date": current_date.strftime("%Y-%m-%d"),
                    "Product ID": product_id,
                    "Product Name": product_name,
                    "Units Sold": units_sold,
                    "Price ($)": round(base_price, 2),
                    "Discount (%)": round(discount, 2),
                    "Revenue ($)": round(revenue, 2),
                    "Region": "USA"
                })
            current_date += timedelta(weeks=1)

        if not os.path.exists(LOCAL_FILE_DIR):
            os.makedirs(LOCAL_FILE_DIR)
            logging.info(f"Created directory: {LOCAL_FILE_DIR}")
        
        # Define the CSV file path
        local_csv_path = os.path.join(LOCAL_FILE_DIR, 'synthetic_sales_data.csv')
        sales_df = pd.DataFrame(data)

        sales_df.to_csv(output_path, index=False)
        local_csv_path = os.path.join(LOCAL_FILE_DIR, "sales_data.csv")
        sales_df.to_csv(local_csv_path, index=False)
        logging.info(f"Sales data generated and saved to {output_path}")
