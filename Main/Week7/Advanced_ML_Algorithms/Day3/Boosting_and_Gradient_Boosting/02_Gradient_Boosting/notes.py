'''
What is Gradient Boosting?
    --Boosting algorithm that builds models subsequentially by mininizing a loss function using gradient descent
    --Iteratively adds weak learners to improve overall model perfromance
How Gradient Boosting works?
Gradient Boosting is an ensemble learning algorithm that builds many weak learners (usually decision trees) sequentially. Each new tree tries to correct the errors made by the previous trees.

Step-by-step example

Suppose you want to classify whether a tumor is benign (0) or malignant (1).

Step 1: Train the first tree

The first decision tree makes initial predictions.

Actual	Prediction
1	1 ✅
0	0 ✅
1	0 ❌
0	1 ❌

There are two mistakes.

Step 2: Calculate the errors (residuals)

Gradient Boosting measures how wrong the predictions are.

For classification, it minimizes a loss function (such as log loss). For regression, the residual is simply:

Residual = Actual − Prediction

The errors indicate what the next tree should learn.

Step 3: Train the second tree

The second tree is trained only to predict the errors made by the first tree, not the original labels.

It focuses more on the difficult samples.

Step 4: Update predictions

Instead of replacing the first tree, Gradient Boosting combines them:

New Prediction =
Old Prediction + Learning Rate × Tree 2 Prediction

The learning rate controls how much each new tree contributes.

Example:

Tree 1 prediction = 0.60
Tree 2 correction = +0.20
Learning rate = 0.1
New Prediction = 0.60 + (0.1 × 0.20)
               = 0.62
Step 5: Repeat

A third tree corrects the remaining errors, then a fourth, and so on.

Tree 1 → Tree 2 → Tree 3 → ... → Tree N

Each tree learns from the mistakes of all previous trees.

Python example
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
gb_model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

gb_model.fit(X_train, y_train)

# Predict
y_pred = gb_model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
Important hyperparameters
n_estimators: Number of trees. More trees can improve performance but increase training time.
learning_rate: Controls how much each tree contributes. Smaller values often improve generalization but require more trees.
max_depth: Maximum depth of each tree. Shallower trees help reduce overfitting.
subsample: If less than 1.0, trains each tree on a random subset of the data, which can improve robustness.
Bagging vs. Gradient Boosting
Bagging	Gradient Boosting
Trees are built independently	Trees are built sequentially
Reduces variance	Reduces bias and variance
Random Forest is the most common example	Gradient Boosting, XGBoost, LightGBM, CatBoost
Trees vote equally	Each tree corrects previous errors
Easy to parallelize	Sequential, so slower to train

Key idea: Gradient Boosting starts with a simple model, measures its mistakes using a loss function, trains a new tree to reduce those mistakes, updates the predictions, and repeats this process until the model becomes highly accurate.

'''