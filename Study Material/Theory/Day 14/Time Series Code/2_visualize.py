import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')

# From the previous code
df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
df.set_index('yearMonth',inplace=True) # inplace will make the change permanent to the DF
print(df.head())

# Now plot
plt.figure(figsize=(10,5))
sns.lineplot(data=df,x=df.index,y=df.passengers)
plt.show()

# The graph will show patterns (e.g. seasonality - data going up and down)
# Refer to the slides for explanation
# We see in our graph two pattern: seasonality and trend















