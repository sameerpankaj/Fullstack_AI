from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression



#Load the dataset
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

#Calculate the correlation matrix
corrleation_matrix = df.corr()

#Plot the heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corrleation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

#Select features with high correlation to the target
corrleation_features = corrleation_matrix['target'].sort_values(ascending=False)
print('Features Most correlated with target:')
print(corrleation_features)

#Separate features and target
x = df.drop(columns=['target'])
y = df['target']

#Calculate mutual information
mutual_info = mutual_info_regression(x, y)

#Create a dataframe for better visualization
mi_df = pd.DataFrame({'Feature': x.columns, 'Mutual Information': mutual_info})
mi_df = mi_df.sort_values(by='Mutual Information', ascending=False)

print('Mututal Information Scores:')
print(mi_df)