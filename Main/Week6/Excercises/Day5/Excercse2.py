import pandas as pd
import os
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Get the folder where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the CSV file
csv_path = os.path.join(script_dir, "bike_sharing_daily.csv")

# Load Bike Sharing Dataset
df = pd.read_csv(csv_path)

# Display dataset information
# print("Dataset Info:")
# df.info()

# Preview the first few rows
# print("\nDataset Preview:")
# print(df.head())

#Convert dteday to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

#Create new features
df['day_of_week'] = df['dteday'].dt.day_name()
df['month'] = df['dteday'].dt.month
df['year'] = df['dteday'].dt.year

#Display the new features
# print('\n New features Derived from Date column')
# print(df[['dteday', 'day_of_week', 'month', 'year']].head())

#Select Feature and Target
x = df[['temp']]
y = df[['cnt']]

#Apply polynomial transformation
poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x)

#Display the transormed feature
# print('\n Original and Polynomial features')
# print(pd.DataFrame(x_poly, columns=['temp', 'temp^2']).head())

#Split the Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_poly_train, x_poly_test = train_test_split(x_poly, test_size=0.2, random_state=42)

#Train and evaluate model with original features
model_original = LinearRegression()
model_original.fit(x_train, y_train)
y_pred_original = model_original.predict(x_test)
mse_original = mean_squared_error(y_test, y_pred_original)

#Train and evaluate model with polynomial features
model_poly = LinearRegression()
model_poly.fit(x_poly_train, y_train)
y_pred_poly = model_poly.predict(x_poly_test)
mse_poly = mean_squared_error(y_test, y_pred_poly)

#Compare results
print(f'MSE original: {mse_original:.2f}')
print(f'MSE Polynomial: {mse_poly:.2f}')





