import yfinance as yf 
import pandas as pd 


def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    df = table[0]
    return df['Symbol'].str.replace('.', '-', regex=True).tolist()

def download_prices(tickers, start_date, end_date):
    print(f"Scaricamento di {len(tickers)} titoli...")
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    return data


def load_fundamentals(file_path="data/raw/fake_bloomberg_data.csv"):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df_pivot = df.pivot(index='Date', columns='Ticker', values='Earnings Yield')

    return df_pivot