
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

#Load dataset
data = load_iris()
x, y = data.data, data.target

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Scale features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Train Individual models
log_model = LogisticRegression()
dt_model = DecisionTreeClassifier()
knn_model = KNeighborsClassifier()

#Fit models
log_model.fit(x_train, y_train)
dt_model.fit(x_train, y_train)
knn_model.fit(x_train, y_train)

#Creating voting classfier
ensemble_model = VotingClassifier(
    estimators=[
        ('log_reg', log_model),
        ('decision_tree', dt_model),
        ('knn', knn_model)
    ],
    voting='hard'
)

#Train Ensemble model
ensemble_model.fit(x_train, y_train)

#Predict with ensemble
y_pred_ensemble = ensemble_model.predict(x_test)

#Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred_ensemble)



#evaluate individual models
y_pred_log = log_model.predict(x_test)
y_pred_dt = dt_model.predict(x_test)
y_pred_knn = knn_model.predict(x_test)

print(f'Logisitic() Model Accuracy: {accuracy_score(y_test, y_pred_log):.2f}')
print(f'Decision Tree  Accuracy: {accuracy_score(y_test, y_pred_dt):.2f}')
print(f'k_NN  Accuracy: {accuracy_score(y_test, y_pred_knn):.2f}')
print(f'Ensemble Model Accuracy: {accuracy:.2f}')







