# Generate a dummy dataset and run Naive Bayes

from sklearn.datasets import make_classification

'''
n_features: This parameter specifies the number of features (attributes) in the dataset. In your case, you've set it to 6, so the dataset will have 6 features.

n_classes: This parameter determines the number of classes or categories in the target variable. You've set it to 3, so the dataset will have 3 distinct classes.

n_samples: This parameter sets the total number of samples (data points) in the dataset. You've specified 800, so the dataset will contain 800 data points.

n_informative: This parameter controls the number of informative features. Informative features are those that contribute to the separation of classes. You've set it to 2, indicating that 2 out of the 6 features are informative, while the others may not be relevant for classification.

random_state: This parameter sets the random seed for generating the dataset. Using a fixed random seed ensures reproducibility, meaning that if you run the code with the same random seed, you will get the same dataset each time.

n_clusters_per_class: This parameter specifies the number of clusters per class. In your code, it's set to 1, which means that each class will have one cluster of data points.
'''

X, y = make_classification(
    n_features=6,
    n_classes=3,
    n_samples=800,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

'''
After running this code, you will have two variables:

X: This variable contains the feature matrix, with 800 rows and 6 columns, representing the 800 data points and their 6 features.

y: This variable contains the target vector, with 800 labels corresponding to the classes assigned to each data point in X. Since you specified n_classes=3, y will contain values from 0 to 2, representing the three classes.
'''

print(X)
print(y)

# Print the first two columns of x, which are the two informative columns out of 6
print (X[:, 0])
print (X[:, 1])

import matplotlib.pyplot as plt

'''
The scatter() function takes three arguments: X[:, 0] and X[:, 1] are the first and second columns of the X array, respectively, and c=y assigns a color to each point based on the corresponding value in the y array.
X[:, 0] and X[:, 1] specify that the x-coordinate of each data point is taken from the first column of X, and the y-coordinate is taken from the second column of X. This assumes that your dataset X has at least two features.
c=y assigns colors to the data points based on the values in the y array. Each unique value in y corresponds to a different class, and the c parameter ensures that data points belonging to the same class are plotted with the same color.
marker="*" specifies that you want to use asterisks as markers for the data points. You can choose different marker styles by changing this parameter.
'''

plt.scatter(X[:, 0], X[:, 1], c=y, marker="*");
plt.show()

from sklearn.model_selection import train_test_split

'''
X is the feature matrix, which contains your data points and their attributes.
y is the target vector, which contains the class labels corresponding to each data point in X.
test_size=0.33 specifies that you want to allocate 33% (one-third) of your data to the testing set. The remaining 67% will be used for training. You can adjust this ratio by changing the test_size parameter.
random_state=125 sets a random seed for the split operation. This ensures reproducibility, meaning that if you run the code with the same random seed (125), you will get the same split every time. The random seed helps control the randomness of the data split.
'''

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)

from sklearn.naive_bayes import GaussianNB

# Build a Gaussian Classifier
model = GaussianNB()

# Model training
'''
model.fit(X_train, y_train): This line trains the Gaussian Naive Bayes model on the training data. Here's what happens:

X_train contains the feature variables (attributes) of the training set.
y_train contains the corresponding target variables (labels) of the training set.
The fit method of the model object is called with X_train and y_train as arguments, which means the classifier learns the underlying probabilistic model from the training data.
'''
model.fit(X_train, y_train)

# Predict Output
'''
X_test[6] selects the seventh data point from the testing set (Python uses 0-based indexing).
model.predict([X_test[6]]) passes this selected data point to the predict method of the model object to make a prediction.
The predicted class label for the selected data point is stored in the predicted variable.
'''
predicted = model.predict([X_test[6]])

print("Actual Value:", y_test[6])
print("Predicted Value:", predicted[0])

# y_pred = model.predict(X_test): This line uses your trained Gaussian Naive Bayes model (model) to make predictions on the testing data (X_test). The predicted class labels are stored in the y_pred variable.
y_pred = model.predict(X_test)

# Now check model accuracy
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
)

'''
accuray = accuracy_score(y_pred, y_test): This line calculates the accuracy score for the model's predictions. Here's what it does:

y_pred contains the predicted class labels.
y_test contains the true class labels (ground truth) from the testing set.
The accuracy_score function compares y_pred and y_test and calculates the ratio of correctly predicted instances to the total number of instances in the testing set. This ratio represents the accuracy of your classifier on the test data.
'''
accuray = accuracy_score(y_pred, y_test)

'''
f1 = f1_score(y_pred, y_test, average="weighted"): This line calculates the F1 score for the model's predictions. Here's what it does:

y_pred contains the predicted class labels.
y_test contains the true class labels (ground truth) from the testing set.
The f1_score function computes the F1 score, which is a measure of a model's accuracy that considers both precision and recall. The "weighted" average indicates that it calculates the weighted average of F1 scores across different classes, taking into account class imbalance.
'''
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)

