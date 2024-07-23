# -*- coding: utf-8 -*-
"""Customer_Churn_Pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HBSX4_QlEVJEd-iFEVCsTkbEQIKSguNK
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score

df = pd.read_csv('/content/Churn_Modelling.csv')

df.head()

df.info()

df.describe()

df = df.drop(columns = ['RowNumber', 'CustomerId', 'Surname'])

df.head()

df.info()

df['Gender'].unique()

df['Gender'].value_counts()

colors = ["#96CBFC" , "#FFC2D9"]

plt.figure(figsize = (20, 6))

counts = df['Gender'].value_counts()
explode = (0, 0.1)

counts.plot(kind = 'pie', fontsize = 12, colors = colors, explode = explode, autopct = '%.1f%%')
plt.title('Males Vs Females')
plt.xlabel('Gender', weight = "bold", color = "#2F0F5D", fontsize = 14, labelpad = 20)
plt.ylabel('Counts', weight = "bold", color = "#2F0F5D", fontsize = 14, labelpad = 20)
plt.legend(labels = counts.index, loc = "best")
plt.show()

df = pd.get_dummies(data = df, drop_first = True, dtype = int)

df.head()

"""0 = female and 1 = male

"""

sns.pairplot(df)

df.Exited.plot.hist()

(df.Exited == 0).sum()              #for people who are still in the bank

(df.Exited == 1).sum()              #for people who have left the bank

dfs = df.drop(columns = 'Exited')

dfs.corrwith(df.Exited).plot.bar(figsize = (16, 9), title = "Correlation with Exited", fontsize = 15, rot = 30, grid = True)
plt.show()

corr = df.corr()

plt.figure(figsize = (10, 10))
sns.heatmap(corr, annot = True, cmap = 'magma')

#splitting the data

x = df.drop(columns = 'Exited')
y = df['Exited']

x_train, x_tst, y_train, y_tst = train_test_split(x, y, test_size = 0.2, random_state = 42)

x_tst.shape

scale = StandardScaler()

x_train = scale.fit_transform(x_train)

x_tst = scale.transform(x_tst)

x_train

#Logistic Regression

Lreg = LogisticRegression(random_state = 0).fit(x_train, y_train)

ypred = Lreg.predict(x_tst)

a_s = accuracy_score(y_tst, ypred)

fone = f1_score(y_tst, ypred)

prc = precision_score(y_tst, ypred)

results = pd.DataFrame([['Logistic Regression', a_s, fone, prc]], columns = ['Model', 'Accuracy Score', 'F1 Score', 'Precision Score'])

results

print(confusion_matrix(y_tst, ypred))

#random forest

rfc = RandomForestClassifier(random_state = 0).fit(x_train, y_train)

ypred = rfc.predict(x_tst)

a_s = accuracy_score(y_tst, ypred)

fone = f1_score(y_tst, ypred)

prc = precision_score(y_tst, ypred)

res = pd.DataFrame([['Random Forest Result', a_s, fone, prc]], columns = ['Model', 'Accuracy Score', 'F1 Score', 'Precision Score'])

res

results = pd.concat([results, res], ignore_index = True)

results

#testing the model

df.head()

test1 = [[732, 35, 3 , 12345, 3, 1, 1,159000, 1, 0, 1]]

Lreg.predict(scale.fit_transform(test1))

# 0 = Customer is going to stay Bank

test2 = [[650, 30, 1, 0,1,1,75000, 1 , 0 , 1, 0]]

rfc.predict(scale.fit_transform(test2))

# 0 = Customer is going to stay with this Bank
