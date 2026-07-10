#Implement Grid Search

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Load dataset
data = load_iris()
x, y = data.data, data.target

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset info
print(f'Feature Names: {data.feature_names}')
print(f'Class Names: {data.target_names}')

#Define hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10]
}

#Initialze Grid search
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5, 
    scoring='accuracy',
    n_jobs=1
)

#Perform grid search
grid_search.fit(x_train, y_train)

#Evaluate the best options or models
best_grid_model = grid_search.best_estimator_
y_pred_grid = best_grid_model.predict(x_test)
accuracy_grid = accuracy_score(y_test, y_pred_grid)

print(f'Best Hyperparameters (Grid Search): {grid_search.best_params_}')
print(f'Grid Search Accuracy: {accuracy_grid:.4f}')
