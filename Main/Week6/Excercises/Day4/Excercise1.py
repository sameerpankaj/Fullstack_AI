#Use correlation and mutual infromation to select important features from a dataset

from sklearn.datasets import load_diabetes
import pandas as pd


#Load the dataset
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

#Display Dataset infromation
print(df.head())
print(df.info())