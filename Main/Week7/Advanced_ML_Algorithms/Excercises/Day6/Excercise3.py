#Ápply SMOTE

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #needed to train a classfier
from sklearn.metrics import classification_report, roc_auc_score 
from imblearn.over_sampling import SMOTE

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

#Apply SMOTE
smote = SMOTE(random_state=42)
x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

#Display new class distribution
print('\n Class Distribution After SMOTE \n')
print(pd.Series(y_resampled).value_counts)

'''
This program trains a Random Forest model for credit card fraud detection and then uses SMOTE to balance the training data. Let's go through it step by step.

Step 1: Import libraries
import pandas as pd

Imports Pandas, which is used to load and manipulate datasets.

from sklearn.model_selection import train_test_split

Splits the dataset into:

Training data (80%)
Testing data (20%)
from sklearn.ensemble import RandomForestClassifier

Imports the Random Forest classification algorithm.

from sklearn.metrics import classification_report, roc_auc_score

Imports evaluation metrics:

classification_report() → Precision, Recall, F1-score
roc_auc_score() → Measures how well the model separates fraud from non-fraud.
from imblearn.over_sampling import SMOTE

Imports SMOTE (Synthetic Minority Oversampling Technique).

SMOTE creates synthetic fraud examples to balance the dataset.

Step 2: Load the dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

Loads the credit card fraud dataset.

Example:

Time	V1	V2	Amount	Class
0	...	...	149.62	0
1	...	...	2.69	1

Target column:

0 = Normal
1 = Fraud
Step 3: Explore the dataset
print(df.info())

Shows:

Number of rows
Number of columns
Data types
Missing values
print(df['Class'].value_counts())

Shows class distribution.

Example:

0    284315
1       492

This means the dataset is highly imbalanced.

Step 4: Separate features and target
x = df.drop(columns=['Class'])

Stores all input features.

y = df['Class']

Stores the target labels.

Step 5: Split into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

Creates

80% training
20% testing

Better practice:

train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)
Step 6: Train Random Forest
rf_model = RandomForestClassifier(
    random_state=42,
    class_weight='balanced'
)

Creates the classifier.

class_weight='balanced'

Because fraud cases are very rare, the algorithm automatically assigns a higher weight to fraud transactions.

Without this, the model may ignore fraud.

rf_model.fit(x_train, y_train)

Trains the Random Forest on the training data.

Step 7: Predict
y_pred = rf_model.predict(x_test)

Predicts whether each transaction is:

0 → Normal
1 → Fraud
Step 8: Classification Report
print(classification_report(y_test, y_pred))

Outputs something like:

              precision    recall   f1-score

0             1.00        1.00      1.00
1             0.91        0.86      0.88
Precision

Of all predicted fraud transactions,

how many were actually fraud?

Recall

Of all actual fraud transactions,

how many did the model detect?

F1-score

Balances precision and recall.

Step 9: ROC-AUC
roc_auc = roc_auc_score(
    y_test,
    rf_model.predict_proba(x_test)[:,1]
)
predict_proba()

Returns probabilities.

Example:

[
 [0.99,0.01],
 [0.20,0.80],
 [0.70,0.30]
]

Column 0

Probability of Normal

Column 1

Probability of Fraud

[:,1]

Extracts only the fraud probabilities.

These probabilities are used to calculate ROC-AUC.

Step 10: Apply SMOTE
smote = SMOTE(random_state=42)

Creates a SMOTE object.

x_resampled, y_resampled = smote.fit_resample(
    x_train,
    y_train
)

This is the most important part.

Suppose the original training data is:

Normal : 227451

Fraud  : 394

SMOTE creates synthetic fraud samples until both classes have the same number of examples.

After SMOTE:

Normal : 227451

Fraud  : 227451

The dataset is now balanced.

How does SMOTE create new samples?

Suppose we have fraud points:

Fraud A

Fraud B

Instead of duplicating A or B,

SMOTE creates a new point between them.

A -------- New Sample -------- B

This gives the model more varied fraud examples to learn from.

Step 11: Display new class distribution
print(pd.Series(y_resampled).value_counts())

Expected output:

0    227451

1    227451

This confirms that SMOTE successfully balanced the classes.

Bug in your code: You wrote:

print(pd.Series(y_resampled).value_counts)

This prints the function object, not the counts.

Correct:

print(pd.Series(y_resampled).value_counts())

Notice the parentheses ().

Important note

Your code applies SMOTE after training the Random Forest, so the resampled data is not used by the model.

If your goal is to train on balanced data, the correct order is:

# Split
X_train, X_test, y_train, y_test = train_test_split(...)

# Apply SMOTE ONLY on the training set
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train on the resampled data
rf_model.fit(X_train_resampled, y_train_resampled)

# Evaluate on the original test set
y_pred = rf_model.predict(X_test)

This avoids data leakage and lets the model learn from the balanced training data while still being evaluated on real-world, imbalanced test data.


'''