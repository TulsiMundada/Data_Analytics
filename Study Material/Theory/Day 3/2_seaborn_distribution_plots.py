import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dm_office_sales.csv")


# rugplot: One mark per data point - needs a single array, not useful for large data
#   y-axis does not represent anything and x-axis is just a stick per data point

sns.rugplot(x='salary',data=df)
sns.rugplot(x='salary',data=df,height=0.5)
plt.show()



# displot: Distribution of a single feature
# It is a histogram with the option of adding KDE plot on top of histogram
# KDE: Explained later in the code

sns.displot(data=df,x='salary',kde=False)
plt.show()

sns.displot(data=df,x='salary',kde=True)
plt.show()

# bins
sns.histplot(data=df,x='salary',bins=10)
plt.show()

sns.histplot(data=df,x='salary',bins=100)
plt.show()
'''
# grid - Options: darkgrid, whitegrid, dark, white, ticks
sns.set(style='darkgrid')
sns.histplot(data=df,x='salary',bins=100)
plt.show()

sns.set(style='white')
sns.histplot(data=df,x='salary',bins=100)
plt.show()

# Adding matplotlib keywords directly (Note: Not all keywords will work in all plots)
sns.displot(data=df,x='salary',bins=20,kde=False,
            color='red',edgecolor='black',lw=4,ls='--')
plt.show()


# KDE (Kernel Density Estimation) plot
# Maps an estimate of a probability *density* function of a random variable
#  Kernel density estimation is a fundamental data smoothing problem where 
#  inferences about the population are made, based on a finite data sample
np.random.seed(42)

# randint should be uniform, each age has the same chance of being chosen
#   note: in reality ages are almost never uniformally distributed, but this 
#   is just an example
sample_ages = np.random.randint(0,100,200)
print(sample_ages)

sample_ages = pd.DataFrame(sample_ages,columns=["age"])
print(sample_ages.head())

sns.rugplot(data=sample_ages,x='age')
plt.show()

plt.figure(figsize=(12,8))
sns.displot(data=sample_ages,x='age',bins=10,rug=True)
plt.show()

plt.figure(figsize=(12,8))
sns.displot(data=sample_ages,x='age',bins=10,rug=True,kde=True)
plt.show()

sns.kdeplot(data=sample_ages,x='age')
plt.show()

# Cut-off KDE 
#  We could cut off the KDE if we know our data has hard limits 
#   (no one can be a negative age and no one in the population can be older than 100 
#    for some reason)

plt.figure(figsize=(12,8))
sns.kdeplot(data=sample_ages,x='age',clip=[0,100])
plt.show()

# Basic styling of KDE plot
sns.kdeplot(data=sample_ages,x='age',bw_adjust=0.5,fill=True,color='red')
plt.show()
'''