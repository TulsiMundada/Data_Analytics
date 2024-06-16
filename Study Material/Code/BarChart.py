# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel("I:\\advanced analytics\Data_Files\EEO Employment Report.xlsx",skiprows=2,nrows=3)
legends=df[df.columns[0]].tolist()
print(legends)
df=df.drop(columns=df.columns[0])
df=df.drop(df.columns[0],axis=1)

print(type(df.iloc[0]))

N = len(df.columns)
print(N)

all_employees = df.iloc[0].tolist()
men=df.iloc[1].tolist()
women = df.iloc[2].tolist()

ind = np.arange(N) 
width = 0.25       
plt.bar(ind, all_employees, width, label=legends[0])
plt.bar(ind + width, men, width,
    label=legends[1])
plt.bar(ind + 2*width, women, width,    label=legends[2])

plt.ylabel('Number Employed')
plt.xlabel('Groups and Genders')
plt.title('Alabama Employment')

print(df.iloc[0].index.tolist())
plt.xticks(ind + width / 2, df.iloc[0].index.tolist(),rotation=90)
plt.legend(loc='best')
plt.show()




