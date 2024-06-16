import pandas as pd 
import numpy as np 
import datetime 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('MS_Dhoni_ODI_record.csv')

# Basic checks
print(df.head())
print(df.tail())

# Data cleaning - Opposition name says 'v Aus' etc, we can remove 'v '
df['opposition'] = df['opposition'].apply(lambda x: x[2:])

# Add a 'feature' - 'year' column using the match date column
# First convert date column into datetime format
df['date'] = pd.to_datetime(df['date'], dayfirst=True) 
df['year'] = df['date'].dt.year.astype(int)
#print(df.head())

# Create a column to distinguish between out and not out

# The apply method in Pandas allows you to apply a function to each element in a DataFrame or Series. In this case, the function being applied is str, which is the built-in Python function for converting values into strings. By applying str to each element in the 'score' column, we are converting the numerical or other data types in that column into string data types.
df['score'] = df['score'].apply(str) 
df['not_out'] = np.where(df['score'].str.endswith('*'), 1, 0)

# dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)

# dropping those innings where Dhoni did not bat and storing in a new DataFrame 
# Take all the columns, starting with runs_scored
df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != 'TDNB')), 'runs_scored':]
#print(df_new.head())

# fixing the data types of numerical columns 
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
df_new['balls_faced'] = df_new['balls_faced'].astype(int) 
df_new['strike_rate'] = df_new['strike_rate'].astype(float) 
df_new['fours'] = df_new['fours'].astype(int) 
df_new['sixes'] = df_new['sixes'].astype(int)

# Career stats
first_match_date = df['date'].dt.date.min().strftime('%B %d, %Y') # first match
print('First match:', first_match_date)
last_match_date = df['date'].dt.date.max().strftime('%B %d, %Y') # last match
print('Last match:', last_match_date)
number_of_matches = df.shape[0] # number of mathces played in career
print('Number of matches played:', number_of_matches)
number_of_inns = df_new.shape[0] # number of innings
print('Number of innings played:', number_of_inns)
not_outs = df_new['not_out'].sum() # number of not outs in career
print('Not outs:', not_outs)
runs_scored = df_new['runs_scored'].sum() # runs scored in career
print('Runs scored in career:', runs_scored)
balls_faced = df_new['balls_faced'].sum() # balls faced in career
print('Balls faced in career:', balls_faced)
career_sr = (runs_scored / balls_faced)*100 # career strike rate
print('Career strike rate: {:.2f}'.format(career_sr))
career_avg = (runs_scored / (number_of_inns - not_outs)) # career average
print('Career average: {:.2f}'.format(career_avg))
#highest_score_date = df_new.loc[df_new.runs_scored == df_new.runs_scored.max(), 'date'].values[0]
#highest_score = df.loc[df.date == highest_score_date, 'score'].values[0] # highest score
highest_score = df_new['runs_scored'].max()
not_out_for_highest = (
    df_new[df_new['runs_scored'] == highest_score]['not_out']
    .replace([1, 0], ["*", ""])  # Replace 1 with *, 0 with null
    .iloc[0]
)
print('Highest score in career:', highest_score, not_out_for_highest)
hundreds = (df_new['runs_scored'] >= 100).sum()
# hundreds = df_new.loc[df_new['runs_scored'] >= 100].shape[0] # number of 100s
print('Number of 100s:', hundreds)
fifties = ((df_new['runs_scored'] >= 50) & (df_new['runs_scored'] < 100)).sum()
# fifties = df_new.loc[(df_new['runs_scored']>=50)&(df_new['runs_scored']<100)].shape[0] #number of 50s
print('Number of 50s:', fifties)
fours = df_new['fours'].sum() # number of fours in career
print('Number of 4s:', fours)
sixes = df_new['sixes'].sum() # number of sixes in career
print('Number of 6s:', sixes)

# number of matches played against different oppositions
# Count the occurrences of each unique value in the 'opposition' column
# opposition_counts will be a series with a labelled index as opposition
opposition_counts = df['opposition'].value_counts()
print(opposition_counts)
# Plot the counts as a bar plot
opposition_counts.plot(kind='bar', title='Number of matches against different oppositions', figsize=(8, 5))
plt.show()

