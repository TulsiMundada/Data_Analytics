'''
Note: We need to do:
pip install empiricaldist 
pip install statadict
before running this example
'''

import empiricaldist
from statadict import parse_stata_dict

# The General Social Survey (GSS). The GSS surveys a representative sample of adult residents of the U.S. and asks questions about demographics, personal history, and beliefs about social and political issues. It is widely used by politicians, policy makers, and researchers.
dict_file = 'GSS.dct'
data_file = 'GSS.dat.gz'

from statadict import parse_stata_dict
stata_dict = parse_stata_dict(dict_file)

import gzip
fp = gzip.open(data_file)

# Convert the file into a Pandas DataFrame
import pandas as pd
gss = pd.read_fwf(fp, 
                  names=stata_dict.names, 
                  colspecs=stata_dict.colspecs)
print(gss.shape)
print(gss.head())

# Column explanation: https://gssdataexplorer.norc.org/variables/vfilter

# Distribution of education
print(gss['EDUC'].value_counts().sort_index())

# The values 98 and 99 are special codes for "Don't know" and "No answer". We'll use replace to replace these codes with NaN.

import numpy as np
educ = gss['EDUC'].replace([98, 99], np.nan)

# Visualize it
import matplotlib.pyplot as plt

educ.hist(grid=False)
plt.xlabel('Years of education')
plt.ylabel('Number of respondents')
plt.title('Histogram of education level');
plt.show()

# Looks like the peak is near 12 years of education. But a histogram is not the best way to visualize this distribution because it obscures some important details. An alternative is to use a Pmf.
# normalize=False indicates that we don't want to normalize this PMF - Explained later below
from empiricaldist import Pmf
pmf_educ = Pmf.from_seq(educ, normalize=False)
print(type(pmf_educ))
print(pmf_educ.head())


# In this dataset, there are 165 respondents who report that they have had no formal education, and 47 who have only one year. Here the last few rows.
print(pmf_educ.tail())
# There are 1439 respondents who report that they have 20 or more years of formal education, which probably means they attended college and graduate school.

# Get the count for 20 years of education separately
print(pmf_educ[20])

# Usually when we make a PMF, we want to know the fraction of respondents with each value, rather than the counts. We can do that by setting normalize=True; then we get a normalized PMF, that is, a PMF where the values in the second column add up to 1.
pmf_educ_norm = Pmf.from_seq(educ, normalize=True)
print(pmf_educ_norm.head())
print(pmf_educ_norm[12]) # Sample for 12 years of experience

# Pmf provides a bar method that plots the values and their probabilities as a bar chart.
pmf_educ_norm.bar(label='EDUC')

plt.xlabel('Years of education')
plt.xticks(range(0, 21, 4))
plt.ylabel('PMF')
plt.title('Distribution of years of education')
plt.legend();
plt.show()

# Lab Exercise: Let's look at the YEAR column in the DataFrame, which represents the year each respondent was interviewed.

# Make an unnormalized Pmf for YEAR and display the result. How many respondents were interviewed in 2018?

# Now CDF

from empiricaldist import Cdf

# Age 98 and 99 mean do not know and do not answer - so replace them
educ = gss['EDUC'].replace([98, 99], np.nan)

cdf_educ = Cdf.from_seq(educ)

cdf_educ.plot()

plt.xlabel('Years of Education (years)')
plt.ylabel('CDF')
plt.title('Distribution of education');
plt.show()
# The x-axis is the education levels, from 1 to 20. The y-axis is the cumulative probabilities, from 0 to 1.

# Now CDF for age

from empiricaldist import Cdf

# Age 98 and 99 mean do not know and do not answer - so replace them
age = gss['AGE'].replace([98, 99], np.nan)
print ("*****************")
print(age)

cdf_age = Cdf.from_seq(age)

cdf_age.plot()

plt.xlabel('Age (years)')
plt.ylabel('CDF')
plt.title('Distribution of age');
plt.show()
# The x-axis is the ages, from 18 to 89. The y-axis is the cumulative probabilities, from 0 to 1.

# We can also obtain the cumulative probability up to a certain point, e.g. age 51:
q = 51
p = cdf_age(q)
print(p)
# about 63% of the respondents are 51 years old or younger

# Inversly, find the age at a certain value of cumulative probability:
p1 = 0.25
q1 = cdf_age.inverse(p1)
print(q1)
# 25% of the respondents are age 31 or less. Another way to say the same thing is "age 31 is the 25th percentile of this distribution".

# We can now use 75th percentile to find IQR
#  It measures the spread of the distribution, so it is similar to standard deviation or variance.
p3 = 0.75
q3 = cdf_age.inverse(p3)
print(q3)
print(q3-q1)

