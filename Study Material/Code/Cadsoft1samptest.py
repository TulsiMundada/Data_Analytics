# -*- coding: utf-8 -*-


import pandas as pd
from scipy import stats
from scipy.stats import t

df=pd.read_excel("D:\\advanced analytics\Data_Files\CadSoft Technical Support Response Times.xlsx", skiprows=2)
print(df)
#critical value
print(t.ppf(1-0.05, 43))

#test statistcis and pvalue
print(stats.ttest_1samp(df[" Time (min)"],25))
