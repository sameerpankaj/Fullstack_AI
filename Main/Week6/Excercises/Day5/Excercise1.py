#Create new features from a date column(eg, day of the week , month, year)

# import pandas as pd


# #Load Bike Sharing Dataset
# df = pd.read_csv('bike_sharing_daily.csv')

# #Display dataset information
# print('Dataset Info:')
# print(df.info())

# #Preview the first few rows
# print('\n Dataset Preview:')
# print(df.head)


import pandas as pd
import os

# Get the folder where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the CSV file
csv_path = os.path.join(script_dir, "bike_sharing_daily.csv")

# Load Bike Sharing Dataset
df = pd.read_csv(csv_path)

# Display dataset information
print("Dataset Info:")
df.info()

# Preview the first few rows
print("\nDataset Preview:")
print(df.head())

#Convert dteday to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

#Create new features
df['day_of_week'] = df['dteday'].dt.day_name()
df['month'] = df['dteday'].dt.month
df['year'] = df['dteday'].dt.year

#Display the new features
print('\n New features Derived from Date column')
print(df[['dteday', 'day_of_week', 'month', 'year']].head())