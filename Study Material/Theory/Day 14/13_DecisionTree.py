import numpy as np
import pandas as pd
from sklearn import tree

input_file = "PastHires.csv"
df = pd.read_csv(input_file, header = 0)

print(df.head())

# scikit-learn needs everything to be numerical for decision trees to work, so we need to map our data to numerical form using the map function

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print(df.head())

# Separate features from the target column that we are building a tree for
features = list(df.columns[:6])
print(features)

# Construct the decision tree
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)
SPLAYED
# pip install pydotplus
# pip install graphviz
# Possibly add path of graphviz\bin directory to Windows PATH variable
# For Linux, on the shell prompt, also do sudo apt-get install graphviz
# OR the following ...
# conda install pydotplus
# conda install graphviz
from IPython.display import Image  
from six import StringIO  
import pydotplus

# The export_graphviz function converts the decision tree classifier into a dot file, and pydotplus converts this dot file to png or displayable form on Jupyter

dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())
graph.write_png('job.png')

# Gini Index or Gini impurity measures the degree or probability of a particular variable being wrongly classified when it is randomly chosen.
# To be discussed