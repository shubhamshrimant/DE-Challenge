'''
This module merges the dataframes based on week start date columns.
'''
import pandas as pd
from config_ import SALES_DATA_PATH, GAS_PRICES_PATH, CPI_DATA_PATH, MERGED_DATA_PATH
import logging

class DataIntegrator:
    @staticmethod
    def merge_data(output_path=MERGED_DATA_PATH):
        try:
            sales_df = pd.read_csv(SALES_DATA_PATH)
            gas_prices = pd.read_csv(GAS_PRICES_PATH)
            cpi_data = pd.read_csv(CPI_DATA_PATH)

            sales_df["Week Start Date"] = pd.to_datetime(sales_df["Week Start Date"])
            gas_prices["Week Start Date"] = pd.to_datetime(gas_prices["Week Start Date"])
            cpi_data["Week Start Date"] = pd.to_datetime(cpi_data["Week Start Date"])

            merged_df = sales_df.merge(gas_prices, on="Week Start Date", how="left")
            merged_df = merged_df.merge(cpi_data, on="Week Start Date", how="left")
            merged_df.rename(columns={"GASREGW": "Average Gas Price ($)", "CPIAUCSL": "CPI"}, inplace=True)
            merged_df.dropna(inplace=True)

            merged_df.to_csv(output_path, index=False)
            logging.info(f"Merged data saved to {output_path}")
        except Exception as e:
            logging.error(f"Error during data merging: {e}")
            raise
