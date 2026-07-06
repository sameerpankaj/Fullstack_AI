'''
What is Boosting?
    --Ensemble technique that sequentially combines weak learners to form a strong learner
    --Each subsequent model focuses on correcting the errors made by previous models
How Does Boosting differ from Bagging?

Bagging and Boosting are both ensemble learning techniques, but they work differently.

Feature	Bagging	Boosting
Goal	Reduce variance	Reduce bias and variance
Training	Models are trained independently	Models are trained sequentially
Data	Each model gets a random bootstrap sample	Each model focuses more on previous errors
Combination	Equal voting/averaging	Weighted voting/sum
Parallelization	Can be trained in parallel	Cannot be easily parallelized
Overfitting	Less likely	More likely if not tuned
Bagging (Bootstrap Aggregating)
Creates multiple training datasets by sampling with replacement.
Trains many models independently.
Final prediction is based on majority vote (classification) or average (regression).

Example: Random Forest

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

Advantages

Reduces overfitting.
Robust to noisy data.
Fast because trees can be built in parallel.
Boosting
Models are trained one after another.
Each new model tries to correct mistakes made by previous models.
Final prediction is a weighted combination of all models.

Example: AdaBoost

from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

Example: Gradient Boosting

from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)
Simple analogy

Imagine predicting whether an email is spam:

Bagging: 100 experts each independently review different samples of emails. The final decision is based on majority vote.
Boosting: The first expert reviews the email. The second focuses on mistakes the first made. The third focuses on mistakes of the first two, and so on. Together they produce a stronger prediction.
Popular algorithms

Bagging

Random Forest
BaggingClassifier

Boosting

AdaBoost
Gradient Boosting
XGBoost
LightGBM
CatBoost
When to use which?
Use Bagging when your model is overfitting (high variance), especially with decision trees.
Use Boosting when you want the highest predictive accuracy and are willing to spend more time tuning hyperparameters.

In one sentence: Bagging trains many models independently and combines their predictions, while Boosting trains models sequentially, with each model learning from the errors of the previous ones.

'''