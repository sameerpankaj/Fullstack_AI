#Perform T-Test

from scipy.stats import ttest_ind

#sample Datasets
group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.8, 2.0, 2.4, 2.7, 2.9]

#Perform T-Test
t_stat, p_value = ttest_ind(group1, group2)
print(f'T-Statistic: \n {t_stat}')
print(f'P-Value: \n {p_value}')


#Interpretation
alpha = 0.05
if p_value < alpha:
    print('Reject the null hypothesis: significant difference')
else:
    print('Failed to reject the null hypothesis: no significant difference')