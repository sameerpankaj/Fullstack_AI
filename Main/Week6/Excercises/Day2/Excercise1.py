#Apply Min-Max scaling and standarization to a dataset using sckit-learn

from sklearn.datasets import load_iris
import pandas as pd

#Load Iris dataset
data = load_iris()
x = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

#Display dataset information
print('Dataset Info')
print(x.describe())
print('\n Target Classes:', data.target_names)