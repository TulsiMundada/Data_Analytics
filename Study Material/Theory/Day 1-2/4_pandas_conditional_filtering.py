import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())
'''
# Conditions

print(df['total_bill'] < 30)   # True/false

bool_series = df['total_bill'] > 30 # Save in a variable

print(bool_series)      # True/False
print(df[bool_series])  # Actual results, applying the true/false conditions

print(df[df['total_bill']>30])

# Another syntax
print(df.total_bill > 30)
print(df[df.total_bill > 30])

print(df[df['gender'] == 'Male'])
'''

# Multiple conditions
df_new = df[(df['total_bill'] > 30) & (df['gender']=='Male')]
print(df_new)

df_new = df[(df['total_bill'] > 30) & ~(df['gender']=='Male')]
print(df_new)

df_new = df[(df['total_bill'] > 30) & (df['gender']!='Male')]
print(df_new)

df_new = df[(df['total_bill'] > 30) | (df['tip'] > 5)]
print(df_new)

# Conditional is in operator
options = ['Sat','Sun']
print(df['day'].isin(options))

print(df[df['day'].isin(['Sat','Sun'])])

