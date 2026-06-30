#Split Data into Training and Testing Sets

# ----------------------------------------------------
# Import the required libraries
# ----------------------------------------------------

# Pandas is used for loading and manipulating datasets.
import pandas as pd

# train_test_split is used to divide the dataset into
# training and testing sets.
from sklearn.model_selection import train_test_split

# ----------------------------------------------------
# Step 1: Load the dataset
#
# Read the Tips dataset directly from a GitHub URL
# into a Pandas DataFrame.
# ----------------------------------------------------
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

# ----------------------------------------------------
# Step 2: Define the input features (X)
#
# Features are the independent variables used to
# predict the target variable.
#
# Here:
# total_bill = Total restaurant bill
# size       = Number of people in the group
# ----------------------------------------------------
features = df[['total_bill', 'size']]

# ----------------------------------------------------
# Step 3: Define the target variable (y)
#
# The target is the value we want the machine learning
# model to predict.
#
# Here:
# tip = Amount of tip given by the customer
# ----------------------------------------------------
target = df['tip']

# ----------------------------------------------------
# Step 4: Display the first five rows of the
# features and target.
# ----------------------------------------------------
print("Features:\n", features.head())
print("Target:\n", target.head())

# ----------------------------------------------------
# Step 5: Split the dataset into training and testing
# datasets.
#
# train_test_split() divides the data into:
#   x_train -> Training features
#   x_test  -> Testing features
#   y_train -> Training target
#   y_test  -> Testing target
#
# test_size = 0.2
#   → 20% of the data is used for testing.
#
# random_state = 42
#   → Ensures the split is reproducible.
# ----------------------------------------------------
x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------
# Step 6: Display the shape of the training and
# testing datasets.
#
# shape returns:
# (number of rows, number of columns)
# ----------------------------------------------------
print("Training Dataset:", x_train.shape)
print("Testing Dataset:", x_test.shape)

'''
What this program does
Imports the required libraries.
Loads the Tips dataset from GitHub.
Selects total_bill and size as the input features.
Selects tip as the target variable.
Splits the dataset into 80% training data and 20% testing data.
Displays the first few records and the sizes of the training and testing datasets. This is a common preprocessing step before training a machine learning model.
'''