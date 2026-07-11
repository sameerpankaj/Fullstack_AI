#Load and preprocess datasets
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

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

'''

This program prepares the Breast Cancer Wisconsin dataset for machine learning. It does not train a model—it only loads, splits, and standardizes the data.

Let's go through it line by line.

1. Import Libraries
from sklearn.datasets import load_breast_cancer
What is sklearn?

sklearn stands for Scikit-learn, one of Python's most popular machine learning libraries.

It provides:

Datasets
Machine learning algorithms
Data preprocessing
Model evaluation
Hyperparameter tuning
datasets

The datasets module contains built-in datasets for learning and testing machine learning algorithms.

Examples:

Iris Dataset
Breast Cancer Dataset
Wine Dataset
Digits Dataset
load_breast_cancer()

This function loads the Breast Cancer Wisconsin Diagnostic Dataset.

It contains:

569 patients
30 input features
Target (0 or 1)

Target values:

0 → Malignant (Cancer)
1 → Benign (No cancer)
from sklearn.model_selection import train_test_split
model_selection

This module helps prepare data for machine learning.

It contains tools such as:

train_test_split()
K-Fold Cross Validation
GridSearchCV
RandomizedSearchCV
train_test_split()

Splits data into:

Training set
Testing set

Why?

We train the model on one dataset and test it on unseen data.

Example:

100 samples

80 → Training
20 → Testing

This checks whether the model generalizes well.

from sklearn.preprocessing import StandardScaler
preprocessing

Used to clean or transform data before training.

Examples:

StandardScaler
MinMaxScaler
LabelEncoder
OneHotEncoder
StandardScaler

Standardizes every feature so they have:

Mean = 0

Standard deviation = 1

Formula:

z=
σ
x−μ
	​


where:

x = original value
μ = mean
σ = standard deviation

Example

Original values:

Age

20
30
40
50
60

Mean = 40

After StandardScaler:

-1.41
-0.71
0
0.71
1.41

This helps many ML algorithms train more effectively.

import pandas as pd
Pandas

Pandas is a data analysis library.

It provides:

DataFrame
Reading CSV files
Cleaning data
Filtering
Statistics

Example:

df = pd.read_csv("data.csv")

In your program, Pandas is imported but never used, so you could remove this line without changing the output.

2. Load Dataset
data = load_breast_cancer()

This loads the dataset into a Bunch object (similar to a dictionary).

It contains:

data.data

Input features.

data.target

Output labels.

You can inspect it:

print(data.keys())

Output:

dict_keys([
'data',
'target',
'feature_names',
'target_names',
'DESCR'
])
3. Separate Features and Target
x, y = data.data, data.target
X

Independent variables (features)

Shape:

569 × 30

Each patient has 30 measurements.

Example:

Radius
Texture
Area
Smoothness
...
y

Dependent variable (label)

Shape:

569

Example:

0
1
1
0
1
...
4. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

This divides the data into training and testing sets.

test_size=0.2

20% goes to testing.

569 samples

≈455 → Training

≈114 → Testing
random_state=42

Ensures the split is the same every time you run the program.

Without it:

Run 1
Training: Sample A

Run 2
Training: Sample B

With random_state=42:

Every run produces the same split.

5. Create StandardScaler
scaler = StandardScaler()

Creates a scaler object.

Nothing happens yet.

6. Fit and Transform Training Data
x_train = scaler.fit_transform(x_train)

This performs two steps:

Step 1: fit()

Learns the mean and standard deviation from the training data.

Example:

Feature:

10
20
30
40

Mean = 25

Std = 11.18
Step 2: transform()

Uses those values to standardize the training data.

Why use fit_transform()?

It's simply a shortcut for:

scaler.fit(x_train)
x_train = scaler.transform(x_train)
7. Transform Test Data
x_test = scaler.transform(x_test)

Notice this is only transform(), not fit_transform().

This is important because the model should only learn scaling parameters from the training data. If you called fit() on the test data, information from the test set would leak into training, leading to overly optimistic results.

8. Print Shapes
print(f'Training data shape: {x_train.shape}')

Output:

Training data shape: (455, 30)

Meaning:

455 patients
30 features per patient
print(f'Test data shape: {x_test.shape}')

Output:

Test data shape: (114, 30)
Complete Workflow
Breast Cancer Dataset
        │
        ▼
569 Samples
        │
        ▼
Split Data
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Training     Testing
455             114
 │               │
 ▼               ▼
Fit StandardScaler
 │
 ▼
Transform Training Data
 │
 ▼
Transform Test Data
 │
 ▼
Data Ready for Machine Learning
Expected output
Training data shape: (455, 30)
Test data shape: (114, 30)

At this point, your data is ready to be passed to a machine learning algorithm such as Logistic Regression, SVM, Random Forest, or XGBoost.



'''