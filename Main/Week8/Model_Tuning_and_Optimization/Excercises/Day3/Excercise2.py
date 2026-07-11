#Define baseline xgboost model

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

#Load datasets
data = load_breast_cancer()
x, y = data.data, data.target

#Split into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Standarize features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

print(f'Taining data shape: {x_train.shape}')
print(f'Test data shape: {x_test.shape}')

#Train a baseline xgboost model
baseline_model = XGBClassifier(eval_metric='logloss', random_state=42)
baseline_model.fit(x_train, y_train)

#Evaluate the model
baseline_pred = baseline_model.predict(x_test)
baseline_accuracy = accuracy_score(y_test, baseline_pred)
print(f'Baseline XGBoost Accuracy: {baseline_accuracy:.4f}')