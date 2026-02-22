import pandas as pd 
import numpy as np 
import os

os.makedirs('data/raw', exist_ok=True)

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
monthly_dates = pd.date_range(start="2015-01-01", end="2023-12-31", freq='BME')

data_list = []

for date in monthly_dates:
    for ticker in tickers:
        fake_value = np.random.uniform(0.02, 0.08)

        row = {
            "Date": date, 
            "Ticker": ticker,
            "Earnings Yield": fake_value
        }

        data_list.append(row)

df = pd.DataFrame(data_list)

file_path = "data/raw/fake_bloomberg_data.csv"

df.to_csv(file_path, index=False)

print(f"Finished! File successfully created at: {file_path}")