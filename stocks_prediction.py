import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_absolute_percentage_error as mape
import matplotlib.pyplot as plt


def load_stock_data(company):
    # Load the dataset
    stocks = pd.read_csv('Data/stocks_close.csv', index_col=[0], parse_dates=[0])
    # Load data of selected company
    stock_data = stocks[f'{company}'].copy()
    print('Stock data: \n', stock_data)

    #  Monthly price (average), setting the trend and transforming month to binary values
    monthly_price = stock_data.resample('ME').mean().reset_index()
    monthly_price = monthly_price.assign(
        trend=monthly_price.index,
        month=monthly_price['Date'].dt.month.astype('object')
    )
    dummies = pd.get_dummies(monthly_price['month'], prefix='month', drop_first=True).astype(int)
    monthly_price = pd.concat([monthly_price.drop('month', axis=1), dummies], axis=1)
    print('Monthly price: \n', monthly_price)
    return monthly_price


def developing_model(monthly_price, company):
    # Setting train and test data sets
    train_data = monthly_price.set_index('Date').loc['2022-03-31':'2024-03-31']
    test_data = monthly_price.set_index('Date').loc['2024-04-30':]

    # Developing linear regression model
    y = train_data[f'{company}']
    X = sm.add_constant(train_data.iloc[:, 1:])
    model = sm.OLS(y, X).fit()
    y_test = test_data[f'{company}']
    X_test = sm.add_constant(test_data.iloc[:, 1:])
    prediction = model.predict(X_test)
    pred_df = pd.DataFrame({'actual': y_test, 'predicted': prediction})
    print(pred_df)

    # Evaluating model performance
    error_mape = mape(pred_df['actual'], pred_df['predicted']).round(2)
    error_mae = mae(pred_df['actual'], pred_df['predicted']).round(2)
    print('Mean absolute percentage error: ', error_mape)
    print('Mean absolute error: ', error_mae)

    plt.figure(figsize=(12, 6))
    pred_df.plot()
    plt.title(f'{company} Stock Price Prediction, mape={error_mape}')
    plt.xlabel('Month')
    plt.ylabel('Stock price')
    plt.ylim(400, 450)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return mape, mae


def main():
    company = 'MSFT'
    monthly_price = load_stock_data(company)
    developing_model(monthly_price, company)


if __name__ == '__main__':
    main()
