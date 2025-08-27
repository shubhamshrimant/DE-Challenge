import requests
import pandas as pd

url = f"https://api.stlouisfed.org/fred/series/observations"
params = {
    "series_id": "GASREGW",
    "api_key": 'c419142da203d725613e39f4b4c5ff3a',
    "file_type": "json",
    "observation_start": "2024-01-01",
    "observation_end": "2024-12-31",
}
response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()["observations"]
df = pd.DataFrame(data)

print(df)

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())
