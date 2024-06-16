# COMMON MISTAKE!
# DON'T FORGET THE .PYPLOT part

import matplotlib.pyplot as plt
import numpy as np

# Basic Array Plot

x = np.arange(0,10)
y = 2*x

print(x)
print(y)

# Line plot
plt.plot(x, y)
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('Plot Title Here')
plt.show() # Required for non-jupyter users , but also removes Out[] info

# More features
plt.plot(x, y)
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('Plot Title Here')
plt.xlim(0,6) # Lower Limit, Upper Limit
plt.ylim(0,12) # Lower Limit, Upper Limit
plt.show() 

# Exporting a plot
plt.plot(x,y)
plt.savefig('example.png')


