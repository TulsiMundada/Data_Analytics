import matplotlib.pyplot as plt

import numpy as np

a = np.linspace(0,10,11)
b = a ** 4

print(a)
print(b)

x = np.arange(0,10)
y = 2 * x

print(x)
print(y)

# The plt.subplots() object will act as a more automatic axis manager
#   This makes it much easier to show multiple plots side by side

fig, axes = plt.subplots()

# Now use the axes object to add stuff to plot
axes.plot(x, y, 'r') # r = red color
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title'); #; hides Out[]
plt.show()

"""## Adding rows and columns

Then you can specify the number of rows and columns when creating the subplots() object:
"""

# Empty canvas of 1 by 2 subplots
fig, axes = plt.subplots(nrows=1, ncols=2)

# Axes is an array of axes to plot on
print(axes)
print(axes.shape)
plt.show()

# Empty canvas of 2 by 2 subplots
fig, axes = plt.subplots(nrows=2, ncols=2)
print(axes)
print(axes.shape)
plt.show()


# Use .subplots_adjust to adjust spacing manually
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(12,8))

# Parameters at the axes level
axes[0][0].plot(a,b)
axes[1][1].plot(x,y)
axes[0][1].plot(y,x)
axes[1][0].plot(b,a)

# Use left,right,top, bottom to stretch subplots
# Use wspace,hspace to add spacing between subplots
fig.subplots_adjust(left=None,
    bottom=None,
    right=None,
    top=None,
    wspace=0.9,
    hspace=0.1,)

plt.show()

