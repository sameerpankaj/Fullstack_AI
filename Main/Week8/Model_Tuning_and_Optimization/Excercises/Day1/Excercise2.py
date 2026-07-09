#Train a model with some default hyperparameters

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

#Load dataset
data = load_iris()
x, y = data.data, data.target

#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display datasets info
print(f'Feature Names: {data.feature_names}')
print(f'Class Names: {data.target_names}')

#Train Random Forest with default hyperparameters
rf_default = RandomForestClassifier(random_state=42)
rf_default.fit(x_train, y_train)

#Predict and evaluate
y_predict_default = rf_default.predict(x_test)
accuracy_default = accuracy_score(y_test, y_predict_default)

print(f'Default Model Accuracy: {accuracy_default:.4f}')
print('\n Classficiation Report:\n', classification_report(y_test, y_predict_default))