# Annotate Q1 and Q3 on the plot to see IQR and outliers
print(f"Q1: {q1}, Q3: {q3}")

# Create the CDF using empiricaldist
cdf_age = empiricaldist.Cdf.from_seq(age)

# Extract CDF values and data points
cdf_values = cdf_age.values
data_points = cdf_age.index

plt.plot(data_points, cdf_values)

# Add Q1 and Q3 lines with annotations
plt.axvline(x=q1, color='red', linestyle='--', label='Q1')
plt.axvline(x=q3, color='orange', linestyle='--', label='Q3')

plt.xlabel('Age (years)')
plt.ylabel('CDF')
plt.title('Distribution of age with Q1 and Q3 marked')
plt.legend()
plt.show()


# Lab exercise: Exercise: Using cdf_age, compute the fraction of the respondents in the GSS dataset that are older than 65.

# Lab exercise: Exercise: The distribution of income in almost every country is long-tailed, which means there are a small number of people with very high incomes. In the GSS dataset, the column REALINC represents total household income, converted to 1986 dollars. We can get a sense of the shape of this distribution by plotting the CDF.

#Select REALINC from the gss dataset, make a Cdf called cdf_income, and plot it. Remember to label the axes.

# Now let us compare PMF and CMF

# Create series for male and female respondents
male = (gss['GENDER'] == 1)
female = (gss['GENDER'] == 2)

# Select ages
male_age = age[male]
female_age = age[female]

# Plot PMF for each
pmf_male_age = Pmf.from_seq(male_age)
pmf_male_age.plot(label='Male')

pmf_female_age = Pmf.from_seq(female_age)
pmf_female_age.plot(label='Female')

plt.xlabel('Age (years)') 
plt.ylabel('PMF')
plt.title('Distribution of age by GENDER')
plt.legend();
plt.show()

# Now CDF for same data_file
cdf_male_age = Cdf.from_seq(male_age)
cdf_male_age.plot(label='Male')

cdf_female_age = Cdf.from_seq(female_age)
cdf_female_age.plot(label='Female')

plt.xlabel('Age (years)') 
plt.ylabel('CDF')
plt.title('Distribution of age by GENDER')
plt.legend();
plt.show()

# Observations:
# In general, CDFs are smoother than PMFs. Because they smooth out randomness, we can often get a better view of real differences between distributions. In this case, the lines are close together until age 40; after that, the CDF is higher for men than women. So what does that mean?

# One way to interpret the difference is that the fraction of men below a given age is generally more than the fraction of women below the same age. For example, about 79% of men are 60 or less, compared to 76% of women.

print(cdf_male_age(60), cdf_female_age(60))

# Comparing male and female at the 50th percentile
print(cdf_male_age.inverse(0.5), cdf_female_age.inverse(0.5))

# Lab Exercise: What fraction of men are over 80? What fraction of women?

# Now income analysis
#  The variable REALINC represents household income in 1986 dollars.
pre95 = (gss['YEAR'] < 1995)
post95 = (gss['YEAR'] >= 1995)

income = gss['REALINC'].replace(0, np.nan)

Pmf.from_seq(income[pre95]).plot(label='Before 1995')
Pmf.from_seq(income[post95]).plot(label='After 1995')

# Plot PMFs
plt.xlabel('Income (1986 USD)')
plt.ylabel('PMF')
plt.title('Distribution of income')
plt.legend();
plt.show()

# Again the graph is very noisy: exhibits a significant amount of random or unstructured variability or fluctuations

# And now CDF
Cdf.from_seq(income[pre95]).plot(label='Before 1995')
Cdf.from_seq(income[post95]).plot(label='After 1995')

plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.title('Distribution of income')
plt.legend();
plt.show()

# Below $30,000 the CDFs are almost identical; above that, we can see that the post-1995 distribution is shifted to the right. In other words, the fraction of people with high incomes is about the same, but the income of high earners has increased.

# Lab Exercise: In the previous figure, the dollar amounts are big enough that the labels on the x axis are crowded. Improve the figure by expressing income in 1000s of dollars (and update the x label accordingly).


# Kernel Density Estimation or PDF
age_data = gss['AGE']

# Create a histogram to visualize the PDF
plt.hist(age_data, bins=20, density=True, alpha=0.6, color='b', label='PDF')
plt.xlabel('Age')
plt.ylabel('Probability Density')
plt.title('PDF of Age in GSS Dataset')
plt.legend()
plt.show()

# Corresponding PMF
pmf = age_data.value_counts(normalize=True).sort_index()

# Create a bar plot of the PMF
plt.figure(figsize=(10, 6))
plt.bar(pmf.index, pmf.values)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('PMF of Age in GSS Dataset')
plt.xticks(rotation=90)
plt.show()
