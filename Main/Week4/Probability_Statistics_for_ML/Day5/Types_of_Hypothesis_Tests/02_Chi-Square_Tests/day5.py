from scipy.stats import chi2_contingency

#Contignecy Table
data = [[50, 30], [20, 40]]

#Perform chi-square test
chi2, p, dof, expected = chi2_contingency(data)
print(f'Chi-Square Statistic: \n {chi2}')
print(f'P-Value: \n {p}')
print(f'Expected frequencies: \n {expected}')