# url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

import pandas as pd

#Load Dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

#Define features and target
features = df[['total_bill', 'size']]
target = df['tip']

print('Features: \n', features.head())
print('Target: \n', target.head())