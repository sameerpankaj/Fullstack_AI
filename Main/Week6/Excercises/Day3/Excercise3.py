# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# #Load Titanic dataset
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)

# #Display dataset information
# print('Dataset Infor:')
# print(df.info())

# #Preview the first few rows
# print('\n Dataset Preview:')
# print(df.head())

# #Apply One Hot encoding
# df_one_hot = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# #Display encoded one hot dataset
# print('\n One Hot Encoded Dataset:')
# print(df_one_hot.head())

# #Apply Label Encoding
# label_encoder = LabelEncoder()
# df['Pclass_encoded'] = label_encoder.fit_transform(df['Pclass'])

# #Display encoded dataset
# print('\n Lable Encoded Dataset:')
# print(df[['Pclass', 'Pclass_encoded']].head())

# #Apply Frequency Encoding
# df['Ticekt_frequency'] = df['Ticket'].map(df['Ticket'].value_counts())

# #Display frequeny encoded feature
# print('\n Frequency Encoded Feature')
# print(df[['Ticket', 'Ticekt_frequency']].head())

# x = df_one_hot.drop(columns=['Survived', 'Name', 'Ticket', 'Cabin'])
# y = df['Survived']

# #Split dataset#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# #Train logistic regression model
# model = LogisticRegression(max_iter=200)
# model.fit(x_train, y_train)

# #Predict and evaluate
# y_pred = model.predict(x_test)
# print('Accuracy with one hot encoding:', accuracy_score(y_test, y_pred))


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ============================================================
# Load Titanic Dataset
# ============================================================
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ============================================================
# Display Dataset Information
# ============================================================
print("Dataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# ============================================================
# Handle Missing Values
# ============================================================

# Fill Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked with most frequent value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin because most values are missing
df = df.drop(columns=["Cabin"])

# ============================================================
# One-Hot Encoding
# ============================================================
df_one_hot = pd.get_dummies(
    df,
    columns=["Sex", "Embarked"],
    drop_first=True
)

print("\nOne-Hot Encoded Dataset:")
print(df_one_hot.head())

# ============================================================
# Label Encoding Example
# ============================================================
label_encoder = LabelEncoder()

df["Pclass_encoded"] = label_encoder.fit_transform(df["Pclass"])

print("\nLabel Encoded Pclass:")
print(df[["Pclass", "Pclass_encoded"]].head())

# ============================================================
# Frequency Encoding Example
# ============================================================
df["Ticket_frequency"] = df["Ticket"].map(df["Ticket"].value_counts())

print("\nFrequency Encoded Ticket:")
print(df[["Ticket", "Ticket_frequency"]].head())

# ============================================================
# Define Features and Target
# ============================================================
X = df_one_hot.drop(
    columns=[
        "Survived",
        "PassengerId",
        "Name",
        "Ticket"
    ]
)

y = df_one_hot["Survived"]

# ============================================================
# Check for Missing Values
# ============================================================
print("\nMissing values after preprocessing:")
print(X.isnull().sum())

# ============================================================
# Split Dataset
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ============================================================
# Train Logistic Regression
# ============================================================
model = LogisticRegression(max_iter=500)

model.fit(X_train, y_train)

# ============================================================
# Prediction
# ============================================================
y_pred = model.predict(X_test)

# ============================================================
# Evaluation
# ============================================================
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))