# -*- coding: utf-8 -*-


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sbn

#probability of failing before 5,000 hours
print(stats.expon.cdf(5000,loc=1/8000,scale=1000))

#probability that it will not fail upto 7000 hours
print(1-stats.expon.cdf(7000,loc=1/8000,scale=1000))


#exponential distribution
ed_df=pd.DataFrame({"x" : range(0,5000,100),"f(x)" : list(stats.expon.pdf(range(0,5000,100),loc=1/8000,scale=1000))})
print(ed_df)
sbn.barplot(x=ed_df["x"], y=ed_df["f(x)"])
plt.title("Exponential Distribution")
plt.xticks(rotation=90)
plt.xlabel("Time to failure")
