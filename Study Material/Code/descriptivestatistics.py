# -*- coding: utf-8 -*-

import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel("I:\\advanced analytics\Data_Files\Purchase Orders.xlsx", skiprows=2)

#Measure of location
print("Mean",np.mean(df["Cost per order"]))

print("Median",np.median(df["Cost per order"]))

print("Mode",stats.mode(df["Cost per order"]))

mid_range=(np.amax(df["Cost per order"])+np.amin(df["Cost per order"]))/2

print("Mid Range",mid_range)





#Measure of dispersion

print("Variance",np.var(df["Cost per order"]))

print("Standard Deviation",np.std(df["Cost per order"]))

range=np.amax(df["Cost per order"])-np.amin(df["Cost per order"])

print("Range",range)

print("Inter Quartile Range",stats.iqr(df["Cost per order"]))

print("Z Score",stats.zscore(df["Cost per order"]))

#Measure of shapes

plt.hist(df["A/P Terms (Months)"])
#plt.hist(df["Cost per order"],bins=10)
plt.ylabel('Frequency')
plt.xlabel('A/P Terms (Months)')
plt.title('Histogram')
plt.show()

print("Skewness",stats.skew(df["A/P Terms (Months)"]))

print("Kutosis",stats.kurtosis(df["A/P Terms (Months)"]))

print("Describe",stats.describe(df["A/P Terms (Months)"]))





