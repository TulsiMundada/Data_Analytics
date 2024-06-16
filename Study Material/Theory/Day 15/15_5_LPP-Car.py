import pulp

# Instantiate our problem class
model = pulp.LpProblem("Profit_maximising_problem", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')

# Objective function
model += 30000 * A + 45000 * B, "Profit"

# Constraints
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21
# Just for testing - What if we want to manufacture at least 5 cars per day?
# Add another constraint
# model += A >= 5

# Some more constraints - One of the two below
# model += A >= B
# model += A <= B

# Solve our problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print ("Production of Car A = {}".format(A.varValue))
print ("Production of Car B = {}".format(B.varValue))

# Print our objective function value
print (pulp.value(model.objective))