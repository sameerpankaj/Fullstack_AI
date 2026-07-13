#Load and explore the dataset
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd

#Load dataset
california = fetch_california_housing()
x, y = california.data, california.target
feature_names = california.feature_names

#split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset info
print('Feature names:\n', feature_names)
print('\n Sample Data:\n', pd.DataFrame(x, columns=feature_names).head())





'''
This program loads the California Housing dataset, splits it into training and testing sets, and displays the feature names and a few sample rows. It is commonly used for regression problems because the target is a continuous house price, not a category.

Let's go through it line by line.

1. Import Libraries
from sklearn.datasets import fetch_california_housing
sklearn.datasets

This module provides built-in datasets for machine learning.

Examples include:

load_iris()
load_breast_cancer()
load_wine()
fetch_california_housing()

Unlike load_* datasets, fetch_california_housing() downloads the dataset (the first time) and then stores it locally for future use.

from sklearn.model_selection import train_test_split

This function splits the dataset into:

Training data
Testing data

This allows you to train a model on one part of the data and evaluate it on unseen data.

import pandas as pd

Pandas is a library for data manipulation.

It provides the DataFrame, which looks like an Excel spreadsheet.

Example:

Age	Salary
25	30000
30	45000
2. Load Dataset
california = fetch_california_housing()

This downloads and loads the California Housing dataset.

The returned object contains:

california.data

Input features.

california.target

Target values.

california.feature_names

Names of all input features.

You can inspect its contents:

print(california.keys())

Output:

dict_keys([
'data',
'target',
'feature_names',
'DESCR'
])
3. Separate Features and Target
x, y = california.data, california.target
x

Independent variables (features).

Shape:

20640 × 8

Meaning:

20,640 houses
8 features for each house
y

Target variable.

Shape:

20640

Each value represents the median house value (in units of $100,000).

For example:

4.526

means approximately:

$452,600
4. Store Feature Names
feature_names = california.feature_names

This stores:

[
'MedInc',
'HouseAge',
'AveRooms',
'AveBedrms',
'Population',
'AveOccup',
'Latitude',
'Longitude'
]
Meaning of each feature
Feature	Description
MedInc	Median income in the area
HouseAge	Average age of houses
AveRooms	Average number of rooms
AveBedrms	Average number of bedrooms
Population	Population of the area
AveOccup	Average occupants per household
Latitude	Latitude of the house
Longitude	Longitude of the house
5. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

This divides the dataset into training and testing sets.

Since there are 20,640 samples:

Training (80%)

16,512 samples
Testing (20%)

4,128 samples
random_state=42

Ensures the split is reproducible.

Without it, each run would produce a different split.

6. Print Feature Names
print('Feature names:\n', feature_names)

Output:

Feature names:

['MedInc',
 'HouseAge',
 'AveRooms',
 'AveBedrms',
 'Population',
 'AveOccup',
 'Latitude',
 'Longitude']
7. Convert to DataFrame
pd.DataFrame(
    x,
    columns=feature_names
)

This converts the NumPy array into a labeled table.

Without a DataFrame:

[[8.3252 41.0 6.98 ...]]

With a DataFrame:

MedInc	HouseAge	AveRooms	AveBedrms	Population	AveOccup	Latitude	Longitude
8.3252	41	6.98	1.02	322	2.56	37.88	-122.23

The column names make the data much easier to understand.

8. .head()
.head()

Returns the first five rows of the DataFrame.

Example:

MedInc	HouseAge	AveRooms	AveBedrms	Population	AveOccup	Latitude	Longitude
8.3252	41	6.98	1.02	322	2.56	37.88	-122.23
8.30	21	6.24	0.97	2401	2.10	37.86	-122.22
...	...	...	...	...	...	...	...
Workflow of the program
California Housing Dataset
           │
           ▼
Load Dataset
           │
           ▼
Separate Features (X) and Target (y)
           │
           ▼
Split into Training and Test Sets
           │
           ▼
Display Feature Names
           │
           ▼
Convert Data to Pandas DataFrame
           │
           ▼
Display First 5 Rows
Expected output
Feature names:
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
 'Population', 'AveOccup', 'Latitude', 'Longitude']

Sample Data:
   MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude
0  8.3252       41.0      6.98       1.02         322       2.56      37.88    -122.23
1  ...
What this program does
Loads the California Housing dataset.
Separates features (x) and target (y).
Splits the data into training and testing sets.
Displays the feature names.
Shows the first five rows in a readable table using Pandas.

This is a typical first step before training a regression model such as Linear Regression, Decision Tree Regressor, Random Forest Regressor, or XGBoost Regressor.

'''