#Apply Standarization

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
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

#Apply Min Max scaling
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

#Split scaled data
x_train_scaled, x_test_scaled, y_train_scaled, y_test_scaled = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

#Train k-NN on scaled data
knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(x_train_scaled, y_train_scaled)

#Predict and evaluate
y_pred_scaled = knn_scaled.predict(x_test_scaled)
print('Accuracy with Min Max scaling: ', accuracy_score(y_test_scaled, y_pred_scaled))


#Apply Standarization
scaler = StandardScaler()
x_std = scaler.fit_transform(x)

#Split Standarized data
x_train_std, x_test_std, y_train_std, y_test_std = train_test_split(x_std, y, test_size=0.2, random_state=42)

#Train k-NN on Standarized data
knn_std = KNeighborsClassifier(n_neighbors=5)
knn_std.fit(x_train_std, y_train_std)

#Predict and evaluate
y_pred_std = knn_std.predict(x_test_std)
print('Accuracy with Standarization: ', accuracy_score(y_test_std, y_pred_std))