#Generate and filter a random dataset

import numpy as np


#Generate random dataset
dataset = np.random.randint(1, 51, size=(5, 5))
print(f'Original: \n {dataset}')


#filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print(f'Modified Dataset: \n {dataset}')


#Calculate summary stats
print(f'Sum: \n {np.sum(dataset)}')
print(f'Mean : \n {np.mean(dataset)}')
print(f'Standard Deviation : \n {np.std(dataset)}')