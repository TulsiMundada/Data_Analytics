# -*- coding: utf-8 -*-

from scipy.optimize import linprog
import numpy as np
#https://towardsdatascience.com/linear-programming-with-python-db7742b91cb
#Maximize Total Profit = 50 Jordanelle + 65 Deercrest 
#       3.5 Jordanelle + 4 Deercrest <= 84
#		1 Jordanelle + 1.5 Deercrest <= 21
#		2Jordanelle - Deercrest  <= 0
#		0*Jordanelle - Deercrest <= 0
#		-Jordanelle  + 0*Deecrest <= 0


# Set the inequality constraints matrix
# Note: the inequality constraints must be in the form of <=
A = np.array([[3.5, 4], [1, 1.5], [2, -1],[-1, 0],[0, -1]])

# Set the inequality constraints vector
b = np.array([84, 21, 0, 0, 0])

# Set the coefficients of the linear objective function vector
# Note: when maximizing, change the signs of the c vector coefficient
c = np.array([-50, -65])

# Solve linear programming problem
res = linprog(c, A_ub=A, b_ub=b, method="simplex")

# Print results
print('Optimal value:', round(res.fun*-1, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)
