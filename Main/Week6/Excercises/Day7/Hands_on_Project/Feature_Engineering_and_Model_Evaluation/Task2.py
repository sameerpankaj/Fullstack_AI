#Task2: Traing and Evaluate Models

# import pandas as pd
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier

# #Load Dataset
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)

# print(df.head())

# #Select relevant features
# #PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# df = df[['PClass', 'Sex', 'Age', 'Fare', 'Survived']]

# #Handle missing values
# # df['Age'].fillna(df['Age'].median(), inplace=True)

# # df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# df.fillna({'Age':df['Age'].median()}, inplace=True)
# df.fillna({'Embarked':df['Embarked'].mode([0])}, inplace=True)

# #Define features and target
# x = df.drop(columns=['Survived'])
# y = df['Survived']

# #Apply feature sclaing and encoding
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', StandardScaler(), ['Age', 'Fare']),
#         ('cat', OneHotEncoder(), ['Pclass', 'Sex', 'Embarked'])
#     ]
# )

# x_preprocessed = preprocessor.fit_transform(x)

# #Train and Evaluate Logistic Regression
# log_model = LogisticRegression()
# log_scores = cross_val_score(log_model, x_preprocessed, y, cv=5, scoring='accuracy')
# print(f'Logisctic Regression Accuracy: {log_scores.mean():.2f}')

# #Train and evaluate Random Froest
# rf_model = RandomForestClassifier(random_state=42)
# rf_scores = cross_val_score(rf_model, x_preprocessed, y, cv=5, scoring='accuracy')
# print(f'Random Forest Accuracy: {rf_scores.mean():.2f}')


import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())

# Select relevant features
df = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Survived']]

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Define features and target
X = df.drop(columns=['Survived'])
y = df['Survived']

# Apply feature scaling and encoding
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'Fare']),
        ('cat', OneHotEncoder(handle_unknown='ignore'),
         ['Pclass', 'Sex', 'Embarked'])
    ]
)

X_preprocessed = preprocessor.fit_transform(X)

# Train and evaluate Logistic Regression
log_model = LogisticRegression(max_iter=1000)

log_scores = cross_val_score(
    log_model,
    X_preprocessed,
    y,
    cv=5,
    scoring='accuracy'
)

print(f'Logistic Regression Accuracy: {log_scores.mean():.2%}')

# Train and evaluate Random Forest
rf_model = RandomForestClassifier(random_state=42)

rf_scores = cross_val_score(
    rf_model,
    X_preprocessed,
    y,
    cv=5,
    scoring='accuracy'
)

print(f'Random Forest Accuracy: {rf_scores.mean():.2%}')