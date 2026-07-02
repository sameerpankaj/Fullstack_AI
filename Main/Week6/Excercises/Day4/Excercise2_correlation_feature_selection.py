from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



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
