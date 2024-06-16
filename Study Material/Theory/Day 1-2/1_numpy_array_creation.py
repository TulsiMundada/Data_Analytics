import numpy as np
'''
my_list = [1,2,3]
my_array = np.array([1,2,3])

print(type(my_list))

# Create a numpy array from a list
print(np.array(my_list))

# Or from a list of list
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_matrix))


# Creating arrays using built-in functions
# Return evenly spaced values within a given interval
# start, stop, step
print(np.arange(0,10))
print(np.arange(0,11,2))

# Generate arrays of zeros or ones

print(np.zeros(3))
print(np.zeros((5,5)))
print(np.ones(3))
print(np.ones((3,3)))

# Return evenly spaced numbers over a specified interval
# start, stop, number of elements (and not step)
# Unlike numpy.arange(), the stop value is included in the result
# The spacing between values is automatically determined based on the 
#  specified number of values (num)
print(np.linspace(0,10,3))
print(np.linspace(0,5,20))
print(np.linspace(0,5,21))

# Random number arrays
print(np.random.rand(2))
print(np.random.rand(5,5))

# From normal distribution
print(np.random.randn(2))
print(np.random.randn(5,5))
'''
# Random integers from low (inclusive) to high (exclusive)
print(np.random.randint(1,100)) # Single random integers between 1 and 100
print(np.random.randint(1,100,10)) # 10 random integers between 1 and 100

# Seeding for reproducable results
np.random.seed(77)
print(np.random.rand(4)) # 4 random numbers 

np.random.seed(77)
print(np.random.rand(4))

# Storing
arr = np.arange(25) # numbers from 0 to 24
ranarr = np.random.randint(0,50,10) # 10 random numbers between 0 and 50

print(arr)
print(ranarr)

# reshape: Returns an array containing the same data with a new shape
print(arr.reshape(5,5))

# Max, Min and their index positions
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())