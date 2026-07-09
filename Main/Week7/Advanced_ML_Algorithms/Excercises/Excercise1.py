import pandas as pd

#Load Dataset
df = pd.read_csv('Telco-Customer-Churn.csv')

#Display dataset information and preview
print('Dataset Info: \n')
print(df.info())
print('\n Class Distribution')
print(df['Churn'].value_counts())
print('n\ Sample Data: \n', df.head())