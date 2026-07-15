#Load and explore dataset 

import pandas as pd

#Load dataset
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
df = pd.read_csv(url)

#Display data
print('Dataset info:\n')
print(df.info)
print('\n Class Distribution:\n')
print(df['Class'].value_counts())