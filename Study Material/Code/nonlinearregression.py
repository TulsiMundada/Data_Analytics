# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import linear_model

df=pd.read_excel("H:\\advanced analytics\Data_Files\Beverage Sales.xlsx",header=2)
print(df)
reg=linear_model.LinearRegression()

reg.fit(df[['Temperature']],df[['Sales']])
print(reg.coef_)
print(reg.intercept_)
df['Temperature2']=df['Temperature']*df['Temperature']
reg.fit(df[['Temperature','Temperature2']],df[['Sales']])
print(reg.coef_)
print(reg.intercept_)
