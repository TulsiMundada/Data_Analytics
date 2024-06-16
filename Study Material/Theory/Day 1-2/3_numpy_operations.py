import numpy as np
arr = np.arange(0,10)
print(arr)

# Basic arithmetic
print(arr + arr)
print(arr * arr)
print(arr - arr)

# This will raise a Warning on division by zero, but not an error!
# It just fills the spot with nan
print(arr/arr)

# Also a warning (but not an error) relating to infinity
print(1/arr)

print(arr**3)


# Universal functions

# Taking Square Roots
print(np.sqrt(arr))

# Calculating exponential (e^)
print(np.exp(arr))

# Trigonometric Functions like sine
print(np.sin(arr))

# Taking the Natural Logarithm
print(np.log(arr))


# Summary statistics

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.var())
print(arr.std())


# 2D arrays

# This is a 2-dimensional array with 3 rows and 4 columns
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)

# Sum all the columns for each row (e.g. 1+5+9, 2+6+10, etc)
print(arr_2d.sum(axis=0))

# Row and column count
print(arr_2d.shape)

# Sum all the rows for each column (e.g. 1+2+3+4, 5+6+7+8, etc)
print(arr_2d.sum(axis=1))