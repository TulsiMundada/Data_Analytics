import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The previous code to test stationarity is now in a function
def test_stationarity(dataFrame, var):
    dataFrame['rollMean']  = dataFrame[var].rolling(window=12).mean()
    dataFrame['rollStd']  = dataFrame[var].rolling(window=12).std()
    
    from statsmodels.tsa.stattools import adfuller
    adfTest = adfuller(dataFrame[var])
    stats = pd.Series(adfTest[0:4],index=['Test Statistic','p-value','#lags used','number of observations used'])
    print(stats)
    
    for key, values in adfTest[4].items():
        print('criticality',key,":",values)
        
    sns.lineplot(data=dataFrame,x=dataFrame.index,y=var)
    sns.lineplot(data=dataFrame,x=dataFrame.index,y='rollMean')
    sns.lineplot(data=dataFrame,x=dataFrame.index,y='rollStd')
    plt.show()


df = sns.load_dataset('flights')

df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
df.set_index('yearMonth',inplace=True) # inplace will make the change permanent to the DF

# Time shift
#air_df = df[['passengers']]
# Just get the passengers column into a new dataframe for easier testing
air_df = df[['passengers']].copy() # Double brackets because it is a list within a list


print(air_df.head())

# By default, shift is by 1 time period (here, one month)
# Create a new column which will contain the shifted value from passengers column - See slide
air_df['shift'] = air_df.passengers.shift(1)
air_df['shiftDiff'] = air_df['passengers'] - air_df['shift']
print(air_df.head(20))

# Test stationarity
test_stationarity(air_df.dropna(),'shiftDiff')
# p-value is just close to 0.05, so let us try a shift of 2

# By default, shift is by 1 time period (here, one month)
# Create a new column which will contain the shifted value from passengers column - See slide
air_df['shift'] = air_df.passengers.shift(2)
air_df['shiftDiff'] = air_df['passengers'] - air_df['shift']
print(air_df.head(20))

# Test stationarity
test_stationarity(air_df.dropna(),'shiftDiff')


# -2.96 < -2.88 and p-value = 0.03, which is < 0.05 , so, 
#   now test statistic < critical value ... now we reject H0
# Conclusion: The data has become somewhat stationary