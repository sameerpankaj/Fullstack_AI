'''


CatBoost (Categorical Boosting) is a Gradient Boosting algorithm developed by Yandex. It is designed to work especially well with categorical features (e.g., country, gender, city, product type) without requiring extensive preprocessing.

Like XGBoost and LightGBM, CatBoost builds decision trees sequentially, where each new tree corrects the errors made by the previous trees.

Why use CatBoost?

Most machine learning algorithms require categorical variables to be converted into numbers using techniques like:

One-Hot Encoding
Label Encoding

CatBoost can handle categorical features directly, saving preprocessing time and often improving performance.

Example dataset:

Age	Gender	City	Bought
25	Male	Berlin	Yes
30	Female	Munich	No

With CatBoost, you can specify:

cat_features = ['Gender', 'City']

No manual encoding is required.

Advantages
✅ Handles categorical features automatically
✅ High accuracy on tabular data
✅ Less preprocessing
✅ Handles missing values
✅ Reduces overfitting using ordered boosting
✅ Good default hyperparameters
Install
pip install catboost
Python example
from catboost import CatBoostClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create model
model = CatBoostClassifier(
    iterations=200,
    learning_rate=0.1,
    depth=6,
    verbose=0
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
Important hyperparameters
Hyperparameter	Purpose
iterations	Number of boosting rounds (trees)
learning_rate	Step size of boosting
depth	Maximum tree depth
l2_leaf_reg	L2 regularization
loss_function	Loss to optimize
eval_metric	Evaluation metric
random_seed	Reproducibility
verbose	Training output

Example:

model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=8,
    l2_leaf_reg=3,
    random_seed=42,
    verbose=100
)
XGBoost vs. LightGBM vs. CatBoost
Feature	XGBoost	LightGBM	CatBoost
Tree growth	Level-wise	Leaf-wise	Symmetric (oblivious) trees
Speed	Fast	Fastest	Moderate
Handles categorical features directly	No	Limited	Yes
Missing values	Yes	Yes	Yes
Overfitting control	Strong	Good	Strong
Preprocessing required	More	Some	Least
When to use each?
XGBoost: Excellent all-around choice for structured/tabular data.
LightGBM: Best for very large datasets where training speed matters.
CatBoost: Best when your data contains many categorical features and you want minimal preprocessing.
Interview answer (30 seconds)

CatBoost is a Gradient Boosting algorithm developed by Yandex. Its key advantage is that it can handle categorical features directly without manual encoding, while also supporting missing values and reducing overfitting through ordered boosting and symmetric trees. It often performs very well on tabular datasets with many categorical variables and requires less preprocessing than XGBoost or LightGBM.


'''