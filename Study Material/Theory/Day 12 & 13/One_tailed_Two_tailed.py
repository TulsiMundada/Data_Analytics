import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Significance level (alpha)
alpha = 0.05

# Calculate critical values for two-tailed test
critical_value_two_tailed = stats.norm.ppf(1 - alpha / 2)

# Calculate critical values for one-tailed test
critical_value_one_tailed = stats.norm.ppf(1 - alpha)

# Generate x-values for the standard normal distribution
x_values = np.linspace(-3, 3, 1000)

# Generate y-values (probability density) for the standard normal distribution
y_values = stats.norm.pdf(x_values)

# Plot rejection region for two-tailed test
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, color='black', label='Standard Normal Distribution')
plt.fill_between(x_values, 0, y_values, where=(x_values <= -critical_value_two_tailed) | (x_values >= critical_value_two_tailed), color='red', alpha=0.3, label='Rejection Region (Two-Tailed)')
plt.xlabel('Z-values')
plt.ylabel('Probability Density')
plt.title('Rejection Region for Two-Tailed Test (α = 0.05)')
plt.legend()
plt.grid(True)
plt.show()

# Plot rejection region for one-tailed test
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, color='black', label='Standard Normal Distribution')
plt.fill_between(x_values, 0, y_values, where=x_values >= critical_value_one_tailed, color='red', alpha=0.3, label='Rejection Region (One-Tailed)')
plt.xlabel('Z-values')
plt.ylabel('Probability Density')
plt.title('Rejection Region for One-Tailed Test (α = 0.05)')
plt.legend()
plt.grid(True)
plt.show()
