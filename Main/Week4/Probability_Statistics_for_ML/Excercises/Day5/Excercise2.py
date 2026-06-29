#Perform a Chi Square Test
from scipy.stats import chi2_contingency

#Contingency
data = [[50, 30, 20], [30, 40, 30]]

#Perform chi square test
chi2, p, dof, expected = chi2_contingency(data)
print('Chis square test: \n', chi2)
print('P-values: \n', p)
print('Expected Frequencies: \n', expected)