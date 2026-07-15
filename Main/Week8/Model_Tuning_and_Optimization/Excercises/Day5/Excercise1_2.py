#Prepare the data

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier


#Load dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

#Display data
print('Dataset info:\n')
df.info()
print('\n Class Distribution:\n')
print(df['Class'].value_counts())

#Define features and target
x = df.drop(columns=['Class'])
y = df['Class']

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Initialize K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

#Train and evaluate model
rf_model = RandomForestClassifier(random_state=42)
scores_kfold = cross_val_score(rf_model, x_train, y_train, cv=kf, scoring='accuracy')

print(f'K-fold cross validation score: {scores_kfold}')
print(f'Mean Accuracy (K-fold): {scores_kfold.mean():.2f}')

#Initialize Stratified kfold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

#Train and evaluate model
scores_stratified = cross_val_score(rf_model, x_train, y_train, cv=skf, scoring='accuracy')

print(f'Stratified K-fold corss validation scores: {scores_stratified}')
print(f'Mean Accuracy (Starfified K-fold): {scores_stratified.mean():.2f}')


