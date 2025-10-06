# Third Step: Load cleaned CSVs into MySQL
import os
import pandas as pd
import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "Password"
DB_NAME = "stock_data"
DB_PORT = 3306

clean_data_dir = "Transform/Clean_Data"

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)
cursor = conn.cursor()

for file_name in os.listdir(clean_data_dir):
    if file_name.endswith(".csv"):
        symbol = file_name.split("_")[0]
        csv_path = os.path.join(clean_data_dir, file_name)
        df = pd.read_csv(csv_path)

        rename_map = {
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. adjusted close": "adjusted_close",
            "6. volume": "volume",
            "7. dividend amount": "dividend",
            "8. split coefficient": "split_coefficient"
        }
        df.rename(columns=rename_map, inplace=True)

        required_cols = [
            "date", "open", "high", "low", "close", "adjusted_close",
            "volume", "dividend", "split_coefficient", "daily_change_percentage"
        ]
        df = df[[col for col in required_cols if col in df.columns]]

        numeric_cols = [
            "open", "high", "low", "close", "adjusted_close",
            "volume", "dividend", "split_coefficient", "daily_change_percentage"
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        columns = df.columns.tolist()
        placeholders = ", ".join(["%s"] * len(columns))
        column_names = ", ".join([f"`{col}`" for col in columns])
        insert_query = f"INSERT INTO `{symbol}` ({column_names}) VALUES ({placeholders})"

        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row.values))

        conn.commit()
        print(f"{symbol} data loaded successfully!")

cursor.close()
conn.close()
print("All stock CSVs loaded into MySQL successfully!")
