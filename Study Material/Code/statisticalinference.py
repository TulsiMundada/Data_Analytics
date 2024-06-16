5# -*- coding: utf-8 -*-

from statsmodels.stats.proportion import proportions_ztest
from scipy import stats
from scipy.stats import t
import pandas as pd

df=pd.read_excel("D:\\advanced analytics\Data_Files\Vacation Survey.xlsx", skiprows=2)
#ritical value
print(t.ppf(1-0.025, 33))
#pvalue and test statistics
print(stats.ttest_1samp(df["Age"],35))


print(proportions_ztest(35, 44, 0.75))
print(t.ppf(1-0.05, 43))


print(stats.ttest_ind([6,9,7,7,5,7,9,6], [3,4,5,6,5,5,5,6,5,5,5,5,5], equal_var=False))



