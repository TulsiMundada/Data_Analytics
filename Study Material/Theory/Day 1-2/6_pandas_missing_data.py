import numpy as np
import pandas as pd

df = pd.read_csv('movie_scores.csv')

print(df)

# Checking and selecting for null values
print(df.isnull()) # True if column is null, else false
print(df.notnull()) # True if column is not null, else false
print (df.pre_movie_score.sum())
'''
print(df['first_name'])
print(df[df['first_name'].notnull()])

print(df[(df['pre_movie_score'].isnull()) & df['gender'].notnull()])


# dropna
print(df.dropna())                  # Drop row if any column contains a null

print(df.dropna(thresh=1))          # Any row with at least one non-null value is retained

print(df.dropna(axis=1))            # Drop a column that contains at least one null

print(df.dropna(thresh=4,axis=1))   # A column must have at least 4 non-null values to be retained


# Fill data
df.fillna("NEW VALUE!")

print(df['first_name'].fillna("Empty"))
df['first_name'] = df['first_name'].fillna("Empty")

# Fill nulls with with average
print(df['pre_movie_score'].mean())
df['pre_movie_score'].fillna(df['pre_movie_score'].mean())
'''



