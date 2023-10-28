import yfinance as yf
from yahoo_fin.stock_info import get_data

def extract_data(ticker_symbol):
    # Define the ticker symbol for the stock of interest

    apple_data = get_data(ticker_symbol, start_date="2018-01-01", end_date="2023-01-01", index_as_date=True, interval="1d")

    return apple_data
