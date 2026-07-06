from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

#Load dataset
data = load_breast_cancer()
x, y = data.data, data.target

#Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset information
print(f'Features: {data.feature_names}')
print(f'Classes: {data.target_names}')

#Train Gradient Boosting model
gb_model = GradientBoostingClassifier(random_state=42)
gb_model.fit(x_train, y_train)

#Predict
y_pred_gb = gb_model.predict(x_test)

#Evaluate performance
accuracy_gb = accuracy_score(y_test, y_pred_gb)
print(f'Gradient Boosting Accuracy: {accuracy_gb:.2f}')
print('\n Classfication Report: \n ',  classification_report(y_test, y_pred_gb))


