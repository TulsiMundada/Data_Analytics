# Step 1 Load Data
import pandas as pd
dataset = pd.read_csv('salary.csv')

# For X (independent variable), take all the columns from the file, except salary
X = dataset.iloc[:, :-1].values

# For Y (dependent variable), take the second column, which is salary
y = dataset.iloc[:,1].values

# Step 2: Split data into training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Step 3: Fit Simple Linear Regression to Training Data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 4: Make Prediction
y_pred = regressor.predict(X_test)
print (y_pred)

# Step 5 - Visualize training set results
import matplotlib.pyplot as plt
# plot the actual data points of training set
plt.scatter(X_train, y_train, color = 'red')
# plot the regression line
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Step 6 - Visualize test set results
import matplotlib.pyplot as plt
# plot the actual data points of test set
plt.scatter(X_test, y_test, color = 'red')
# plot the regression line (same as above)
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Step 7 - Make new prediction
new_salary_pred = regressor.predict([[15]])
print('The predicted salary of a person with 15 years experience is ',new_salary_pred)

# Step 8 - Intercept and Coefficient
# Intercept: Salary for "0" years of experience (What will be y-axis value if x-axis value is 0?) and coefficient: For each additional year, how much additional salary will we offer?
print("Intercept ... Fresher Salary: ", regressor.intercept_)
print("Coefficient ... Additional Salary for Each Additional Year's Experience: ", regressor.coef_)

# Evaluate results
from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np

MAE = mean_absolute_error(y_test,y_pred)
MSE = mean_squared_error(y_test,y_pred)
RMSE = np.sqrt(MSE)

# on average, the predictions were off by around 3426.43 units from the actual values
print(f"MAE = {MAE}") 

# Squares the absolute differences between the predicted values and the actual values, 
#  and then averages them - Squaring the errors gives more weight to larger errors
#  An MSE of 21026037.33 suggests that there might be some outliers or 
#   significant errors in our predictions, as squaring amplifies their 
#  contribution to the MSE value
print(f"MSE = {MSE}")

# Now take the square root of the MSE - It has the same units as the original data, 
#   making it easier to interpret in the context of our specific problem
# An RMSE of 4585.42 implies that the average prediction error was around 4585.42 units
print(f"RMSE = {RMSE}")

'''
A lower MAE, MSE, and RMSE generally indicate better model performance, meaning the 
predictions are closer to the actual values
The high MSE value compared to MAE suggests that there might be a few instances 
where the model's predictions were significantly far off from the actual values
'''