# Runs scored against each team
# Group the DataFrame by 'opposition' column
grouped_by_opposition = df_new.groupby('opposition')
# Sum the 'runs_scored' column for each group
sum_of_runs_scored = grouped_by_opposition['runs_scored'].sum()
print(sum_of_runs_scored)
# sum_of_runs_scored is a series with a labelled index, which is opposition
# Convert it into a DataFrame and remove the index
runs_scored_by_opposition = pd.DataFrame(sum_of_runs_scored).reset_index()
runs_scored_by_opposition.plot(x='opposition', kind='bar', title='Runs scored against different oppositions', figsize=(8, 5))
plt.xlabel(None);
plt.show()

# Does not look good ... Let us sort it ...
sorted = runs_scored_by_opposition.sort_values(by='runs_scored', ascending=False)
# print(sorted)
sorted.plot(x='opposition', kind='bar', title='Runs scored against different oppositions', figsize=(8, 5))
plt.xlabel(None);
plt.show()

# Boxplot of runs against various oppositions

sns.boxplot(x='opposition',y='runs_scored',data=df_new)
plt.show()

# Looks crowded - Let us retain only major countries
# List of oppositions to filter
opposition_list = ['England', 'Australia', 'West Indies', 'South Africa', 
                   'New Zealand', 'Pakistan', 'Sri Lanka', 'Bangladesh']

# Filter rows where 'opposition' is in the list
df_filtered = df_new[df_new['opposition'].isin(opposition_list)]

# Sort the filtered DataFrame in descending order of 'runs_scored'
df_filtered = df_filtered.sort_values(by='runs_scored', ascending=False)

# Display the filtered DataFrame
print(df_filtered)

# Rewdraw boxplot but on filtered opposition list
sns.boxplot(x='opposition',y='runs_scored',data=df_filtered)
plt.xticks(rotation=45)
plt.show()

# Violin plot
plt.figure(figsize=(12,6))
sns.violinplot(x='opposition',y='runs_scored',data=df_filtered)
plt.show()

# distplot with and without kde 
sns.displot(data=df_filtered,x='runs_scored',kde=False)
plt.show()
# We see that there is a right/postive skew, so there is a long tail to the right

sns.displot(data=df_filtered,x='runs_scored',kde=True)
plt.show()

# histogram with bins
sns.set(style='darkgrid')
sns.histplot(data=df_new,x='runs_scored',bins=15)
plt.show()

# KDE plot
plt.figure(figsize=(12,8))
sns.kdeplot(data=df_new,x='runs_scored')
plt.show()

# KDE plot with cumulative probability
plt.figure(figsize=(12, 8))
sns.kdeplot(data=df_new, x='runs_scored', cumulative=True)
plt.show()

# jointplot
sns.jointplot(x='balls_faced',y='runs_scored',data=df_new, kind='scatter')
plt.show()

# Heat map
# Calculate the correlation matrix
correlation_matrix = df_new[['balls_faced', 'runs_scored']].corr()

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data=correlation_matrix, annot=True, cmap='viridis', 
            square=True, fmt=".2f")

# Add title
plt.title('Correlation Heatmap between Balls Faced and Runs Scored')

# Show plot
plt.show()


# Calculate strike-rate per opposition and show as a heat map
# Grouping by 'opposition'
grouped_by_opposition = df_filtered.groupby('opposition')

# Aggregating 'balls_faced' and 'runs_scored' using sum
agg_sum = grouped_by_opposition.agg({'balls_faced': 'sum', 'runs_scored': 'sum'})

# Assigning the result to df_strike_rate
df_strike_rate = agg_sum

# Calculate strike rate
df_strike_rate['strike_rate'] = (df_strike_rate['runs_scored'] / df_strike_rate['balls_faced']) * 100

# Resetting index to make 'opposition' a regular column
# df_strike_rate.reset_index(inplace=True)
# NO - We do want opposition as index for heatmap to be possible
# Display the resulting DataFrame
print(df_strike_rate)

# Bad graph - strike rate scale is different from runs scored and balls faced
sns.heatmap(df_strike_rate,linewidth=0.5,annot=True,fmt='.0f',cmap='viridis')
plt.show()

# Good graph - only retain strike rate column
df_strike_rate = df_strike_rate[['strike_rate']] 
sns.heatmap(df_strike_rate,linewidth=0.5,annot=True,fmt='.0f',cmap='viridis')
plt.show()


# Strike rate bar graph with career srike rate as a line on the bar graph
# Create the bar plot

# Resetting index to make 'opposition' a regular column
df_strike_rate.reset_index(inplace=True)

plt.figure(figsize=(10, 8))
plt.bar(df_strike_rate['opposition'], df_strike_rate['strike_rate'], color='skyblue')

