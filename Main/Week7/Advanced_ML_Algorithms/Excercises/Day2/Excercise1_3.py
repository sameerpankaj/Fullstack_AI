from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV


#Load dataset
data = load_breast_cancer()
x, y = data.data, data.target

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset information
# print('Features:', data.feature_names)
# print('Classes:', data.target_names)

#Train Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(x_train, y_train)

#Predict
y_pred = rf_model.predict(x_test)

#Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print('RAndom Forest Accuracy: ', accuracy)
print('\n Classfication Report: \n', classification_report(y_test, y_pred))

#Define hyperparameter grid
param_trid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'max_features': ['sqrt', 'log2', None]
}

grid_search = GridSearchCV(
    estimator= RandomForestClassifier(random_state=42),
    param_grid=param_trid,
    cv=5,
    scoring='accuracy',
    n_jobs=1
)

grid_search.fit(x_train, y_train)

#Display best parameters 
print(f'Best Parameters:{grid_search.best_params_}')
print(f'Best Cross validation accuracy : {grid_search.best_score_}')

