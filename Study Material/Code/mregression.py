# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
df=pd.read_excel("D:\\advanced analytics\Data_Files\Colleges and Universities.xlsx",header=2)
print(df.columns)

mlr=linear_model.LinearRegression()
mlr.fit(df[['Median SAT', 'Acceptance Rate',
       'Expenditures/Student', 'Top 10% HS']],df[['Graduation %']])
print(mlr.coef_)
print(mlr.intercept_)

print(mlr.predict([[1315,.22,26636,85]]))
X = sm.add_constant(df[['Median SAT', 'Acceptance Rate',
       'Expenditures/Student', 'Top 10% HS']])

model=sm.OLS(df[['Graduation %']],X).fit()
print(model.summary())
