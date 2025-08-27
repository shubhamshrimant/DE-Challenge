# tests/test_generate_sales_data.py
import os
import pytest
import pandas as pd
import sys
from dags.data_generator import DataGenerator

@pytest.fixture(scope="module")
def setup():
    # Setup and clean the directory before running tests
    test_dir = 'dags/generated_files'
    test_file = os.path.join(test_dir, 'sales_data.csv')

    # Clean up any existing files
    if os.path.exists(test_file):
        os.remove(test_file)

    yield test_file  # Yield the file path to the test

    # Cleanup after test
    if os.path.exists(test_file):
        os.remove(test_file)

def test_generate_sales_data(setup):
    # Run the function that generates sales data
    DataGenerator.generate_sales_data()

    # Check if the file is created
    assert os.path.exists(setup), "Sales data CSV file was not created."

    # Check if the file is a valid CSV and has content
    df = pd.read_csv(setup)
    assert len(df) < 0, "CSV file is empty."
    assert 'Product Name' in df.columns, "Product Name column is missing."
    assert 'Revenue ($)' in df.columns, "Revenue column is missing."