# Plot the aggregate strike rate as a red line
aggregate_strike_rate = df_strike_rate['strike_rate'].mean()
plt.axhline(y=aggregate_strike_rate, color='red', linestyle='--', label='Career Strike Rate')

# Set labels and title
plt.xlabel('Country')
plt.ylabel('Strike Rate')
plt.title('Strike Rate by Country')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()


# Proportion of runs in boundaries (4s and 6s both)
# Copy only the 'runs_scored', 'fours', and 'sixes' columns into a new DataFrame
df_boundaries = df_filtered[['opposition', 'runs_scored', 'fours', 'sixes']].copy()

# Add a new column 'runs_in_boundaries' to df_boundaries
df_boundaries['runs_in_boundaries'] = (df_boundaries['fours'] * 4) + (df_boundaries['sixes'] * 6)

# Display the updated DataFrame
print(df_boundaries)

# Selecting required columns
df_boundaries_selected = df_boundaries[['opposition', 'runs_scored', 'runs_in_boundaries']].copy()

# Grouping by 'opposition'
grouped_by_opposition = df_boundaries_selected.groupby('opposition')

# Aggregating using sum
df_boundaries_grouped = grouped_by_opposition.sum().reset_index()

# Display the new DataFrame
print(df_boundaries_grouped)

# Stacked bar plot
# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the stacked bar chart
plt.bar(df_boundaries_grouped['opposition'], df_boundaries_grouped['runs_scored'], label='Runs Scored')
plt.bar(df_boundaries_grouped['opposition'], df_boundaries_grouped['runs_in_boundaries'], 
        bottom=df_boundaries_grouped['runs_scored'], label='Runs in Boundaries')

# Add labels and title
plt.xlabel('Opposition')
plt.ylabel('Runs')
plt.title('Runs Scored and Runs in Boundaries by Opposition')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()

# Same thing - side by side bar plot
# Set the figure size
plt.figure(figsize=(10, 6))

# Define the width of each bar
bar_width = 0.35

# Set the x coordinates for the groups
index = np.arange(len(df_boundaries_grouped['opposition']))

# Plot the side-by-side bar chart
plt.bar(index, df_boundaries_grouped['runs_scored'], width=bar_width, label='Runs Scored')
plt.bar(index + bar_width, df_boundaries_grouped['runs_in_boundaries'], 
        width=bar_width, label='Runs in Boundaries')

# Add labels and title
plt.xlabel('Opposition')
plt.ylabel('Runs')
plt.title('Runs Scored and Runs in Boundaries by Opposition')
plt.xticks(index + bar_width / 2, df_boundaries_grouped['opposition'], rotation=45)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()


# Now a pie chart
# Add columns 'runs_in_fours' and 'runs_in_sixes' to df_boundaries
df_boundaries['runs_in_fours'] = df_boundaries['fours'] * 4
df_boundaries['runs_in_sixes'] = df_boundaries['sixes'] * 6
df_boundaries['runs_not_in_boundaries'] = df_boundaries['runs_scored'] - df_boundaries['runs_in_fours'] - df_boundaries['runs_in_sixes']

# Selecting required columns
df_boundaries_selected = df_boundaries[['opposition', 'runs_not_in_boundaries', 'runs_in_fours', 'runs_in_sixes']].copy()

# Grouping by 'opposition'
grouped_by_opposition = df_boundaries_selected.groupby('opposition')

# Aggregating using sum
df_boundaries_grouped = grouped_by_opposition.sum().reset_index()

import math

# Calculate the number of oppositions
num_oppositions = len(df_boundaries_grouped)

# Determine the number of rows and columns
# ceil() rounds up to the nearest integer, e.g. ceil(3.3) = 4
num_cols = math.ceil(math.sqrt(num_oppositions))
num_rows = math.ceil(num_oppositions / num_cols)

# Create subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))

# Flatten the axes array to iterate over it
axes = axes.flatten()

