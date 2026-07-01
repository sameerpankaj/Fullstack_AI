

#Task2 : Train and Evaluate Multiple models

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Load Telco Customer Churn Dataset
df_telco = pd.read_csv('Telco-Customer-Churn.csv')

#Inspect Data
print(df_telco.info())
print(df_telco.describe())

#Visualize Churn distribution
sns.countplot(x='Churn', data=df_telco)
plt.title('Churn Distribution')
plt.show()

#Handle the missing values
# df_telco.fillna(df_telco.mean(), inplace=True)

df_telco["TotalCharges"] = pd.to_numeric(
    df_telco["TotalCharges"],
    errors="coerce"
)

numeric_cols = df_telco.select_dtypes(include="number").columns

df_telco[numeric_cols] = df_telco[numeric_cols].fillna(
    df_telco[numeric_cols].mean()
)