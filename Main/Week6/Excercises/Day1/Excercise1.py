#Load a dataset and explore its features, identifying categorical and numerical features

import pandas as pd

#Load Titanic Dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

#Display dataset information
print('Dataset Infor: \n')
print(df.info())

#Preview the first few rows
print('\n Dataset Preview: \n')
print(df.head())

#Seperate features
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['int64', 'Float64']).columns

print('\nCategorical Features: ', categorical_features.tolist())
print('\nNumerical Features: ', numerical_features.tolist())

