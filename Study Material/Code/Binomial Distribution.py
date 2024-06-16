# -*- coding: utf-8 -*-


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sbn
n=10
p=0.8

##probability that exactly 2 customers will make a purchase
print(stats.binom.pmf(2,n,p))

##probability that a maximum of 5 customers will make a purchase
print(stats.binom.cdf(5,n,p))

##probability that more than 5 customers will make a purchase
print(1-stats.binom.cdf(5,n,p))

##Expected value and variance of binomial distribution
mean,var=stats.binom.stats(n,p)
print("Mean ",mean," Variance ",var)

#Binomial Distribution
bd_df=pd.DataFrame({"x" : range(0,11),"f(x)" : list(stats.binom.pmf(range(0,11),10,p))})
print(bd_df)
sbn.barplot(x=bd_df["x"], y=bd_df["f(x)"])
plt.title("Binomial Distribution")

   









