import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier


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

#Define hyperparameter grid
param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 0.1]
}

#Initialize XGBoost classifier
xgb_clf = XGBClassifier(eval_metric='logloss', random_state=42)


#Perform Grid Search
grid_search = GridSearchCV(estimator=xgb_clf, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1 )
grid_search.fit(x_train, y_train)

#Display the best parameters and score
print(f'Best Parameters: {grid_search.best_params_}')
print(f'Best cross validation accuracy: {grid_search.best_score_}')

#