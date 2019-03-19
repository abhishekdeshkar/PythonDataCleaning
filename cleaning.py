import pandas as pd

data = pd.read_csv("data.csv")

#Counts total null values.
x1 = data['x1'].isnull().sum()
x2 = data['x2'].isnull().sum()
x3 = data['x3'].isnull().sum()
x4 = data['x4'].isnull().sum()
x5 = data['x5'].isnull().sum()

print(x5)