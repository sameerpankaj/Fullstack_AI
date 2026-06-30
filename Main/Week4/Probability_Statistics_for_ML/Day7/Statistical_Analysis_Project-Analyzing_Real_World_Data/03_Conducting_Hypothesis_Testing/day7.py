from scipy.stats import ttest_ind
import pandas as pd

#Load Dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

#Separate data by gender
male_tips = df[df['sex'] == 'Male']['tip']
female_tips = df[df['sex'] == 'Female']['tip']


#Perfrom t-test
t_stat, p_value = ttest_ind(male_tips, female_tips)
print('T-statistic: ', t_stat)
print('P-Value: ', p_value)


#Interpret Results
alpha = 0.05
if p_value <= alpha:
    print('Reject all null hypothesis: Significant difference')
else:
    print('Fail to reject all null hypothesis: No significant difference')

    