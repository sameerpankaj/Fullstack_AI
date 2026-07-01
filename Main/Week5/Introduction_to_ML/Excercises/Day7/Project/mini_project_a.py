
#Train and evaluate multiple models
#Task1 : Perform Exploratory Data Analysis and preporcessing


import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



#Load Dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

#Define Features and targets
x = df[['MedInc', 'HouseAge', 'AveRooms']]
y = df['MedHouseVal']

# #Inspect Data
# print(df.info())
# print(df.describe())

# #Visualize relationships
# sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
# plt.show()

# #Check for missing values
# print('Missing values: \n', df.isnull().sum())

#Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Train the Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)

#Make Predictions
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print('Linear Regession MSE: ', mse)



