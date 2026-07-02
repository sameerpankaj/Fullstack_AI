#Plan which feature engineering techniques might be most suitable for the dataset


import pandas as pd

#Load Titanic Dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)


#Seperate features
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['int64', 'Float64']).columns

print('\nCategorical Features: ', categorical_features.tolist())
print('\nNumerical Features: ', numerical_features.tolist())


#Display Summary of Categorical features
print('\n Categorical Feature Summary:\n')
for col in categorical_features:
    print(f'{col}:\n', df[col].value_counts(), '\n')

#Display Summary of Numerical features
print('\n Numerical Feature Summary:\n')
print(df[numerical_features].describe())