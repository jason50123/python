import pandas as pd
# import numpy as np

df = pd.read_csv('diamonds.csv')

print(df)
print("===================")

# Age_mean = df.Age.mean()
# df.Age[df.Age.isnull()]=Age_mean

# Salary_mean = df.Salary.mean()
# df.Salary[df.Salary.isnull()]=Salary_mean


df.dropna(axis=0, how='any', inplace=True)
print(df)

df.to_excel('newData.xls',sheet_name='data')
