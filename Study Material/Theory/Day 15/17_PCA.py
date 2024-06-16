import numpy as np 
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import time

# Students' performance in Maths
student_data= pd.read_csv("student-mat.csv")

'''
# Attributes
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2 gender - student's gender (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)
'''

print(student_data.describe())

col_str = student_data.columns[student_data.dtypes == object]
print(col_str)

# convert each category value into a new column and assign a 1 or 0 (True/False) value to the column. This has the benefit of not weighting a value improperly. Simplest method is using pandas' .get_dummies() method
#drop_first = True reduces extra column creation (e.g. coin toss, is_head and is_tail: both are not needed)
student_data = pd.get_dummies(student_data, columns = col_str, drop_first = True)
print(student_data.info())

print(student_data[["G1","G2","G3"]].corr())
# Since, G1,G2,G3 have very high correlation, we can drop G1,G2

student_data.drop(axis = 1,labels= ["G1","G2"])

# Drop the G3 column, because we want to predict it now
label = student_data["G3"].values
predictors = student_data.drop(axis = 1,labels= ["G3"]).values
print(student_data.shape)

#Using Linear Regression to predict grades
lr = linear_model.LinearRegression()

# cross_val_score: Used during the testing and validation phase of your machine learning model development
# Trains and tests a model over multiple folds of your dataset. This cross validation method gives you a better understanding of model performance over the whole dataset instead of just a single train/test split.
'''
The number of folds is defined, by default this is 5
The dataset is split up according to these folds, where each fold has a unique set of testing data
A model is trained and tested for each fold
Each fold returns a metric for it's test data
The mean and standard deviation of these metrics can then be calculated to provide a single metric for the process
'''

# Returns an array of scores of the estimator for each run of the cross validation
lr_score= cross_val_score(lr, predictors, label, cv=5) # Five runs, 5 means
print("LR Model Cross Validation score : " + str(lr_score)) 

# Average of all those means
print("LR Model Cross Validation Mean score : " + str(lr_score.mean()))

#Using PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=len(student_data.columns)-1)
pca.fit(predictors)
variance_ratio = pca.explained_variance_ratio_
print(pca.explained_variance_.shape)

# Now plot 
import matplotlib.pyplot as plt

# Find cumulative variance, adding one independent variable at a time
variance_ratio_cum_sum=np.cumsum(variance_ratio)
print(variance_ratio_cum_sum)

# This cumulative explained variance graph helps us to choose the number of desired principal components. If we look at the above print statement's output, we will realize that 90% variation in the data is explaining by the first 6 principal components. Hence, we annotate 6 on the graph.

plt.plot(variance_ratio_cum_sum)
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')

# Annotate 90% variance explained by the first 6 variables only
plt.annotate('6',xy=(6,.90))
plt.show()

# individual explained variance, instead of cumulative variance
# We see that the first variable causes 60% variance, the second 22%, and so on ...
plt.figure(figsize=(10, 5))

plt.bar(range(41),pca.explained_variance_, alpha=0.5,label='individual explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()

# PCA transforms a set of correlated variables into a set of linearly uncorrelated variables called principal components, we can check the correlarion with a heat map of correlation matrix

# correlation between the variables of the original data
# we see high correlation, which means duplication - we can eliminate many variables
import seaborn as sns
correlation = pd.DataFrame(predictors).corr()
sns.heatmap(correlation, vmax=1, square=True,cmap='Greens')
plt.title('Correlation between different features')
plt.show()

# Looking at the above plot we are taking 6 variables
pca = PCA(n_components=6)
pca.fit(predictors)
Transformed_vector =pca.fit_transform(predictors)
print(Transformed_vector)

# correlation between the 6 variables after transforming the data with PCA is 0
import seaborn as sns
correlation = pd.DataFrame(Transformed_vector).corr()
sns.heatmap(correlation, vmax=1, square=True,cmap='viridis')
plt.title('Correlation between different features')
plt.show()

# Check the performance with 6 variables
lr_pca = linear_model.LinearRegression()
lr_pca_score = cross_val_score(lr_pca, Transformed_vector, label, cv=5)
print("PCA Model Cross Validation score : " + str(lr_pca_score))
print("PCA Model Cross Validation Mean score : " + str(lr_pca_score.mean()))
# We see values similar to the earlier case when we had 40 independent variables
# This means that PCA has indeed reduced 40 variables to 6 without causing any negative impact
