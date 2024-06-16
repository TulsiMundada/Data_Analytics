# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
#from sklearn.metrics import mean_absolute_percentage_error


df=pd.read_excel("D:\\advanced analytics\Data_Files\Tablet Computer Sales.xlsx", skiprows=2)
print(df)
df["es_0p1"]=df["Units Sold"].ewm(alpha=0.1).mean()
df["es_0p2"]=df["Units Sold"].ewm(alpha=0.2).mean()
df["es_0p3"]=df["Units Sold"].ewm(alpha=0.3).mean()
print(df)
plt.plot(df[df.columns[0]],df[df.columns[1]])
plt.plot(df[df.columns[0]],df[df.columns[3]])
plt.xlabel("Week")
plt.ylabel("Units Sold")
plt.title("Exponential Smoothing alpha=0.2")
plt.show()
df=df.dropna(how='any') 
#print(mean_absolute_percentage_error(df["Units Sold"], df["es_0p2"])) #MAPE
#print(mean_squared_error(df["Units Sold"], df["es_0p2"], squared=False)) #RMSE
#print(mean_squared_error(df["Units Sold"], df["es_0p2"], squared=True)) #MSE
#print("MAD alpha 1",mean_absolute_error(df["Units Sold"], df["es_0p1"])) #MAD
#print("MAD alpha 2",mean_absolute_error(df["Units Sold"], df["es_0p2"])) #MAD
#print("MAD alpha 3",mean_absolute_error(df["Units Sold"], df["es_0p3"])) #MAD
