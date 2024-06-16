import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


advert = pd.read_csv('advertising.csv')
advert.head()

# Covariance coefficient
print(advert['TV'].cov(advert['Newspaper']))

corr = advert.corr()
print(corr['TV']['Newspaper'])
print(corr['Radio']['Newspaper'])
# OR
print(advert.TV.cov(advert.Newspaper))

# Covariance matrix
print(advert.cov())

#fmt='g' means use general format for numbers, not scientific notations
dataplot = sns.heatmap(advert.cov(), annot=True, fmt='g') 
plt.show()