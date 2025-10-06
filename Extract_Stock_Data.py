# This is the first step of my project: creating the extraction script to pull stock data.

import requests
import json
import os

os.makedirs("Extract/Raw_Data", exist_ok=True)


API_KEY = "GYIR5OSFGP5FSZLQ"
symbols = ["AAPL", "GOOG", "MSFT"]

for symbol in symbols:
    print (f"Fetching data for {symbol}...")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    file_path = f"Extract/Raw_Data/{symbol}_daily.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Saved {symbol} data to {file_path}")

print("All data extracted successfully.")