import numpy as np
import talib as talib
import pandas as pd
x=[ i.strip('\n').split(',') for i in open('./0050.csv') ]
data = []
data=[ i[4] for i in x]
data.remove("close")
float_data = [float(x) for x in data]
int_data=[int(x) for x in float_data]

print(data)


KBar = {}


KBar['P'] = np.array(float_data)
y=talib.SMA(KBar['P'],20)
print("y=",y)
ma = y.tolist()
print (type(ma))
print (type(data))
for i in range(0,19):
    ma[i] = 0 
for i in range(20,len(data)):
    if data[i-1]<ma[i-1] and data[i]>=ma[i]:
        print(i)
