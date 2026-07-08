import pandas as pd
from sklearn.model_selection import train_test_split

#Load Dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

#Explore dataset
print('Dataset Info: \n')
print(df.info())
print('\n Class Distribution:\n')
print(df['Class'].value_counts())

#Split Dataset
x = df.drop(columns=['Class'])
y = df['Class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)




'''

Yes. Your code is correct and will run successfully if you have an internet connection. Here's what it does:

import pandas as pd
from sklearn.model_selection import train_test_split

# Load Dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

# Explore dataset
print('Dataset Info:\n')
print(df.info())

print('\nClass Distribution:\n')
print(df['Class'].value_counts())

# Split Dataset
X = df.drop(columns=['Class'])
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
One improvement

This is an imbalanced dataset (very few fraud cases compared to normal transactions). When splitting, you should use stratified sampling to maintain the same class distribution in both the training and test sets.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
Why use stratify=y?

Suppose your dataset has:

Normal transactions (Class = 0): 99.8%
Fraud transactions (Class = 1): 0.2%

Without stratify=y, the split might accidentally place too few fraud cases in the test set.

With stratify=y, both sets keep approximately the same proportions.

Expected output
Dataset Info:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 284807 entries
Data columns (total 31 columns):
...

Class Distribution:

0    284315
1       492
Name: Class, dtype: int64
Best practice

For this dataset, the recommended split is:

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

This preserves the class balance and is the approach commonly used for fraud detection problems.

'''