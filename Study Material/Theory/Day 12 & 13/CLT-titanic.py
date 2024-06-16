import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import math 

df=pd.read_csv("titanic-tested.csv")
print(df)

plt.figure(figsize=(21,30))

# Check various column distributions
plt.subplot(2,3,1)
df["Age"].plot(kind="hist")
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')

plt.subplot(2,3,2)
df["Pclass"].plot(kind="hist")
plt.xlabel('Passenger Class')
plt.ylabel('Class')
plt.title('Passenger Class Distribution')

plt.subplot(2,3,3)
df["Survived"].plot(kind="hist")
plt.xlabel('Survived')
plt.ylabel('Count')
plt.title('Survied Passengers Distribution')

plt.subplot(2,3,4)
df["PassengerId"].plot(kind="hist",bins=50)
plt.xlabel('Passenger ID')
plt.ylabel('Count')
plt.title('Passenger ID Distribution')

plt.subplot(2,3,5)
df["Fare"].plot(kind="hist")
plt.xlabel('Fare')
plt.ylabel('Count')
plt.title('Fare Distribution')

plt.subplot(2,3,6)
df["SibSp"].plot(kind="hist")
plt.xlabel('Siblings and Spouse Count')
plt.ylabel('Count')
plt.title('Siblings and Spouse Distribution')

plt.savefig("output_before.png")
plt.show()

# Calculate and print sample means
# sample() function returns randomly selected rows
# So, take 10 samples of 50 each and calculate means
# replace=False will allow repeat selection of the same row in multiple samples
means_list=[df['Age'].sample(50, replace=False).mean() for i in range(10)]
print(means_list)

# Plot histogram of means_list
plt.hist(means_list, bins=10, edgecolor='black', alpha=0.7)

plt.xlabel('Mean Age')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means')
plt.savefig('output_plot_original.png')
plt.show()

# Keep increasing the sample size and repeatation count to see the shift towards normal distribution

## Repeat for one more column Pclass
means_list=[df['Pclass'].sample(300, replace=False).mean() for i in range(100)]
print(means_list)

# Plot histogram of means_list
plt.hist(means_list, bins=10, edgecolor='black', alpha=0.7)

plt.xlabel('Mean Passenger Class')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means')
plt.show()

## Now let us keep changing the sample composition to see the effect
# For testing, we will again take the Age column

# First define a list of data points in each sample and how many such samples
dist_list=[(400,10),(50,50),(400,100),(400,200),(400,300),(400,500)]  #(no. of datapoints,no. of samples)

import statistics

sample_mean=[]
plt.figure(figsize=(20,15))
for i,j in enumerate(dist_list):
    for z in range(j[1]):
        x=df['Age'].sample(j[0], replace=False).mean()
        sample_mean.append(x)
    mn=np.mean(sample_mean)
    sd=statistics.stdev(sample_mean,mn)
    plt.subplot(2,3,i+1)
    sns.histplot(sample_mean)
    se=np.std(sample_mean, ddof=1) / np.sqrt(np.size(sample_mean))
    plt.title(f"DtPts={j[0]}, TSams={j[1]}, Mean={mn:.2f},STD={sd:.2f}, SE={se:.2f}")

# Save the output to a file also
plt.savefig('output_plot.png')

plt.show()
