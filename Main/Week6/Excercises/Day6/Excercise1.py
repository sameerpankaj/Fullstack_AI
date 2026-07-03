# Excercise 1: Classfication Model Evaluation
#     Objective:
#         Train a classfication model, calculate confusion matrix, and interpret precision, recall and F1 score


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Load Dataset
data = load_iris()
x = data.data
y = (data.target == 0).astype(int)

#Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Train logistic regression model
model = LogisticRegression()
model.fit(x_train, y_train)

#Predict
y_predict = model.predict(x_test)

#Confusion Matrix
cm = confusion_matrix(y_test, y_predict)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Class 0', 'Class 0'])
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

#Classfication metrics
print('\n Classifciation Report')
print(classification_report(y_test, y_predict))


