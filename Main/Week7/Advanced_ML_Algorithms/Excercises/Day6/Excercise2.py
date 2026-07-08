#Train a classifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #needed to train a classfier
from sklearn.metrics import classification_report, roc_auc_score 

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

#Train Random Forest
rf_model = RandomForestClassifier(random_state=42, class_weight='balanced')
rf_model.fit(x_train, y_train)

#Predict and evaluate
y_pred = rf_model.predict(x_test)
print('\n Classficiation Report:\n')
print(classification_report(y_test, y_pred))

roc_auc = roc_auc_score(y_test, rf_model.predict_proba(x_test)[:,1])
print(f'ROC-AUC: {roc_auc:.2f}')


'''
This program builds a Random Forest model to detect fraudulent credit card transactions. Let's go through it step by step.

Step 1: Import libraries
import pandas as pd

Used to read and manipulate the dataset.

from sklearn.model_selection import train_test_split

Splits the dataset into:

Training data (80%)
Testing data (20%)
from sklearn.ensemble import RandomForestClassifier

Imports the Random Forest classification algorithm.

from sklearn.metrics import classification_report, roc_auc_score

Used to evaluate the model.

classification_report() shows Precision, Recall, F1-score, and Accuracy.
roc_auc_score() measures how well the model distinguishes fraud from non-fraud.
Step 2: Load the dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

Downloads and loads the dataset into a Pandas DataFrame.

Example:

Time	V1	V2	...	Amount	Class
0	...	...	...	149.62	0
1	...	...	...	2.69	1

The Class column is the target:

0 → Normal transaction
1 → Fraud transaction
Step 3: Explore the dataset
print(df.info())

Displays information like:

Number of rows
Number of columns
Data types
Missing values

Example:

RangeIndex: 284807 entries

Data columns (31 columns)

Time float64
V1 float64
...
Class int64
print(df['Class'].value_counts())

Counts how many transactions belong to each class.

Example:

0    284315
1       492

This shows the dataset is highly imbalanced.

Approximately:

99.83% normal
0.17% fraud
Step 4: Split features and target
x = df.drop(columns=['Class'])

Creates the feature matrix.

Everything except the target column becomes an input feature.

Features include:

Time
V1
V2
...
Amount
y = df['Class']

Creates the target vector.

0
0
0
1
...
Step 5: Split training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

Splits the data.

80% → Training

20% → Testing

The training data is used to build the model.

The testing data evaluates its performance on unseen data.

Better practice for this dataset: Use stratify=y to preserve the class distribution:

train_test_split(
    x, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
Step 6: Create the Random Forest
rf_model = RandomForestClassifier(
    random_state=42,
    class_weight='balanced'
)

Creates the model.

random_state=42

Ensures reproducible results.

class_weight='balanced'

This is very important.

Since fraud cases are rare, the algorithm gives them higher importance.

Without balancing:

Normal = 284315

Fraud = 492

The model might predict:

Everything = Normal

and still achieve 99.8% accuracy, while missing almost all fraud.

class_weight='balanced' increases the penalty for misclassifying fraud.

Step 7: Train the model
rf_model.fit(x_train, y_train)

The Random Forest learns patterns from the training data.

It builds many decision trees.

Example:

Tree 1

Tree 2

Tree 3

...

Tree 100

Each tree votes.

Majority vote becomes the final prediction.

Step 8: Make predictions
y_pred = rf_model.predict(x_test)

Predicts:

0
0
1
0
...

for every transaction in the test set.

Step 9: Classification report
print(classification_report(y_test, y_pred))

Produces something like:

              precision recall f1-score support

0             1.00      1.00     1.00   56864

1             0.92      0.84     0.88      98
Precision

Of all predicted frauds,

How many were actually fraud?

Precision = TP / (TP + FP)

Higher precision = fewer false alarms.

Recall

Of all actual frauds,

How many were detected?

Recall = TP / (TP + FN)

For fraud detection,

Recall is often the most important metric, because missing a fraudulent transaction can be costly.

F1-score

Balances precision and recall.

F1 = 2 × (Precision × Recall)
     ------------------------
     Precision + Recall
Step 10: ROC-AUC
roc_auc = roc_auc_score(
    y_test,
    rf_model.predict_proba(x_test)[:,1]
)
predict_proba()

Returns probabilities instead of class labels.

Example:

[
 [0.98,0.02],
 [0.10,0.90],
 [0.75,0.25]
]

Each row is:

Probability of Class 0

Probability of Class 1
[:,1]

Selects only the fraud probability.

Example:

0.02

0.90

0.25

These probabilities are used to compute the ROC-AUC score.

Print ROC-AUC
print(f'ROC-AUC: {roc_auc:.2f}')

Example:

ROC-AUC: 0.99

Interpretation:

1.0 → Perfect classifier
0.9–1.0 → Excellent
0.8–0.9 → Good
0.5 → Random guessing

For imbalanced datasets like fraud detection, ROC-AUC is a more informative metric than accuracy, because it evaluates how well the model separates fraud from non-fraud across different classification thresholds.

'''



