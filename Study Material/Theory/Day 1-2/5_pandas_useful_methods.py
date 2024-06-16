import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')
print(df.head())

# apply function
print(df.info())

def last_four(num):
    return str(num)[-4:]

print(df['CC Number'][0])

print(last_four(3560325168603410))

df['last_four'] = df['CC Number'].apply(last_four)

# More complex use of apply()
print(df['total_bill'].mean())

def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'

df['Expensive'] = df['total_bill'].apply(yelp)
print(df.head)

# apply on multiple columns

def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
'''
add a new column Tip_Quality
Apply a Lambda function to all the rows (because axis = 1)
For each row, calculate Tip_Quality using the quality() function above
'''
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)
print(df.head())


# sort_values
print(df.sort_values('tip'))


# correlation
print(df[['total_bill','tip']].corr())


# idxmin and idxmax
print(df.head())

print(df['total_bill'].max())
print(df['total_bill'].idxmax())
print(df['total_bill'].idxmin())

print(df.iloc[67])
print(df.iloc[170])


# value_counts - get count on categorical columns
print(df['smoker'].value_counts())   # Smokers and non-smokers
print(df['gender'].value_counts())   # Males and Females


# replace one value with another
print(df.head())

df['Tip Quality'] = df['Tip Quality'].replace(to_replace='Other',value='Ok')
print(df.head())


# unique
print(df['size'].unique())   # All the unique values as an array
print(df['size'].nunique())  # Number of unique values (i.e. count of the above array)
print(df['time'].unique())   # For a char column


# map
my_map = {'Dinner':'D','Lunch':'L'}
df_new = df['time'].map(my_map) # Create a new DF only containing D or L for each row
print(df_new.head())


# duplicated and drop_duplicates
# Returns True for the 1st instance of a duplicated row
print(df.duplicated())

simple_df = pd.DataFrame([1,2,2],['a','b','c'])

print(simple_df)

print(simple_df.duplicated())  # True/False for each case

print(simple_df.drop_duplicates())


# between: options for inclusive are both, left, right, neither
print(df['total_bill'].between(10,20,inclusive='both'))     # True/false
print(df[df['total_bill'].between(10,20,inclusive='both')]) # Actual data


# Sample data, randomly selected
print(df.sample(5))             # 5 rows
print(df.sample(frac=0.1))      # 10% of rows


# nlargest and nsmallest
print(df.nlargest(10,'tip'))
print(df.nsmallest(10,'tip'))


