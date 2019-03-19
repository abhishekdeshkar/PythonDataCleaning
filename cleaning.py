import pandas as pd

#Identifying NULL values.
missing_values = ["Na","==","nA","NA"]

data = pd.read_csv("data.csv",na_values=missing_values)

#print(data)

#Counts total null values.
x1 = data['x1'].isnull().sum()
x2 = data['x2'].isnull().sum()
x3 = data['x3'].isnull().sum()
x4 = data['x4'].isnull().sum()
x5 = data['x5'].isnull().sum()

#Type of x3 column. int64
print(data['x3'].dtype)

#If there are any null values in data frame.
print(data.isnull().values.any())