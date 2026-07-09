#get the datasets

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

#Load dataset
data = load_iris()
x, y = data.data, data.target

#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display datasets info
print(f'Feature Names: {data.feature_names}')
print(f'Class Names: {data.target_names}')