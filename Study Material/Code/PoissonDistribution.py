# -*- coding: utf-8 -*-"""


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sbn

ld=12
#probability that 6 customers will arrive during the hour
print(stats.poisson.pmf(6,ld))

#probability that maximum 6 customers will arrive during the hour
print(stats.poisson.cdf(6,ld))

#probability that more than 6 customers will arrive during the hour
print(1-stats.poisson.cdf(6,ld))

#poisson distribution
pd_df=pd.DataFrame({"x" : range(0,21),"f(x)" : list(stats.poisson.pmf(range(0,21),12))})
print(pd_df)
sbn.barplot(x=pd_df["x"], y=pd_df["f(x)"])
plt.title("Poisson Distribution")

