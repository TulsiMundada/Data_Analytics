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
airP['Diff12'] = airP['passengers'].diff(12) # This will be used later in SARIMAX

print(airP.head())

# Now ARIMA
# In google colab, you may need !pip install pmdarima
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_pacf(airP['firstDiff'].dropna(),lags=20)
plt.show()
# Shaded area is insignificant area
# PACF gives us the auto regressive values (i.e. p - Refer to the slides)
# First 'p' is 1 (the x-axis coordinate), whose value is ~0.31 (the y-axis coordinate)
# So, significant p values are 1, 2, 4, 6, etc) 

# Now let us take this value as p and find q, for which we need ACF
plot_acf(airP['firstDiff'].dropna(),lags=20)
plt.show()
# Results of ACF are similar to that of PACF
# Interpretation: We got q. Significant q values are 1, 3, 4, 8, etc) 

# Let us take p = 1, q = 3 (both are significant) and d = 2 (already known)

# Build ARIMA model
train = airP[:round(len(airP)*70/100)] # Take the first 70% data
print(train.tail()) # Just to check where it ends

test = airP[round(len(airP)*70/100):] # Take the last 30% data, starting from 71%
print(test.head()) # Just to check where it starts

model = ARIMA(train['passengers'],order=(1,2,3)) # Parameters: p, d, q
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['arimaPred'] = prediction
print(airP.tail())

# Plot

sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='arimaPred')
plt.show()

# Conclusion: The ARIMA prediction is not good

