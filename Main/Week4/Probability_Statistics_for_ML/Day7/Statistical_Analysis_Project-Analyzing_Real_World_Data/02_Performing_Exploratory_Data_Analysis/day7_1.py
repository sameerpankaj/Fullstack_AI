# url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

#Inspect Data
print(df.info())
print(df.describe())

#Visulaize Distributions
sns.histplot(df['total_bill'], kde=True)
plt.title('Distribution fo Total Bill')
plt.show()

