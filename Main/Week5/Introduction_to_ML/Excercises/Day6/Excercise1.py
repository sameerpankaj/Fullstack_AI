#Implement k-NN for a classfication task, experimenting with different values of k

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

#Load Iris dataset
data = load_iris()
x, y = data.data, data.target

#Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Scale features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Experiment with different values of k
for k in range(1, 11):
    #Initialize k-NN model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    #Predict on test data
    y_pred = knn.predict(x_test)

    #Evaluate performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f'k = {k}, Accuracy = {accuracy:.2f}')