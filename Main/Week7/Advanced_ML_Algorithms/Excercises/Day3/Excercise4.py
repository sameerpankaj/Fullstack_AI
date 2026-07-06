#Compare gradient boosting with random forest


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
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

#Define a hyperparameter grid
param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7]
}

#Perform Grid search
grid_searach = GridSearchCV(
    estimator=GradientBoostingClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=1

)

grid_searach.fit(x_train, y_train)

#Display best parameters and score
print(f'Best Parameters: {grid_searach.best_params_}')
print(f'Best Cross validation Accuracy: {grid_searach.best_score_:.2f}')

#Train Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(x_train, y_train)

##Predict 
y_pred_rf = rf_model.predict(x_test)


#Evaluate performance
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Random Forest Accuracy: {accuracy_rf:.2f}')

