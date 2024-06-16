# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel("I:\\advanced analytics\Data_Files\China Trade Data.xlsx",skiprows=2,usecols="A,B")
print(df)

x = df[df.columns[0]].tolist()
y = df[df.columns[1]].tolist()
plt.xlabel('Year')
plt.ylabel('US Exports to China in billions of dollars')
plt.title('China Export Data')
plt.plot(x,y)
plt.show()

