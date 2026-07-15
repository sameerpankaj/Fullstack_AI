#Load dataset

import pandas as pd

#Losd dataset
df = pd.read_csv('Telco-Customer-Churn.csv')

#Display dataset info
print('Dataset Info:\n')
print(df.info())
print('\n Class Distributions: \n')
print(df['Churn'].value_counts())
print('\n Sample Data: \n', df.head())