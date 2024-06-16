import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('vehicles.csv')
print(df.head(8))

print(df.info())

print(df['Favorite Transport'].unique())

print(df.value_counts('Favorite Transport'))

print(df.isnull().sum())

df['Income'] = df['Income'].fillna(0.0)
print(df.head(8))

print(df.isnull().sum())

label_encoder = LabelEncoder()
encoded_genders = label_encoder.fit_transform(df['Gender'])
print(encoded_genders)

df['Gender'] = encoded_genders
print(df.head(8))

print(df.dtypes)

X = df.drop(columns='Favorite Transport')
y = df['Favorite Transport']
print(X.head())

print(y.head())

model = DecisionTreeClassifier()

model.fit(X, y)

test_df = pd.DataFrame({
    'Age': [12, 30, 75],
    'Gender': [0, 0, 1],
    'Income': [0.0, 4000, 50000]
})
print(test_df)

model.predict(test_df)

"""### Export to DOT file"""

tree.export_graphviz(model, out_file='decision_tree_model.dot', filled=True, feature_names=['Age', 'Gender', 'Income'], class_names=sorted(y.unique()))

# To open the file, first convert to png and then open the png file
# To convert: dot decision_tree_model.dot -Tpng -o decision_tree_model.png

sns.countplot(x=df['Gender'], hue=df['Favorite Transport'])
plt.show()

sns.histplot(x=df['Income'], hue=df['Favorite Transport'])
plt.show()

"""### Evaluate Accuracy of the Model"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print('Train shape', X_train.shape)
print('Test shape', X_test.shape)
print('Source data shape', X.shape)
print('Test input data', X_test)
print('Test target data', y_test)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

model_score = accuracy_score(y_test, predictions)
print('Model score', model_score)