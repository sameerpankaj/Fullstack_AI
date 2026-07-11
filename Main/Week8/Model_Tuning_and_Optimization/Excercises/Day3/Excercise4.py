#Compare with grid and random search

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import optuna 


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

#Define the objective function for optuna
def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'max_depth': trial.suggest_int('max_depth', 3, 100),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'gamma': trial.suggest_float('gamma', 0, 5),
        'reg_alpha': trial.suggest_float('reg_aplha', 0, 10),
        'reg_lambda': trial.suggest_float('reg_lambda', 0, 10)


    }

    #Train XGboost model with the suggested params from above
    model = XGBClassifier(eval_metric='logloss', random_state=42, **params)
    model.fit(x_train, y_train)

    #evaluate model on valiadation set
    preds = model.predict(x_test)
    accuracy = accuracy_score(y_test, preds)
    return accuracy


#Create an Optuna study
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)

#Best hyperparameters are
print('Best hyperparameters: ', study.best_params)
print('best Accuracy:', study.best_value)

#Define parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.6, 0.8, 1.0]
}

#Train XGboost with Grid search
grid_search = GridSearchCV(
    estimator=XGBClassifier(eval_metric='logloss', random_state=42),
    param_grid=param_grid,
    scoring='accuracy',
    cv=3,
    verbose=1
)

grid_search.fit(x_train, y_train)

#Best parameters and accuracy
print('\n\n\nGrid Search Best Parameters: ', grid_search.best_params_)
print('Grid Search Best Accuracs: ', grid_search.best_score_)


#Define parameter distribution
param_dist = {
    'n_estimators': [50, 100, 200, 300, 400],
    'max_depth': [3, 5, 7, 9],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0]
}

#Train XGBoost with Random search
random_search = RandomizedSearchCV(
    estimator=XGBClassifier(eval_metric='logloss', random_state=42),
    param_distributions=param_dist,
    n_iter=50, 
    scoring='accuracy',
    cv=3,
    verbose=1,
    random_state=42
)

random_search.fit(x_train, y_train)

#best parameters and accuracy for random search
print('\n\n\nRandom search Best Parameters: ', random_search.best_params_)
print('Random Search Best Accuracy', random_search.best_score_)



#Baseline XGBoost Accuracy: 0.9649
#best Accuracy: 0.9649122807017544

# Grid Search Best Parameters:  {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 200, 'subsample': 0.6}
# Grid Search Best Accuracs:  0.9735970721505751
# Fitting 3 folds for each of 50 candidates, totalling 150 fits



# Random search Best Parameters:  {'subsample': 0.9, 'n_estimators': 300, 'max_depth': 3, 'learning_rate': 0.2, 'colsample_bytree': 0.8}
# Random Search Best Accuracy 0.9779975601254792