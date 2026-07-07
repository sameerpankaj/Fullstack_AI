'''
LightGBM (Light Gradient Boosting Machine) is a fast, efficient Gradient Boosting framework developed by Microsoft. It is designed for large datasets and is often faster than XGBoost while achieving comparable or better accuracy.

How LightGBM works

Like XGBoost, LightGBM:

Builds decision trees sequentially.
Each new tree corrects the errors of previous trees.
Minimizes a loss function using gradient boosting.

Its main difference is how it grows trees.

LightGBM vs. XGBoost
XGBoost	LightGBM
Level-wise tree growth	Leaf-wise tree growth
Slower	Faster
Higher memory usage	Lower memory usage
Good for medium datasets	Excellent for very large datasets
Less risk of overfitting	Can overfit if not tuned
Level-wise growth (XGBoost)
        Root
       /    \
      A      B
     / \    / \

The tree grows one level at a time, making balanced trees.

Leaf-wise growth (LightGBM)
        Root
       /    \
      A      B
     /
    C
   /
  D

The algorithm always splits the leaf with the greatest potential improvement, often reducing the loss faster.

Advantages

Faster training
Often higher accuracy
Fewer trees needed

Disadvantage

More prone to overfitting on small datasets.
Install
pip install lightgbm
Python example
from lightgbm import LGBMClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LGBMClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
Important hyperparameters
Hyperparameter	Purpose
n_estimators	Number of trees
learning_rate	Step size for each tree
max_depth	Maximum tree depth
num_leaves	Maximum number of leaves in one tree
min_child_samples	Minimum samples required in a leaf
subsample	Fraction of rows used per tree
colsample_bytree	Fraction of features used per tree
reg_alpha	L1 regularization
reg_lambda	L2 regularization
Example with tuned parameters
model = LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
When to use LightGBM

Choose LightGBM when:

You have large tabular datasets (hundreds of thousands or millions of rows).
Training speed is important.
You want strong predictive performance with relatively low memory usage.
Random Forest vs. XGBoost vs. LightGBM
Feature	Random Forest	XGBoost	LightGBM
Ensemble type	Bagging	Boosting	Boosting
Tree growth	Independent trees	Level-wise	Leaf-wise
Training speed	Fast	Moderate	Fastest
Accuracy	Good	Excellent	Excellent
Handles missing values	Limited	Yes	Yes
Hyperparameter tuning	Simple	Moderate	Moderate
Best for	Strong baseline	High accuracy	Large datasets & speed
Interview answer (30 seconds)

LightGBM is a Gradient Boosting framework from Microsoft that uses leaf-wise tree growth instead of level-wise growth. This usually makes it faster and more memory-efficient than XGBoost, especially on large tabular datasets. It supports parallel training, handles missing values automatically, and offers high predictive accuracy, though it may overfit on smaller datasets if hyperparameters such as num_leaves and max_depth are not tuned properly.


'''