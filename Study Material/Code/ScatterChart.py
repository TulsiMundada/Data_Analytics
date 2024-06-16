# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df=pd.read_excel("I:\\advanced analytics\Data_Files\Home Market Value.xlsx",skiprows=2)
print(df)
square_feet = df["Square Feet"].tolist()
market_value = df["Market Value"].tolist()
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(square_feet, market_value, color='r')
ax.set_xlabel('Square Feet')
ax.set_ylabel('Market Value')
ax.set_title('Home Market Value')
plt.show()

#Measure of association
print("Covariance ",np.cov(square_feet,market_value))
print("Correlation ",stats.pearsonr(square_feet,market_value))
#sbn.regplot(x="Square Feet",y="Market Value", data=df)
