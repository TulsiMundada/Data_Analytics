import numpy as np
import pandas as pd

# Create a simple dataframe from an existing Python list

np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))

print(mydata)

myindex = ['CA','NY','AZ','TX']

mycolumns = ['Jan','Feb','Mar']

df = pd.DataFrame(data=mydata)
print(df)

df = pd.DataFrame(data=mydata,index=myindex)
print(df)

df = pd.DataFrame(data=mydata,index=myindex,columns=mycolumns)
print(df)

print(df.info())


# Create a dataframe from a CSV file

df = pd.read_csv('tips.csv')
print(df)

''' 
Columns
    * tip in dollars,
    * bill in dollars,
    * gender of the bill payer,
    * whether there were smokers in the party,
    * day of the week,
    * time of day,
    * size of the party.
Note: Fake columns: Name, CC Number, and Payment ID
'''

print(df.columns) # Column names

print(df.index) # Index

print(df.head(3)) # First three rows

print(df.tail(3)) # Last three rows

print(df.info()) # Information about he DF, including data types and memory used

print(len(df)) # Number of rows

print(df.describe()) # Statistical summary

print(df.describe().transpose()) # Statistical summary, better organized
