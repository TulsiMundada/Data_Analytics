# -*- coding: utf-8 -*-

# import uniform distribution
from scipy.stats import uniform
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import seaborn as sbn
a=1000
b=2000

#probability density function
print(uniform.pdf(1200, loc = 1000, scale=1000))

#Probability that sales revenue would be less than x=$1,300
print(uniform.cdf(1300, loc = 1000, scale=1000))

#Probability that revenue will be between $1,500 and $1,700
print(uniform.cdf(1700, loc = 1000, scale=1000)-uniform.cdf(1500, loc = 1000, scale=1000))

print("Variance", uniform.var(loc=1000, scale=1000))
mean,var=uniform.stats(loc=1000, scale=1000)
print("Expected Value ", mean, " Variance ", var)

n = 10
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)
print(data_uniform)


print("Demand is utmost 900 ", norm.cdf(900, loc = 750, scale=100))
print("Demand exceed 700 ", 1-norm.cdf(700, loc = 750, scale=100))
print("Demand is between 700 and 900 ", norm.cdf(900, loc = 750, scale=100)-norm.cdf(700, loc = 750, scale=100))



print(norm.pdf(500, loc = 750, scale=100))
print(norm.ppf(0.9331, loc = 750, scale=100))

data_norm = norm.rvs(size=10, loc = 750, scale=100)
print(data_norm)


df=pd.read_excel("D:\\advanced analytics\Data_Files\Purchase Orders.xlsx", skiprows=2)

mean, var  = stats.distributions.norm.fit(df["Cost per order"])

x = np.linspace(0,125000,94)
print(x)

fitted_data = stats.distributions.norm.pdf(x, mean, var)

plt.hist(df["Cost per order"], bins=20, density=True)
plt.plot(x,fitted_data,'r-')
plt.show()

sbn.distplot(df["Cost per order"], label="Cost per order")
plt.xlabel("Gain")
plt.xlabel("Density")
plt.legend()






