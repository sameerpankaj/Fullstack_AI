#Analyze a Datasets Distribution

#url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Data set
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

#Analyse sepal_length
feature = df['sepal_length']
print(f'Skewness: \n {skew(feature)}')
print(f'Kurtosis: \n {kurtosis(feature)}')

#Visualize Distribution
sns.histplot(feature, kde=True)
plt.title('Distribution of Sepal Length')
plt.show()