import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)

# Load the dataset
stocks = pd.read_csv('Data/stocks_close.csv', index_col=[0], parse_dates=[0])

print(stocks.head())
print(stocks.info())

#  Visualising stock prices
plt.figure(figsize=(12, 6))
stocks.plot()
plt.title('Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Visualising normalised stock prices
stocks_norm = stocks.div(stocks.iloc[0]).mul(100)
print(stocks_norm)
plt.figure(figsize=(12, 6))
stocks_norm.plot()
plt.title('Stock Prices (normalised)')
plt.xlabel('Date')
plt.ylabel('Normalised Price (%)')
plt.legend()
plt.show()

#  Stocks' return (yearly value change)
yearly_return = stocks.resample('YE').last().pct_change(periods=1).mul(100)
print(yearly_return)

plt.figure(figsize=(12, 6))
yearly_return.plot()
plt.title("Stocks' Return (yearly change, %)")
plt.xlabel('Date')
plt.ylabel('Stocks yearly return (%)')
plt.xlim('2015', '2023')
plt.legend()
plt.show()

sns.boxplot(data=yearly_return)
plt.title('Stocks Return (yearly change, %) Boxplot')
plt.show()

ann_return_mean = yearly_return.mean().round(2).sort_values(ascending=False)
print(ann_return_mean)

sns.barplot(data=ann_return_mean)
plt.title('Stocks Annual Return (Mean, %)')
plt.xlabel('Stock')
plt.ylabel('Annual Return (%)')
plt.show()