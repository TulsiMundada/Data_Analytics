# -*- coding: utf-8 -*-

import pandas as pd

df=pd.DataFrame({"Quarter":[1,2,3,4],
                 "Year1":[4.8,4.1,6,6.5],
                 "Year2":[5.8,5.2,6.8,7.4],
                 "Year3":[6,5.6,7.5,7.8],
                 "Year4":[6.3,5.9,8,8.4]})
print(df)
#step 1
df_mean = df[["Year1","Year2","Year3","Year4"]].to_numpy().mean().round(1)
print(df_mean)

#step2
df["Season Average"]=df[["Year1","Year2","Year3","Year4"]].mean(axis=1).round(1)
print(df)

#step3
df["Seasonal Index"]=(df["Season Average"]/df_mean).round(1)
print(df)

df["Year1D"]=(df["Year1"]/df["Seasonal Index"]).round(1)
df["Year2D"]=(df["Year2"]/df["Seasonal Index"]).round(1)
df["Year3D"]=(df["Year3"]/df["Seasonal Index"]).round(1)
df["Year4D"]=(df["Year4"]/df["Seasonal Index"]).round(1)
print(df)
#forecasting for deseasonal data
ma=df["Year4D"].mean()

print(ma)
print("Seasonal Forecast\n",(df["Seasonal Index"]*ma).round(1))