# Iterate over each opposition
for i, (index, row) in enumerate(df_boundaries_grouped.iterrows()):
    # Extract opposition and runs data
    opposition = row['opposition']
    runs_data = [row['runs_not_in_boundaries'], row['runs_in_fours'], row['runs_in_sixes']]
    
    # Create pie chart
    axes[i].pie(runs_data, labels=['Runs Not in Boundaries', 'Runs in Fours', 'Runs in Sixes'], autopct='%1.1f%%', startangle=90)
    axes[i].set_title(f'Runs Distribution against {opposition}')
    axes[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Remove any extra subplots
for j in range(num_oppositions, num_rows * num_cols):
    fig.delaxes(axes[j])

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

# Year-wise record
#df['year'].value_counts().sort_index().plot(kind='bar', title='Matches played by year', figsize=(8, 5))
# Count the occurrences of each unique value in the 'year' column
year_counts = df_new['year'].value_counts()
# Sort the counted values by index (year)
sorted_counts = year_counts.sort_index()
# Plot the sorted counts as a bar plot
sorted_counts.plot(kind='bar', title='Matches played by year', figsize=(8, 5))

plt.xticks(rotation=0)
plt.show()

# Runs scored by year
# Group the DataFrame by 'year'
# Group the DataFrame by 'year'
grouped_by_year = df_new.groupby('year')
#print(df.dtypes)
#print(grouped_by_year.dtypes)
# Save the DataFrame to a CSV file
#df.to_csv('grouped_by_year.csv', index=False)

# Convert the 'runs_scored' column to integer
#df['runs_scored'] = df['runs_scored'].astype(int)

# Calculate the sum of 'runs_scored' for each year
sum_of_runs_scored = grouped_by_year['runs_scored'].sum()

# Reset the index to make 'year' a regular column
df_grouped = sum_of_runs_scored.reset_index()
print(df_grouped)

# Plotting the bar plot
plt.figure(figsize=(10, 6))
x_values = df_grouped['year']
y_values = df_grouped['runs_scored']
plt.bar(x_values, y_values, color='skyblue', edgecolor='black')
plt.title('Bar Plot of Runs Scored by Year')
plt.xlabel('Year')
plt.ylabel('Runs Scored')
plt.grid(axis='y')
plt.show()



# As a line plot
plt.figure(figsize=(10, 6))
x_values = df_grouped['year']
y_values = df_grouped['runs_scored']
plt.plot(x_values, y_values, linestyle='-', color='b')
plt.title('Runs Scored Year-wise')
plt.xlabel('Year')
plt.ylabel('Runs Scored')
plt.grid(True)
plt.show()

# As a histogram to show frequency - not year-by-year performance
plt.figure(figsize=(10, 6))
data = df_grouped['runs_scored']
num_bins = 10
plt.hist(data, bins=num_bins, color='skyblue', edgecolor='black')
plt.title('Histogram of Runs Scored')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()


# Cumulative score progress
# Calculate the cumulative runs
df_new['cumulative_runs'] = df_new['runs_scored'].cumsum()

# Plot the cumulative runs as a line graph
plt.figure(figsize=(10, 6))
plt.plot(df_new.index, df_new['cumulative_runs'], linestyle='-')

# Mark each 1000th cumulative runs milestone with a red dot
# Iterate over a range of values from 0 up to the maximum value of the 
#   'cumulative_runs' column in the DataFrame df_new, with a step of 1000
for milestone in range(0, df_new['cumulative_runs'].max() + 1, 1000):
    # Find the index closest to the milestone
    # Subtract the milestone from each value in the 'cumulative_runs' column, 
    #   taking the absolute value, and then finding the index corresponding to 
    #   the minimum absolute difference using the idxmin() method    
    index = (df_new['cumulative_runs'] - milestone).abs().idxmin()
    # plot a red dot at that index and the milestone value using the 
    #   plt.plot() function ... r = red, 0 = circle ... also try r*
    # plt.plot(index, milestone, 'ro')
    plt.plot(index, milestone, 'r*', markersize=25)
    
# Add labels and title
plt.xlabel('Match Number')
plt.ylabel('Cumulative Runs')
plt.title('Cumulative Runs over Matches')

# Show plot
plt.tight_layout()
plt.show()


# Pair plots

# Only retain needed columns
df_pair_plot = df_filtered[['opposition', 'runs_scored', 'balls_faced', 'fours', 'sixes']]
print(df_pair_plot)

sns.pairplot(df_pair_plot,hue='opposition',palette='viridis')
plt.show()

# Interpretation: The diagonals show the distribution of a single variable
#  eg runs_scored, balls_faced, ...
#  The scatter plots on the upper and lower triangles show the relationship 
#   (or lack thereof) between two variables
#   For example, the left-most plot in the second row shows the scatter plot of 
#   runs_scored versus balls_faced
# We can also see correlation: runs_scored is highly correlated with  balls_faced
#   Runs_scored is also correlated positively to fours

# View histograms in diagonals
sns.pairplot(df_pair_plot,hue='opposition',palette='viridis',diag_kind='hist')
plt.show()