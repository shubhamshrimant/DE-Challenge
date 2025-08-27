'''
This module is a simple validator of the data which will log the warning and errors.
'''

import pandas as pd
from config_ import MERGED_DATA_PATH
import logging

class DataValidator:
    @staticmethod
    def validate_data():
        try:
            merged_df = pd.read_csv(MERGED_DATA_PATH)
            if merged_df.isnull().sum().any():
                logging.warning("Missing values detected in the dataset.")
            if merged_df["Week Start Date"].duplicated().any():
                logging.error("Duplicate week dates detected in the dataset.")
            logging.info("Data validation completed successfully.")
        except Exception as e:
            raise logging.error(f"Error during data validation: {e}")
            
