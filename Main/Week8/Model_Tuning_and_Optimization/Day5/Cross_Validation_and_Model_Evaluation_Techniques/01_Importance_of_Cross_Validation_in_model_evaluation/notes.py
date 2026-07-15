'''
Cross-validation is a technique used to evaluate how well a machine learning model will perform on unseen data. Instead of testing the model on just one train-test split, it trains and tests the model multiple times on different splits of the dataset.

Why use Cross-Validation?

Suppose you split your data once:

80% → Training
20% → Testing

Your accuracy might be 95%.

But if you choose a different random split, the accuracy might become 91%.

A single train-test split can give misleading results. Cross-validation reduces this problem by evaluating the model on multiple splits.

K-Fold Cross-Validation

The most common method is K-Fold Cross-Validation.

If K = 5, the data is divided into 5 equal parts (folds).

Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5

The model is trained and tested 5 times.

Iteration 1
Train: Fold 2 + Fold 3 + Fold 4 + Fold 5
Test : Fold 1
Iteration 2
Train: Fold 1 + Fold 3 + Fold 4 + Fold 5
Test : Fold 2
Iteration 3
Train: Fold 1 + Fold 2 + Fold 4 + Fold 5
Test : Fold 3
Iteration 4
Train: Fold 1 + Fold 2 + Fold 3 + Fold 5
Test : Fold 4
Iteration 5
Train: Fold 1 + Fold 2 + Fold 3 + Fold 4
Test : Fold 5

Every sample is used:

Once for testing
K−1 times for training
Example

Suppose the model achieves these accuracies:

Fold	Accuracy
1	95%
2	96%
3	94%
4	97%
5	95%

Average accuracy:

(95 + 96 + 94 + 97 + 95) / 5

= 95.4%

This average is a more reliable estimate than using just one train-test split.

Python Example
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load dataset
X, y = load_breast_cancer(return_X_y=True)

# Create model
model = RandomForestClassifier(random_state=42)

# Perform 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5)

print("Scores:", scores)
print("Average Accuracy:", scores.mean())

Example output:

Scores:
[0.956 0.974 0.965 0.982 0.973]

Average Accuracy:
0.970
cross_val_score()

Syntax:

cross_val_score(
    estimator,
    X,
    y,
    cv=5,
    scoring='accuracy'
)

Parameters:

estimator → Machine learning model
X → Features
y → Target
cv → Number of folds
scoring → Evaluation metric
Common values of cv
Value	Meaning
3	3-fold Cross-Validation
5	5-fold Cross-Validation (most common)
10	10-fold Cross-Validation (more reliable, slower)
Advantages
Uses all data for both training and testing.
Gives a more reliable estimate of model performance.
Reduces the chance of results depending on one lucky or unlucky split.
Helpful when comparing different models or tuning hyperparameters.
Disadvantages
Slower than a single train-test split because the model is trained multiple times.
Can be computationally expensive for large datasets or complex models.
Train-Test Split vs Cross-Validation
Feature	Train-Test Split	Cross-Validation
Number of splits	1	Multiple
Model training	Once	K times
Reliability	Lower	Higher
Speed	Faster	Slower
Best use	Quick experiments	Model evaluation and hyperparameter tuning
Interview definition

Cross-validation is a model evaluation technique in which a dataset is divided into multiple folds. The model is trained on some folds and tested on the remaining fold, repeating the process until every fold has been used for testing. The final performance is the average across all folds, providing a more reliable estimate of how the model will perform on unseen data.


'''



'''
There are several types of cross-validation, each suited for different kinds of datasets and problems.

1. K-Fold Cross-Validation (Most Common)

The dataset is divided into K equal folds.

Example: K = 5

Fold1 | Fold2 | Fold3 | Fold4 | Fold5

The model is trained 5 times.

Each fold is used once for testing.
The remaining folds are used for training.
Python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

scores = cross_val_score(model, X, y, cv=5)
print(scores)

Best for: General classification and regression.

2. Stratified K-Fold Cross-Validation

Similar to K-Fold, but it preserves the class distribution in every fold.

Example:

Original dataset:

90% Healthy
10% Diseased

Every fold also contains approximately:

90% Healthy
10% Diseased

This is especially useful for imbalanced classification datasets.

Python
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(n_splits=5)

Best for: Classification with imbalanced classes.

3. Leave-One-Out Cross-Validation (LOOCV)

Each iteration uses one sample for testing and all remaining samples for training.

Example:

100 samples:

Iteration 1
Train = 99
Test = 1

Iteration 2
Train = 99
Test = 1

...

Iteration 100
Train = 99
Test = 1
Python
from sklearn.model_selection import LeaveOneOut

cv = LeaveOneOut()

Advantages

Uses almost all data for training.

Disadvantages

Very slow for large datasets.

Best for: Very small datasets.

4. Leave-P-Out Cross-Validation

Instead of leaving one sample out, it leaves P samples out.

Example:

P = 2

Train = 98
Test = 2
Python
from sklearn.model_selection import LeavePOut

cv = LeavePOut(p=2)

Best for: Small datasets.

5. Repeated K-Fold Cross-Validation

Runs K-Fold multiple times using different random splits.

Example:

5-Fold

Repeated 3 times

Total training rounds = 15
Python
from sklearn.model_selection import RepeatedKFold

cv = RepeatedKFold(
    n_splits=5,
    n_repeats=3,
    random_state=42
)

Best for: More stable performance estimates.

6. ShuffleSplit

Randomly splits the dataset multiple times.

The same sample can appear in multiple test sets.

Python
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(
    n_splits=10,
    test_size=0.2,
    random_state=42
)

Best for: Randomized evaluation.

7. Time Series Cross-Validation

Used for time-dependent data.

Unlike standard K-Fold, it never trains on future data.

Example:

Train: Jan Feb Mar
Test : Apr

Train: Jan Feb Mar Apr
Test : May

Train: Jan Feb Mar Apr May
Test : Jun
Python
from sklearn.model_selection import TimeSeriesSplit

cv = TimeSeriesSplit(n_splits=5)

Best for: Stock prices, weather forecasting, sales prediction.

8. Group K-Fold Cross-Validation

Keeps all samples from the same group together.

Example:

Suppose patient data:

Patient A
Patient A
Patient A

Patient B
Patient B

Patient C

Data from the same patient will never appear in both training and testing.

Python
from sklearn.model_selection import GroupKFold

cv = GroupKFold(n_splits=5)

Best for: Medical, customer, or user-based datasets.

Comparison
Type	Best For	Main Feature
K-Fold	General ML	Equal folds
Stratified K-Fold	Imbalanced classification	Preserves class ratio
Leave-One-Out (LOOCV)	Very small datasets	Tests one sample at a time
Leave-P-Out	Small datasets	Tests P samples at a time
Repeated K-Fold	More reliable evaluation	Repeats K-Fold multiple times
ShuffleSplit	Random evaluation	Random train/test splits
TimeSeriesSplit	Time-series data	Respects chronological order
GroupKFold	Grouped data	Keeps groups together
Which one should you use?
Most classification problems: StratifiedKFold
Most regression problems: KFold
Very small datasets: LeaveOneOut
Time-series forecasting: TimeSeriesSplit
Grouped data (e.g., patients/users): GroupKFold
More robust evaluation: RepeatedKFold

'''