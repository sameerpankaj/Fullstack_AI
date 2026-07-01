#Compare k_NN results to logistic regression, analyzing accuracy and other metrics



from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

#Load Iris dataset
data = load_iris()
x, y = data.data, data.target

#Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


#Scale features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Train Logistic Regression model
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(x_train, y_train)

#Predict using logistic regression
y_pred_lr = log_reg.predict(x_test)

#Evaluate logisitic regression
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print('logistic regressin accuracy is: ', accuracy_lr)

#Evaluate k-NN
best_k = 5
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f'k-NN Accuracy k={best_k}: ', accuracy_knn)

#Detailed Comparision
print('\n Logisitc Regression Classification Report: ')
print(classification_report(y_test, y_pred_lr))

print('\n k-NN Regression Classification Report: ')
print(classification_report(y_test, y_pred_knn))





# #Experiment with different values of k
# for k in range(1, 11):
#     #Initialize k-NN model
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(x_train, y_train)

#     #Predict on test data
#     y_pred = knn.predict(x_test)

#     #Evaluate performance
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f'k = {k}, Accuracy = {accuracy:.2f}')