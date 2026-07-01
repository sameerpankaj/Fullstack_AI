#Genearte and interpret confusion matrix for a classfication model
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import train_test_split


#Load datasets
data = load_iris()
x, y = data.data, data.target

#Load Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


#Train logistic regression
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)

#Predict on test data
y_pred = model.predict(x_test)

#Generate the confuion matrix
cm = confusion_matrix(y_test, y_pred)

#Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.show()

#Print Classficition Report
print('\nClassfication Report:\n', classification_report(y_test, y_pred))