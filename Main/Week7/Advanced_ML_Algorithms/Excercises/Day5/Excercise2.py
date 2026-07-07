import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import lightgbm as lgb
from sklearn.metrics import accuracy_score

#Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

#Select features and target
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
target = 'Survived'

#Handle missing values
df.fillna({'Age': df['Age'].median()}, inplace=True)
df.fillna({'Embarked': df['Embarked'].mode()[0]}, inplace=True)

#Encode categorical variables
label_encoders = {}
for col in ['Sex', 'Embarked']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    
#Split Data
x = df[features]
y = df[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f'Training Data Shape: {x_train.shape}')
print(f'Test Data Shape: {x_test.shape}')

#Train LightGBM model
lgb_model = lgb.LGBMClassifier()
lgb_model.fit(x_train, y_train)

#Predict and values
lgb_pred = lgb_model.predict(x_test)
print(f'LightGBM Accuracy: {accuracy_score(y_test, lgb_pred):.4f}')

