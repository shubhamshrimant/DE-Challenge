'''
This module calls the api and gets the data for gas prices and cpi.
'''
import pandas as pd
import requests
from config_ import FRED_API_KEY, GAS_PRICES_PATH, CPI_DATA_PATH
import logging

class EconomicDataFetcher:
    def __init__(self, api_key=FRED_API_KEY):
        self.api_key = api_key

    def fetch_fred_data(self, series_id, start_date, end_date):
        try:
            url = f"https://api.stlouisfed.org/fred/series/observations"
            params = {
                "series_id": series_id,
                "api_key": self.api_key,
                "file_type": "json",
                "observation_start": start_date,
                "observation_end": end_date,
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()["observations"]
            df = pd.DataFrame(data)
            df = df[["date", "value"]]
            df.columns = ["Week Start Date", series_id]
            df["Week Start Date"] = pd.to_datetime(df["Week Start Date"])
            df[series_id] = pd.to_numeric(df[series_id], errors="coerce")
            logging.info(f"Fetched data for {series_id}")
            return df
        except Exception as e:
            logging.error(f"Error fetching data for {series_id}: {e}")
            raise

    def fetch_and_save(self, start_date="2024-01-01", end_date="2024-12-31"):
        gas_prices = self.fetch_fred_data("GASREGW", start_date, end_date)
        cpi_data = self.fetch_fred_data("CPIAUCSL", start_date, end_date)

        gas_prices.to_csv(GAS_PRICES_PATH, index=False)
        cpi_data.to_csv(CPI_DATA_PATH, index=False)
        logging.info("Economic data fetched and saved.")
