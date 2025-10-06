#Second Step: Read raw JSON files and convert them into clean CSV files
import json
import os
import pandas as pd

raw_folder = "Extract/Raw_Data"
clean_folder = "Transform/Clean_Data"
os.makedirs(clean_folder, exist_ok=True)

for file_name in os.listdir(raw_folder):
    if not file_name.endswith(".json"):
        continue

    symbol = file_name.split("_")[0]
    file_path = os.path.join(raw_folder, file_name)

    with open(file_path, "r") as f:
        data = json.load(f)

    daily_data = data.get("Time Series (Daily)")
    if not daily_data:
        print(f"No data found in {file_name}")
        continue

     

    df = pd.DataFrame(daily_data).T
    df.index.name = "date"
    df.reset_index(inplace=True)


    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. adjusted close": "adjusted_close",
        "6. volume": "volume",
        "7. dividend amount": "dividend",
        "8. split coefficient": "split_coefficient"
    })

    df['daily_change_percentage'] = ((df['close'] - df['open']) / df['open']) * 100

    df = df[['date', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend', 'split_coefficient', 'daily_change_percentage']]

    numeric_cols = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend', 'split_coefficient', 'daily_change_percentage']
    df[numeric_cols] = df[numeric_cols].astype(float)


    csv_file = os.path.join(clean_folder, f"{symbol}_daily.csv")
    df.to_csv(csv_file, index=False)
    print(f"Transformed {symbol} data saved to {csv_file}")

print("All stock data transformed successfully!")