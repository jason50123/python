# from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_excel('newData.xls')
(train_data, test_data) = train_test_split(data, test_size = 0.3)
print('total:' ,len(data),
     'train', len(train_data),
     'test', len(test_data))

train_data.to_excel('train_data.xls',sheet_name='data')
test_data.to_excel('test_data.xls',sheet_name='data')


