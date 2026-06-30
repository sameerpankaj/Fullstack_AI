#Conduct Hypothesis Tests

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

#Load Dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

contingency_table = pd.crosstab(df['smoker'], df['time'])

#Perform Ch-Square Test
chi2, p, dof, expected = chi2_contingency(contingency_table)
print('Chi square statistic: ', chi2)
print('P-Value', p)


#Interpret the results
alpha = 0.05
if p <= alpha:
    print('Reject the Null hypothesis: variables are dependent')
else:
    print('Fail to reject the null hypothesis: variables are independent ')



