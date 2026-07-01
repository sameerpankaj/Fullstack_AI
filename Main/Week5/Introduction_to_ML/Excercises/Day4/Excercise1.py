#Implement a logistic regression model to classfiy a dataset(e.g, predicting if a customer will make a purchase)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

#Gnerate synthetic dataset
np.random.seed(42)
n_samples = 200
x = np.random.rand(n_samples, 2) * 10
y = (x[:, 0] * 1.5 + x[:, 1] > 15).astype(int)

#Create a dataframe
df = pd.DataFrame(x, columns=['Age', 'Salary'])
df['Purchase'] = y

#Split data
x_train, x_test, y_train, y_test = train_test_split(df[['Age', 'Salary']], df['Purchase'], test_size=0.2, random_state=42)

#Train logistics regression model
model= LogisticRegression()
model.fit(x_train, y_train)

#Make Prediction
y_pred  = model.predict(x_test)

#Evaluate performance
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1 Score:', f1_score(y_test, y_pred))
print('\nClassification Report: n\:', classification_report(y_test, y_pred))
