# Largest tech companies: EDA and Prediction of Stock Values

### Project overview:

The main results of the project:
* Analysed and visualised stocks' values and key performance indicators of the largest tech companies: Apple, Google, 
Meta and Microsoft.
* Developed the stock price prediction model accurately predicts the value of Microsoft stocks (mean absolute 
percentage error: 0.02)

Stock data for the largest technology companies for a 10 years period (from 2014-07-01 to 2024-06-30) imported
from Yahoo using the yfinance library. 

The key performance indicators - normalised stock prices, annual stocks' return (yearly change), average of annual stock return 
have been calculated and visualised. 

Technologies used:
* Python
* Pandas
* Yfinance
* statsmodels.api
* sklearn
* Seaborn
* Matplotlib 


### Stock prices trend
The stock prices of the largest companies vary. It is notable that META's stock value are significantly higher than the 
others, except for the sharp decrease in mid-2021 to late 2023. Apple and Google stock prices are quite close in this 
decade.

![img.png](Images%2Fimg.png)

### Normalised stock prices (to the basic value)
As the stock prices of the largest companies vary, the normalized stock prices (initially changed by the basic 
value - 100), better reflect the real growth in stocks value. The largest increases in value are in Microsoft and 
Apple stocks. 

![img_1.png](Images%2Fimg_1.png)

### Stocks annual return (yearly change, %)
The stocks annual return shows that META's value skyrocked by the end of 2023. However, in 2022 the return 
on these stocks was very negative (about -70%), therefore the increase in value in the next period seems huge.

Microsoft, Apple and Google stocks have more stable and valuable annual stock returns. In 2022, there were also significant 
declines in values, but lower than META's.

![img_2.png](Images%2Fimg_2.png)

### Stocks annual return (yearly change, %) boxplot
Annual stock returns are usually in the following ranges:
* Apple - from 0% to 48%. A quarter of returns even up to 86%.
* Google - from 9% to 42%. A quarter of returns up to 65%.
* META - from 13% to 51%. A quarter up to 55%.
* Microsoft - from 19% to 49%. A quarter up to 56%.

![img_3.png](Images%2Fimg_3.png)

### Average of stocks' annual return (%)
The highest average of stock return belongs to META - 35.7%. However, the result was impacted by huge decrease in 
previous period as it was mentioned above.
The averages of other companies are quite similar: 
* Microsoft - 28.2%
* Apple - 27.6%
* Google - 25.6%

![img_4.png](Images%2Fimg_4.png)

### Stock price prediction (MSFT)
Developed the stock price prediction model (Linear regression) accurately predicts the value of Microsoft stocks. 
* Mean absolute percentage error:  0.02
* Mean absolute error:  9.11

![img_5.png](Images%2Fimg_5.png)
