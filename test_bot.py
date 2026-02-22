from src.data_loader import download_prices, load_fundamentals
from src.factors import calculate_risk_adjusted_momentum, calculate_combined_score
from config import START_DATE, END_DATE
import pandas as pd 

print("-- START OF THE BOT --")

print("Fundamentals loading")
fundamentals = load_fundamentals()
tickers = fundamentals.columns.tolist()

print(f"downloading prices from {START_DATE}, to {END_DATE}")
daily_prices = download_prices(tickers, start_date=START_DATE, end_date=END_DATE)
monthly_prices = daily_prices.resample('BME').last()

print("Calculating Risk-Adjusted Momentum")
momentum_df = calculate_risk_adjusted_momentum(monthly_prices)

print("Calculating Z-score and Combined Score")
final_scores = calculate_combined_score(value_df=fundamentals, momentum_df=momentum_df)

last_date = final_scores.index[-1]
final_ranking = final_scores.loc[last_date].sort_values(ascending=False)

print("=========================================")
print(f"FINAL RANKING: ({last_date.date()})")
print("=========================================")
print(f"YOU SHOULD BUY: {final_ranking.index[0]}")
print("=========================================")