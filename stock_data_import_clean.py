import pandas as pd
import yfinance as yf


#  Setting output (display) settings
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)

#  Importing and saving stock data
companies = ['AAPL', 'MSFT', 'META', 'GOOG', 'AMZN', 'BKNG']
stocks = yf.download(companies, start='2014-07-01', end='2024-06-30')
stocks.to_csv('Data/stocks.csv')

# Loading stock data
stocks = pd.read_csv('Data/stocks.csv', header=[0, 1], index_col=[0], parse_dates=[0])

#  First data analysis
print(stocks.head(10))
print(stocks.info())
print(stocks.describe())

#  Saving closing price for upcoming EDA
stocks_close = stocks.loc[:, 'Close'].copy()
print(stocks_close.head())
stocks_close.to_csv('Data/stocks_close.csv')

