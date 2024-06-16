import numpy as np
import pandas as pd

# Combining dataframes
# Directly  "glue" together dataframes

data_one = {'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)

print(one)
print(two)

# Concatenate along rows
axis0 = pd.concat([one,two],axis=0)
print(axis0)

# Concatenate along columns
axis1 = pd.concat([one,two],axis=1)
print(axis1)

# How to bring them one below another?
two.columns = one.columns
print(pd.concat([one,two]))


# Merge
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Alice','Bob','Carol','Dave']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Alice','Yolanda','Bob']})

print(registrations)
print(logins)


# Inner Join

# Match where the key is present in BOTH tables. 
# There should be no NaNs due to the join, since by definition to be part 
#   of the Inner Join we need info in both tables.

# Notice pd.merge does not take in a list like concat
merged_df = pd.merge(registrations,logins,how='inner',on='name')
print(merged_df)

# Pandas is smart enough to figure out the key column if only one column name matches up
merged_df = pd.merge(registrations,logins,how='inner')
print(merged_df)

# Pandas reports an error if "on" key column isn't in both dataframes
# pd.merge(registrations,logins,how='inner',on='reg_id')


# Left join
# Match up AND include all rows from Left Table

merged_df = pd.merge(registrations,logins,how='left')
print(merged_df)

# Right join
# Match up AND include all rows from Right Table.

merged_df = pd.merge(registrations,logins,how='right')
print(merged_df)

# Outer join
# Match up on all info found in either Left or Right Table

merged_df = pd.merge(registrations,logins,how='outer')
print(merged_df)
