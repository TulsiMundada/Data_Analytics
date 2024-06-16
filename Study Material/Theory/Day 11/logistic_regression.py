import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("diabetes.csv")
print(df)

# Split the dataset into predictor variables X (all columns except "Outcome") and the target variable y ("Outcome").
X=df.drop("Outcome",axis=1)
y=df['Outcome']

print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LogisticRegression
# Creates an instance of a logistic regression classifier named classifier using the liblinear solver.
#Fits the model to the training data using classifier.fit.
# 'liblinear': This solver is suitable for small to medium-sized datasets. It uses a coordinate descent algorithm to optimize the logistic regression model. It's efficient for linear problems and can handle both L1 (Lasso) and L2 (Ridge) regularization penalties.
# Scikit-learn offers other solver options as well, and the choice of solver may depend on factors such as the dataset size, sparsity of data, and regularization preferences.
classifier=LogisticRegression(solver='liblinear')
classifier.fit(X_train,y_train)

y_test_prediction=classifier.predict(X_test)
print(y_test_prediction)

comparison=pd.DataFrame({'Actual':y_test,'Predicted':y_test_prediction})
print(comparison[0:10])

from sklearn.metrics import accuracy_score
# Calculates and prints the accuracy score, which measures the fraction of correctly predicted instances in the test set.
print(accuracy_score(y_test,y_test_prediction))

y_train_prediction=classifier.predict(X_train)
print(accuracy_score(y_train,y_train_prediction))

from sklearn.metrics import confusion_matrix
# Calculates and prints the confusion matrix for the test set, showing true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN).
conf_mat=confusion_matrix(y_test,y_test_prediction)
print(conf_mat)

# Creates a heatmap using Seaborn to visualize the confusion matrix. This provides a graphical representation of the model's performance.

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
sns.heatmap(conf_mat,annot=True,fmt='d')
plt.title("Confusion Matrix of test data")
plt.xlabel("Predicted value")
plt.ylabel("Actual value")
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_test_prediction))

TN=conf_mat[0][0]
FP=conf_mat[0][1]
FN=conf_mat[1][0]
TP=conf_mat[1][1]

recall=TP/(TP+FN)
print("Recall=",recall)
precision=TP/(TP+FP)
print("Precision=",precision)
specificity=TN/(TN+FP)
print("Specificity=",specificity)
accuracy=(TP+TN)/(TP+FP+FN+TN)
print("Accuracy=",accuracy)


