#Experiment with different encoding techniques and observe their impact on model performance

import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

#Display dataset information
print('Dataset Infor:')
print(df.info())

#Preview the first few rows
print('\n Dataset Preview:')
print(df.head())

#Apply One Hot encoding
df_one_hot = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

#Display encoded one hot dataset
print('\n One Hot Encoded Dataset:')
print(df_one_hot.head())

#Apply Label Encoding
label_encoder = LabelEncoder()
df['Pclass_encoded'] = label_encoder.fit_transform(df['Pclass'])

#Display encoded dataset
print('\n Lable Encoded Dataset:')
print(df[['Pclass', 'Pclass_encoded']].head())

#Apply Frequency Encoding
df['Ticekt_frequency'] = df['Ticket'].map(df['Ticket'].value_counts())

#Display frequeny encoded feature
print('\n Frequency Encoded Feature')
print(df[['Ticket', 'Ticekt_frequency']].head())