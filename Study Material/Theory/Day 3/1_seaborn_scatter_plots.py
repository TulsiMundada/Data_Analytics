import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dm_office_sales.csv")

print(df.head())
print(df.info())

sns.scatterplot(x='salary',y='sales',data=df)
plt.show()  # Note that seaborn is linked to matplotlib underneath

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df)
plt.show()

# hue: Color points based off a categorical feature in the DataFrame
plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,hue='division')
plt.show()

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,hue='work experience')
plt.show()
'''
# Choosing a palette from Matplotlib's cmap: 
#    https://matplotlib.org/tutorials/colors/colormaps.html

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,hue='work experience',palette='viridis')
plt.show()

# Use *s=* if you want to change the marker size to be some uniform integer value
plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,s=200)
plt.show()

plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,s=200,linewidth=0,alpha=0.2)
plt.show()


# style
# Automatically choose styles based on another categorical feature in the dataset
#   Optionally use the **markers=** parameter to pass a list of marker choices 
#   based off matplotlib, for example: ['*','+','o']
plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,style='level of education')
plt.show()

plt.figure(figsize=(12,8))
# Sometimes its nice to do BOTH hue and style off the same column
sns.scatterplot(x='salary',y='sales',data=df,style='level of education',hue='level of education',s=100)
plt.show()
'''