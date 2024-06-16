# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel("I:\\advanced analytics\Data_Files\Stock Comparisons.xlsx",skiprows=1)
labels=df[df.columns[0]]
print(labels)
df=df.drop(columns=df.columns[0])
print(df)

x = df.iloc[0].tolist()
print(x)
y = df.iloc[1].tolist()
print(y)
z = df.iloc[2].tolist()
print(z)
colors = len(df.columns) 
print(colors)
# use the scatter function
plt.scatter(x, y, s=z)
#For each point, we add a text inside the bubble
#for line in range(0,df.shape[0]):
 #    ax.text(df.x[line], df.y[line], df.group[line])
plt.xlabel('Price')
plt.ylabel('P/E')
plt.title('Stock Comparisons')
plt.show()

