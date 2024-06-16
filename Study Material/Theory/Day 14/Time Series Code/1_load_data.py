import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Find available dataset names in seaborn
print(sns.get_dataset_names())

df = sns.load_dataset('flights')
print(df.head)
# We get only year and month for the date, we need day also

# Convert the date to a YYYY-MM-DD format in a new column named yearMonth
df['yearMonth'] = "01-"+df['month'].astype(str)+"-"+df['year'].astype(str)
print(df.info())

# yearMonth is of type object - we may have problems later, so convert it into datetime
df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
print(df.info())
print(df.head())

# Make yearMonth column as the dataframe index
df.set_index('yearMonth',inplace=True) # inplace will make the change permanent to the DF
print(df.head())
