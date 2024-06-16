# -*- coding: utf-8 -*-

import pandas as pd
from scipy import stats

df=pd.read_excel("D:\\advanced analytics\Data_Files\Pile Foundation.xlsx", skiprows=3)
print(df)

print(stats.ttest_rel(df["Estimated"],df["Actual"]))
