from src.data_loader import download_prices, load_fundamentals
from config import START_DATE, END_DATE
import pandas as pd 

print("START TEST")

fundamentals = load_fundamentals()

print("Values of last 5 Earning Yields")
print(fundamentals.tail())

tickers = fundamentals.columns.tolist()

print(f"downloading prices from {START_DATE}, to {END_DATE}")
daily_prices = download_prices(tickers, start_date=START_DATE, end_date=END_DATE)

monthly_prices = daily_prices.resample('BME').last()

print("Here the last datas on prices")
print(monthly_prices.tail())