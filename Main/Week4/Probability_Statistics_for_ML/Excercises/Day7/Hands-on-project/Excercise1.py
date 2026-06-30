
#Perform Exploratory Data Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

#Inspect Data
print(df.info())
print(df.describe())

#reoves unwanted columns from the datasets
del df['sex']
del df['smoker']
del df['day']
del df['time']

#Visulaize Distributions
sns.histplot(df['total_bill'], kde=True)
plt.title('Distribution fo Total Bill')
plt.show()


#Coreleation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('coorealtion heatmap')
plt.show()


