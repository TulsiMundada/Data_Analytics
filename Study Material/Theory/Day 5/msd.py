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
