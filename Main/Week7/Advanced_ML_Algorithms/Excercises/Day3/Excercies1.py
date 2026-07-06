from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#Load dataset
data = load_breast_cancer()
x, y = data.data, data.target

#Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Display dataset information
print(f'Features: {data.feature_names}')
print(f'Classes: {data.target_names}')


