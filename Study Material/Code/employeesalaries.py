# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

df=pd.read_excel("D:\\advanced analytics\Data_Files\Employee Salaries.xlsx",header=2)

reg=linear_model.LinearRegression()
MBA = {'No': 0,'Yes': 1} 
df.MBA = [MBA[item] for item in df.MBA] 
print(df)
reg.fit(df[['Age','MBA']].values,df[['Salary']])
print(df)
print(reg.coef_)
print(reg.intercept_)

df["Interaction"]=df["Age"]*df["MBA"]
print(df)

reg.fit(df[['Age','MBA','Interaction']].values,df[['Salary']])
print(reg.coef_)
print(reg.intercept_)

X = sm.add_constant(df[['Age','MBA','Interaction']].values)

model=sm.OLS(df[['Salary']],X).fit()
print(model.summary())

reg.fit(df[['Age','Interaction']].values,df[['Salary']])
print(reg.coef_)
print(reg.intercept_)
