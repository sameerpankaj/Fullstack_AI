import numpy as np
from scipy.stats import pearsonr, spearmanr

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

#Pearson Correlation
r, _= pearsonr(x, y)
print('Pearson Correlatoin Coefficient: \n', r)

#Spearman Correlation
rho, _= spearmanr(x, y)
print('Spearman Correlation Cofficient: \n', rho)