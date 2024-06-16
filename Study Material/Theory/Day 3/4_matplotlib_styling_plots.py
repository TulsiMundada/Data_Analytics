import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = 2 * x

# Legends
# We can use the **label="label text"** keyword argument when plots or 
#   other objects are added to the figure, and then using the 
#   **legend** method without arguments to add the legend to the figure

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()
plt.show()

# Try some of the code below ...
# Notice how legend could potentially overlap some of the actual plot!

# The **legend** function takes an optional keyword argument **loc** 
#   that can be used to specify where in the figure the legend is to be drawn
#   The allowed values of **loc** are numerical codes for the various 
#   places the legend can be drawn
# Lots of options....
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=1) # upper right corner
plt.show()

# ax.legend(loc=2) # upper left corner
# ax.legend(loc=3) # lower left corner
# ax.legend(loc=4) # lower right corner

# Most common to choose
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=0) # let matplotlib decide the optimal location
plt.show()

# Setting colors, linewidths, linetypes

# Matplotlib gives you *a lot* of options for customizing colors, linewidths, 
#   and linetypes
# There is the basic MATLAB like syntax (which I would suggest you 
#   avoid using unless you already feel really comfortable with MATLAB)
#   Instead let's focus on the keyword parameters
### Colors with MatLab like syntax
# With matplotlib, we can define the colors of lines and other graphical 
#   elements in a number of ways
#   First of all, we can use the MATLAB-like syntax where `'b'` means blue, 
#   `'g'` means green, etc
#   The MATLAB API for selecting line styles are also supported: 
#   where, for example, 'b.-' means a blue line with dots:

# MATLAB style line color and style
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'g--') # green dashed line
plt.show()

# Suggested Approach: Use keyword arguments
### Colors with the color parameter
# We can also define colors by their names or RGB hex codes and 
#   optionally provide an alpha value using the `color` and `alpha` keyword arguments
#   Alpha indicates opacity

fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue", alpha=0.5) # half-transparant
ax.plot(x, x+2, color="#8B008B")        # RGB hex code
ax.plot(x, x+3, color="#FF8C00")        # RGB hex code
plt.show()


# Line and marker styles

## Linewidth

# To change the line width, we can use the `linewidth` or `lw` keyword argument.

fig, ax = plt.subplots(figsize=(12,6))

# Use linewidth or lw
ax.plot(x, x-1, color="red", linewidth=0.25)
ax.plot(x, x-2, color="red", lw=0.50)
ax.plot(x, x-3, color="red", lw=1)
ax.plot(x, x-4, color="red", lw=10)
plt.show()


# Linestyles

# There are many linestyles to choose from, here is the selection:
# possible linestype options ‘--‘, ‘–’, ‘-.’, ‘:’, ‘steps’
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x-1, color="green", lw=3, linestyle='-') # solid
ax.plot(x, x-2, color="green", lw=3, ls='-.') # dash and dot
ax.plot(x, x-3, color="green", lw=3, ls=':') # dots
ax.plot(x, x-4, color="green", lw=3, ls='--') # dashes
plt.show()


# Markers
fig, ax = plt.subplots(figsize=(12,6))

# Use marker for string code
# Use markersize or ms for size
ax.plot(x, x-1,marker='+',markersize=20)
ax.plot(x, x-2,marker='o',ms=20) #ms can be used for markersize
ax.plot(x, x-3,marker='s',ms=20,lw=0) # make linewidth zero to see only markers
ax.plot(x, x-4,marker='1',ms=20)
plt.show()

# Custom marker edges, thickness,size,and style
fig, ax = plt.subplots(figsize=(12,6))

# marker size and color
ax.plot(x, x, color="black", lw=1, ls='-', marker='s', markersize=20,
        markerfacecolor="red", markeredgewidth=8, markeredgecolor="blue");
plt.show()