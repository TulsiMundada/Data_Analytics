import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

# Calculate the correlation coefficient
correlation_coefficient = df['reading score'].corr(df['writing score'])

print(f'Correlation Coefficient: {correlation_coefficient}')

# Plot a scatter plot to visualize the data
plt.scatter(df['reading score'], df['writing score'])
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title(f'Scatter Plot (Correlation: {correlation_coefficient:.2f})')

# Identify potential outliers (e.g., values with residuals greater than 2 times the standard deviation)
residuals = df['writing score'] - df['reading score']
print(residuals)

std_deviation = residuals.std()
outliers = df[abs(residuals) > 2 * std_deviation]

# Highlight potential outliers on the scatter plot
plt.scatter(outliers['reading score'], outliers['writing score'], color='red', label='Outliers')
plt.legend()

plt.show()
