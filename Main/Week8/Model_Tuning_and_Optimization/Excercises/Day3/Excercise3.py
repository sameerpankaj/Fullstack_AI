#Apply the Bayesian Optimization

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
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