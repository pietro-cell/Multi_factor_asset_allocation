import pandas as pd 
import numpy as np 

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import WEIGHTS

def calculate_z_score(df):
    z_scores = df.apply(lambda x: (x - x.mean()) / x.std(), axis=1)
    return z_scores

def calculate_risk_adjusted_momentum(prices_df):
    monthly_returns = prices_df.pct_change()
    momentum_return = (prices_df.shift(1) / prices_df.shift(12)) - 1
    volatility = monthly_returns.rolling(window=12).std().shift(1)

    risk_adjusted_momentum = momentum_return / volatility
    return risk_adjusted_momentum

def calculate_combined_score(value_df, momentum_df):
    z_value = calculate_z_score(value_df)
    z_momentum = calculate_z_score(momentum_df)

    value_w = WEIGHTS["value"]
    momentum_w = WEIGHTS["momentum"]

    combined_score = (z_value * value_w) + (z_momentum * momentum_w)

    return combined_score