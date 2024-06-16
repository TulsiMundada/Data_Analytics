import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')

plt.figure(figsize=(10,5))
sns.lineplot(data=df,x=df.index,y=df.passengers)
plt.show()

# The graph will show patterns (e.g. seasonality - data going up and down)
# Refer to the slides for explanation
# We see in our graph two pattern: seasonality and trend

# Check further for seasonality and trend
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df.passengers, period=12)
fig = decomposition.plot()
plt.show()
# Upward trend and clear seasonality


# Calculate and plot rolling mean and standard deviation for 12 months
df['rollMean']  = df.passengers.rolling(window=12).mean()
df['rollStd']  = df.passengers.rolling(window=12).std()

print (df['rollMean'])
print (df['rollStd'])

plt.figure(figsize=(10,5))
sns.lineplot(data=df,x=df.index,y=df.passengers)
sns.lineplot(data=df,x=df.index,y=df.rollMean)
sns.lineplot(data=df,x=df.index,y=df.rollStd)
plt.show()

# Conclusion: Mean is not stationary, SD is stationary; so our data is not stationary

# Now let us perform the ADF test
from statsmodels.tsa.stattools import adfuller
adfTest = adfuller(df['passengers'])

print(adfTest) # Let us interpret these values below by converting into a series

stats = pd.Series(adfTest[0:4],index=['Test Statistic','p-value','#lags used','number of observations used'])
print(stats)

for key, values in adfTest[4].items():
    print('criticality',key,":",values)

# We will see that our Test statistic > Critical value in all the cases, so we do not reject the null hypothesis. It means that our data is not stationary.
