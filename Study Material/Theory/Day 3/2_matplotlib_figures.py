import matplotlib.pyplot as plt

# Matplotlib Object Oriented Method

import numpy as np

a = np.linspace(0,10,11)
b = a ** 4

print(a)
print(b)

x = np.arange(0,10)
y = 2 * x

print(x)
print(y)

# Creating a Figure

# The main idea in using the more formal Object Oriented method is to create a
#   figure object and then just call methods or attributes off of that object -
#   This approach is nicer when dealing with a canvas that has multiple plots on it

# Create an empty canvas
fig = plt.figure()
# Add set of axes to figure
axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)
# Plot on that set of axes
axes.plot(x, y)
plt.show()


# Create Figure (empty canvas)
fig = plt.figure()
# Add set of axes to figure
axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)
# Plot on that set of axes
axes.plot(a, b)
plt.show()

# Adding another set of axes to the Figure
# So far we have only seen one set of axes on this figure object, 
#   but we can keep adding new axes on to it at any location and size we want
#   We can then plot on that new set of axes
# Code is a little more complicated, but the advantage is that we now 
#   have full control of where the plot axes are placed, and we can easily 
#   add more than one axis to the figure
#   Note how we are plotting a, b twice here
# Create blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0, 0, 1, 1]) # Large figure
axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5]) # Smaller figure

# Larger Figure Axes 1
axes1.plot(a, b)

# Use set_ to add to the axes figure
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Big Figure')

# Insert Figure Axes 2
axes2.plot(a,b)
axes2.set_title('Small Figure');

plt.show()


# Let's move the small figure and edit its parameters

# Create blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0, 0, 1, 1]) # Large figure
axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25]) # Smaller figure

# Larger Figure Axes 1
axes1.plot(a, b)

# Use set_ to add to the axes figure
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Big Figure')

# Insert Figure Axes 2
axes2.plot(a,b)
axes2.set_xlim(8,10)
axes2.set_ylim(4000,10000)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Zoomed In');

plt.show()

