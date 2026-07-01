



#Task2 : Train and Evaluate Multiple models

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report, confusion_matrix

# #Load Telco Customer Churn Dataset
# df_telco = pd.read_csv('Telco-Customer-Churn.csv')

# #Encode Categorical variables
# le = LabelEncoder()
# df_telco['Churn'] = le.fit_transform(df_telco['Churn'])

# #Define features and target
# x = df_telco.drop(columns=['Churn'])
# y = df_telco['Churn']

# #Scale Features
# scaler = StandardScaler()
# x = scaler.fit_transform(x)

# #Split Dataset
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# #Train Logisitc regression model
# log_model = LogisticRegression(max_iter=200)
# log_model.fit(x_train, y_train)

# #Train k-NN model
# knn_model = KNeighborsClassifier(n_neighbors=5)
# knn_model.fit(x_train, y_train)

# #Evaluate models
# log_pred = log_model.predict(x_test)
# knn_pred = knn_model.predict(x_test)

# print('\n Logistic Regression Classfication report:')
# print(classification_report(y_test, log_pred))

# print('\n k-NN  Classfication report:')
# print(classification_report(y_test, knn_pred))

# #Confusion metics for logistic regression
# print('Confusion Matrix: \n', confusion_matrix(y_test, log_pred))


# #Inspect Data
# print(df_telco.info())
# print(df_telco.describe())

# #Visualize Churn distribution
# sns.countplot(x='Churn', data=df_telco)
# plt.title('Churn Distribution')
# plt.show()

# #Handle the missing values
# # df_telco.fillna(df_telco.mean(), inplace=True)

# df_telco["TotalCharges"] = pd.to_numeric(
#     df_telco["TotalCharges"],
#     errors="coerce"
# )

# numeric_cols = df_telco.select_dtypes(include="number").columns

# df_telco[numeric_cols] = df_telco[numeric_cols].fillna(
#     df_telco[numeric_cols].mean()
# )





import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ============================================================
# Step 1: Load Dataset
# ============================================================
df = pd.read_csv("Telco-Customer-Churn.csv")

# ============================================================
# Step 2: Inspect Dataset
# ============================================================
print(df.head())
print(df.info())
print(df.isnull().sum())

# ============================================================
# Step 3: Convert TotalCharges to numeric
# (Blank values become NaN)
# ============================================================
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values with the column mean
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].mean())

# ============================================================
# Step 4: Encode Target Variable
# ============================================================
le = LabelEncoder()
df["Churn"] = le.fit_transform(df["Churn"])

# ============================================================
# Step 5: Define Features and Target
# Remove customerID because it is only an identifier
# ============================================================
X = df.drop(columns=["customerID", "Churn"])
y = df["Churn"]

# ============================================================
# Step 6: Convert Categorical Features
# ============================================================
X = pd.get_dummies(X, drop_first=True)

print("\nShape after encoding:", X.shape)

# ============================================================
# Step 7: Split Dataset
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================================
# Step 8: Scale Features
# IMPORTANT:
# Fit only on training data
# ============================================================
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================================================
# Step 9: Train Logistic Regression
# ============================================================
log_model = LogisticRegression(max_iter=300)
log_model.fit(X_train, y_train)

# ============================================================
# Step 10: Train KNN
# ============================================================
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# ============================================================
# Step 11: Predictions
# ============================================================
log_pred = log_model.predict(X_test)
knn_pred = knn_model.predict(X_test)

# ============================================================
# Step 12: Evaluation
# ============================================================
print("\n========== Logistic Regression ==========")
print(classification_report(y_test, log_pred))
print(confusion_matrix(y_test, log_pred))

print("\n========== KNN ==========")
print(classification_report(y_test, knn_pred))
print(confusion_matrix(y_test, knn_pred))