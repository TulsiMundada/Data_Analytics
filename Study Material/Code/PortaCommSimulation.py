# -*- coding: utf-8 -*-

from scipy.stats import rv_discrete
from scipy.stats import uniform  
from scipy.stats import norm
import pandas as pd

sp_per_unit=249
admin_cost=400000
advt_cost=600000

#parts cost with uniform distribution
low=80
high=100

#demand with normal distribution
mean=15000
std_dev=4500

trials=500

sample = rv_discrete(values=([43, 44, 45, 46, 47],[0.1, 0.2, 0.4, 0.2, 0.1]))
df=pd.DataFrame({"Labor Cost" : sample.rvs(size=trials)})
df["Part Cost"]=uniform .rvs(low, 20, size = trials).round(2)
df["Demand"] = norm.rvs(loc=mean, scale=std_dev, size = trials).round()
df["Profit"]= (sp_per_unit-df["Labor Cost"]-df["Part Cost"])*df["Demand"]-admin_cost-advt_cost
print(df)
print("Mean Profit", df["Profit"].mean())
print("Standard Deviation", df["Profit"].std())
print("Minimum Profit", df["Profit"].min())
print("Maximum Profit", df["Profit"].max())
num_of_loss=df[df["Profit"]<0]["Profit"].count()
print("Number of losses", num_of_loss)
print("Probability of loss", num_of_loss/trials)

