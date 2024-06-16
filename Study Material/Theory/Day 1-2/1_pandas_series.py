import numpy as np
import pandas as pd

# Creating a series from a Python list
myindex = ['USA','Canada','England']

mydata = [1776,1867,1821]

# Just the numeric index
myser = pd.Series(data=mydata)

print(myser)

# Now the named index
myser = pd.Series(data=mydata,index=myindex)

print(myser)



# Creating a series from NumPy array
# First create a NumPy array using the earlier list
ran_data = np.random.randint(0,100,4)
print(ran_data)

names = ['Alice','Bob','Charles','Dave']

ages = pd.Series(ran_data,names)

print(ages)


# Creating a series from a dictionary

ages = {'Sammy':5,'Frank':10,'Spike':7}

print(ages)

print(pd.Series(ages))


# Using named index
# Imaginary Sales Data for 1st and 2nd Quarters for a Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

# Convert into Pandas Series
sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)

print(sales_Q1)

# Call values based on Named Index
print(sales_Q1['Japan'])

# Integer Based Location information also retained!
print(sales_Q1[0])


# Be careful with potential errors!

# Wrong Name
# print(sales_Q1['France'])

# Accidental Extra Space
# print(sales_Q1['USA '])

# Text case Mistake
# print(sales_Q1['usa'])



# Series operations
# Grab just the index keys
print(sales_Q1.keys())

# Can Perform Operations Broadcasted across entire Series
print(sales_Q1 * 2)

print(sales_Q2 / 100)


# Notice how Pandas informs you of mismatch with NaN
print(sales_Q1 + sales_Q2)

# You can fill NAN with any matching data type value you want
print(sales_Q1.add(sales_Q2,fill_value=0))

