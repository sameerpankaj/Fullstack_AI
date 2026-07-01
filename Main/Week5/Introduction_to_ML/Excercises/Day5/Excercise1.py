#Evaluate a model using cross validation to obtain a more accurate estimate of model performance

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

#Load datasets
data = load_iris()
x, y = data.data, data.target

#Initialize classfier
model = RandomForestClassifier(random_state=42)

#Perform K-Fold cross validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, x, y, cv=kf, scoring='accuracy')

#Output results
print('Corss validation scores: ', cv_scores)
print('Mean Accuracy:', cv_scores.mean())