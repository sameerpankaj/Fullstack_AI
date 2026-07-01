#Task1 : Perform Exploratory Data Analysis and preporcessing

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing



#Load Dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

x = df[['MedInc', 'HouseAge', 'AveRooms']]
y = df['MedHouseVal']

#Inspect Data
print(df.info())
print(df.describe())

#Visualize relationships
sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
plt.show()

#Check for missing values
print('Missing values: \n', df.isnull().sum())

