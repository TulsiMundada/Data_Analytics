import numpy as np
import pandas as pd

'''
groupby functionality:
1. Splitting: The data is first split into groups based on the criteria provided
2. Applying: A function (or multiple functions) is applied to each group independently
3. Combining: The results of the function applications are then combined 
   into a new DataFrame
'''

df = pd.read_csv('tips.csv')
print(df)


# 1. Splitting
df_grouped = df.groupby('gender')

# Note that the output will not have any visible impact, except for 
#   a mention of grouping
print(df_grouped)


# 2. Applying
# Calculate the mean tip for each gender
mean_tip_by_gender = df_grouped['tip'].mean()
print(mean_tip_by_gender)

print(df_grouped['tip'].min())
print(df_grouped['tip'].max())
print(df_grouped['tip'].std())
print(df_grouped['tip'].var())
print(df_grouped['tip'].count())
print(df_grouped['tip'].sum())


# Creating groups on multiple columns
df_grouped = df.groupby(['gender', 'day'])

# 3. Combining
mean_tip_by_gender_day = df_grouped['tip'].mean()
print(mean_tip_by_gender_day)


# agg function
# Apply multiple aggregation functions to different columns when grouping data
# Calculate both the mean and sum of the 'tip' column for each combination of 
#     'gender' and 'day'

# Group the DataFrame by both 'gender' and 'day' and calculate the mean and sum of 'tip' for each combination
df_grouped = df.groupby(['gender', 'day']).agg({'tip': ['mean', 'sum']}).reset_index()

# When we perform group operations using groupby(), the resulting DataFrame 
#   has a hierarchical index, known as a MultiIndex, which reflects the groups 
#   created by the grouping columns
# Resetting the index using reset_index() converts the hierarchical index 
#   into a simple integer index, making the DataFrame easier to work with 
#   and allowing us to access the grouped data more easily

# Rename the columns for clarity
df_grouped.columns = ['gender', 'day', 'mean_tip', 'total_tip']

print(df_grouped)
