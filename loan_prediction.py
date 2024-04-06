# -*- coding: utf-8 -*-
"""Loan_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1evrcXQdt7cTU9fvvK052batVmT7F1ybq
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import files
data =files.upload()

data

import pandas as pd


# Load the CSV file into a DataFrame
df = pd.read_csv('dataset.csv')

# Display the first few rows of the DataFrame
print(df.head())

df.head()

df.columns

df.info()

"""#Data Preprocessing"""

df.isna().sum()

df['Gender'].value_counts()

df.Gender = df.Gender.fillna('Male')

df['Married'].value_counts()

df.Married = df.Married.fillna('Yes')

df['Dependents'].value_counts()

df.Dependents = df.Dependents.fillna('0')

df.Self_Employed = df.Self_Employed.fillna('No')

df['Loan_Amount_Term'].value_counts()

df.Loan_Amount_Term = df.Loan_Amount_Term.fillna(360.0)

df['Credit_History'].value_counts()

df.Credit_History = df.Credit_History.fillna(1.0)

df.isna().sum()

df['LoanAmount'].value_counts()

df.LoanAmount = df.LoanAmount.fillna(120.0)

df.isna().sum()

#Split the data into input and output
X = df.iloc[:,1:12].values
y = df.iloc[:,12]

y

#train and test split

from sklearn.model_selection import train_test_split

X_train,X_test,y_train, y_test = train_test_split(X,y, test_size=0.15,random_state=0)

X_train

from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()

for i in range(0,5):
  X_train[:,i] = labelencoder.fit_transform(X_train[:,i])
X_train[:,10] = labelencoder.fit_transform(X_train[:,10])

labelencoder_y = LabelEncoder()

y_train = labelencoder_y.fit_transform(y_train)

labelencoder_xt = LabelEncoder()

for i in range(0,5):
  X_test[:,i] = labelencoder.fit_transform(X_test[:,i])
X_test[:,10] = labelencoder.fit_transform(X_test[:,10])

y_test = labelencoder_y.fit_transform(y_test)

y_test

X_train

#Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)

X_train

X_test = sc.fit_transform(X_test)

# PCA

from sklearn.decomposition import PCA

pca = PCA(n_components=3)

X_train = pca.fit_transform(X_train)

X_test = pca.fit_transform(X_test)

X_train

#Classification
# logistic regression
# nearest neighbor
# SVM

#Logistic Regression
from sklearn.linear_model import LogisticRegression

lrclf = LogisticRegression(max_iter=100,random_state=0)

lrclf.fit(X_train,y_train)

lrclf.predict(X_test)

y_pred = lrclf.predict(X_test)

y_test

from sklearn import metrics

metrics.accuracy_score(y_test,y_pred)

cm = metrics.confusion_matrix(y_test,y_pred)

cm

X_test[:,0]

# observed data plot
plt.scatter(X_test[:,0],y_test,c=y_test)

# KNN
from sklearn.neighbors import KNeighborsClassifier

knnclf = KNeighborsClassifier(n_neighbors=5)

knnclf.fit(X_train,y_train)

knnclf.predict(X_test)

y_pred = knnclf.predict(X_test)

plt.scatter(X_test[:,0],y_test, c=y_test)

plt.scatter(X_test[:,0],y_pred,c=y_pred)

metrics.accuracy_score(y_test,y_pred)

cm = metrics.confusion_matrix(y_test,y_pred)

cm

# Support Vector Machine
from sklearn.svm import SVC

svcrbf = SVC(random_state=0)
svclin = SVC(random_state=0)

svcrbf.fit(X_train,y_train)
svclin.fit(X_train,y_train)

y_predr = svcrbf.predict(X_test)
y_predl = svclin.predict(X_test)

#rbf svm
metrics.accuracy_score(y_test,y_predr)

#lin svm
metrics.accuracy_score(y_test,y_predl)