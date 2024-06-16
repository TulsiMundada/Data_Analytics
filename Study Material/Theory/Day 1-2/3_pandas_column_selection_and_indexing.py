import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())

# Select a single column
print(df['total_bill'])
print(type(df['total_bill']))

# Select multiple columns
# Note how its a python list of column names! Thus the double brackets.
print(df[['total_bill','tip']])

# Create new columns
df['tip_percentage'] = 100 * df['tip'] / df['total_bill']
print(df.head())

df['price_per_person'] = df['total_bill'] / df['size']
print(df.head())


# Adjust Existing Columns
df['price_per_person'] = np.round(df['price_per_person'],2)
print(df.head())

# Remove Columns
df = df.drop("tip_percentage",axis=1)
print(df.head())


# Index
print(df.head())
print(df.index)

df.set_index('Payment ID')
print(df.head())

df = df.set_index('Payment ID')
print(df.head())

df = df.reset_index() # Set it to the default integer values
print(df.head())


# Rows

# Get a single row
# Integer Based
print(df.iloc[0])

# Name Based
# First set the index to the column which will be used in locating the row
df = df.set_index('Payment ID') 

print(df.loc['Sun2959'])

# Remove a row
print(df.head())
df = df.drop('Sun2959',axis=0)
print(df.head())









