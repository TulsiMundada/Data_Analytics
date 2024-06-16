import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')
df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
df.set_index('yearMonth',inplace=True) # inplace will make the change permanent to the DF

airP = df[['passengers']].copy(deep=True)
print(airP.head())

# Create columns for one month and one year lagged data
airP['firstDiff'] = airP['passengers'].diff()
airP['Diff12'] = airP['passengers'].diff(12) # This will show nulls to start with

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_pacf(airP['Diff12'].dropna(),lags=20)
plt.show() 

plot_acf(airP['Diff12'].dropna(),lags=20)
plt.show()

train = airP[:round(len(airP)*70/100)] # Take the first 70% data
test = airP[round(len(airP)*70/100):] # Take the last 30% data, starting from 71%

# First ARIMA prediction
model = ARIMA(train['passengers'],order=(1,2,3)) # Parameters: p, d, q
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['arimaPred'] = prediction

# Now SARIMAX prediction
model = SARIMAX(train['passengers'],order=(1,2,3),seasonal_order=(1,2,3,12))
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['sarimaxPred'] = prediction
print(airP.tail())
# Data looks better

# Plot
airP.dropna()
print(airP.head())
sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='sarimaxPred')
sns.lineplot(data=airP,x=airP.index,y='arimaPred')
plt.show()

# Compared to ARIMA, SARIMAX is much better

# Future prediction

# First check the last date in our dataset
print(airP.tail())

# MS: Month Start frequency
# Create a data frame to hold index values from 01.01.61 to 01.12.62
futureDate = pd.DataFrame(pd.date_range(start='1961-01-01', end='1962-12-01',freq='MS'),columns=['Dates'])
futureDate.set_index('Dates',inplace=True)
print(futureDate.head())

# Predict and print
print(model_fit.predict(start=futureDate.index[0],end=futureDate.index[-1]))

# Plot

airP.dropna()
sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='sarimaxPred')
sns.lineplot(data=airP,x=airP.index,y='arimaPred')
model_fit.predict(start=futureDate.index[0],end=futureDate.index[-1]).plot(color='black')
plt.show()
