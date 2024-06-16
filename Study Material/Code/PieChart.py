# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_excel("I:\\advanced analytics\Data_Files\Census Education Data.xlsx",skiprows=17,nrows=6,usecols="A,B")
print(df)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
marital_status = df[df.columns[0]].tolist()
counts = df[df.columns[1]].tolist()
ax.pie(counts, labels = marital_status,autopct='%1.2f%%')
ax.set_title('Marital Status')
plt.show()

