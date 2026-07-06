import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

#Load Dataset
data = load_breast_cancer()
x, y = data.data, data.target

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset infor
print(f'Features: {data.feature_names}')
print(f'Classes: {data.target_names}')

#Convert dataset to DMatrix
dtrain = xgb.DMatrix(x_train, label=y_train)
dtest = xgb.DMatrix(x_test, label=y_test)

#Train XGBoost model
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'max_depth': 3,
    'eta': 0.1
}

xgb_model = xgb.train(
    params,
    dtrain,
    num_boost_round=100
)

#Predict
y_pred = (xgb_model.predict(dtest) > 0.5).astype(int)

#Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print(f'XGBoost Accuracy: {accuracy}')
print('\nClassfication Report; \n', classification_report(y_test, y_pred))