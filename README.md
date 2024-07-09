# Largest tech companies: EDA and Prediction of Stock Values

### Project overview:

The main results of the project:
* Analysed and visualised stocks' values and key performance indicators of the largest tech companies: Apple, Google, Meta and 
Microsoft.
* Developed the stock price predicting model (for Microsoft stocks).

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
![img_2.png](Images%2Fimg_2.png)

### Stocks annual return (yearly change, %) boxplot
![img_3.png](Images%2Fimg_3.png)

### Average of stocks' annual return (%)
![img_4.png](Images%2Fimg_4.png)

### Stock price prediction (MSFT)

![img_5.png](Images%2Fimg_5.png)