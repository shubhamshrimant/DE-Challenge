'''
This file is to store configurations, mainly paths. API key should not be stored like this rather in .env file, 
using dot_env should be read.
'''

import os
# FRED API Key
FRED_API_KEY = "c419142da203d725613e39f4b4c5ff3a" #should be in .env and in gitignore

# Data paths
BASE_DIR = "/opt/airflow/dags/generated_files"

if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
SALES_DATA_PATH = os.path.join(BASE_DIR, "synthetic_sales_data.csv")
GAS_PRICES_PATH = os.path.join(BASE_DIR, "gas_prices.csv")
CPI_DATA_PATH = os.path.join(BASE_DIR, "cpi_data.csv")
MERGED_DATA_PATH = os.path.join(BASE_DIR, "merged_sales_data.csv")
