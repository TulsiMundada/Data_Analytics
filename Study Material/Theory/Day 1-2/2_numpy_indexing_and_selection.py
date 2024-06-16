import numpy as np

#Creating sample array
arr = np.arange(0,11)
print(arr)

# Bracket indexing and selection - similar to Python lists
#Get a value at an index
print(arr[8])

#Get values in a range
print(arr[1:5])

#Get values in a range
print(arr[0:5])


# Broadcasting
#Setting a value with index range (Broadcasting)
arr[0:5]=100
print(arr)


# Reset array, why? will be clear soon
arr = np.arange(0,11)
print(arr)

#Important notes on Slices
slice_of_arr = arr[0:6]
print(slice_of_arr)

#Change Slice
slice_of_arr[:]=99
print(slice_of_arr)
print(arr)
# Changes made are also there in our original array!
# Data is not copied, it is a view of the original array! 
# This avoids memory problems

#To get a copy, we need to be explicit
arr_copy = arr.copy()
print(arr_copy)


# 2D arrays
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

#Indexing row
print(arr_2d[1])

# Getting individual element value
# Syntax is arr_2d[row][col] or arr_2d[row,col]
print(arr_2d[1][0])
print(arr_2d[1,0])

# 2D array slicing
# Shape (2,2) from top right corner
print(arr_2d[:2,1:])

# Shape bottom row
print(arr_2d[2])

# Same thing: Shape bottom row
print(arr_2d[2,:])


# Conditional selection
arr = np.arange(1,11)
print(arr)

# Check each element of the array  against the condition arr > 4, 
#  which returns a boolean array where 
#  each element is True if the corresponding element in arr is greater than 4, 
#  and False otherwise
print(arr > 4)

# Store boolean results in another array
bool_arr = arr > 4
print(bool_arr)

# Select only those elements from the arr array where 
# the corresponding element in bool_arr is True
# It effectively filters out the elements of arr where the condition arr > 4 is True
print(arr[bool_arr])

'''
arr > 2 creates a boolean array where each element is True if 
the corresponding element in arr is greater than 2, and False otherwise

arr[arr > 2] uses this boolean array as a mask to select only the elements 
of arr where the corresponding element in the boolean array is True

The array arr is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The boolean array arr > 2 is [False False True True True True True True True True].
So, arr[arr > 2] selects only those elements of arr where the corresponding 
element in the boolean array is True, 
which are [3, 4, 5, 6, 7, 8, 9, 10]
'''
print(arr[arr > 2])

# Same as before
x = 2
print(arr[arr > x])

