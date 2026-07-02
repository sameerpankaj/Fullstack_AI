from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.ensemble import RandomForestRegressor
import numpy as np



#Load the dataset
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

#Calculate the correlation matrix
corrleation_matrix = df.corr()

#Plot the heatmap
# plt.figure(figsize=(10,8))
# sns.heatmap(corrleation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()

#Select features with high correlation to the target
corrleation_features = corrleation_matrix['target'].sort_values(ascending=False)
# print('Features Most correlated with target:')
# print(corrleation_features)

#Separate features and target
x = df.drop(columns=['target'])
y = df['target']

#Calculate mutual information
mutual_info = mutual_info_regression(x, y)

#Create a dataframe for better visualization
mi_df = pd.DataFrame({'Feature': x.columns, 'Mutual Information': mutual_info})
mi_df = mi_df.sort_values(by='Mutual Information', ascending=False)

# print('Mututal Information Scores:')
# print(mi_df)

#Train a Random Forest Model
model = RandomForestRegressor(random_state=42)
model.fit(x, y)

#Get Feature importance
feature_importance = model.feature_importances_
imporance_df = pd.DataFrame({'Feature': x.columns, 'Importance': feature_importance})
imporance_df = imporance_df.sort_values(by='Importance', ascending=False)

print('Feature importance from random forest')
print(imporance_df)

#Plot features importance
plt.figure(figsize=(10,6))
plt.barh(imporance_df['Feature'], imporance_df['Importance'])
plt.title('Feature Importance from Random Forest')
plt.show()

