#Task1: Perform Feature Engineering

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

#Load Dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

print(df.head())

#Select relevant features
#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
df = df[['PClass', 'Sex', 'Age', 'Fare', 'Survived']]

#Handle missing values
# df['Age'].fillna(df['Age'].median(), inplace=True)

# df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.fillna({'Age':df['Age'].median()}, inplace=True)
df.fillna({'Embarked':df['Embarked'].mode([0])}, inplace=True)

#Define features and target
x = df.drop(columns=['Survived'])
y = df['Survived']

#Apply feature sclaing and encoding
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'Fare']),
        ('cat', OneHotEncoder(), ['Pclass', 'Sex', 'Embarked'])
    ]
)

x_preprocessed = preprocessor.fit_transform(x)