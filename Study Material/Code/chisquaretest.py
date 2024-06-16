# -*- coding: utf-8 -*-


import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

df=pd.read_excel("D:\\advanced analytics\Data_Files\Energy Drink Survey.xlsx", skiprows=2)
print(df)
count=len(df)
print(count)
#original frequency
table=pd.crosstab(df["Gender"],df["Brand Preference"])
print(table)
f_obs=table.loc["Female"].tolist()+table.loc["Male"].tolist()
print(f_obs)
f_obs_arr=np.array(f_obs)
f_obs_arr.shape=( 2, 3 )
print("Observation Array")
print(f_obs_arr)
print(chi2_contingency(f_obs_arr))

