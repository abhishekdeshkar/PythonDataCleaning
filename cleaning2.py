import pandas as pd

data = pd.DataFrame({'k1' : ['one','two'] * 3 + ['two'],
                    'k2' : [1,1,2,3,3,4,4]})
# print(data)

#=========Prints duplicate values.==============
#print(data.duplicated())

#=========Drops Duplicate values.=========
#print(data.drop_duplicates())
#By column
#print(data.drop_duplicates('k2'))