#train data without scaling

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

#Load Iris dataset
data = load_iris()
x = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

#Display dataset information
print('Dataset Info')
print(x.describe())
print('\n Target Classes:', data.target_names)

#Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Traing k-NN classfier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

#Predict and evaluate
y_pred = knn.predict(x_test)
print('Accuracy without scaling: ', accuracy_score(y_test, y_pred))