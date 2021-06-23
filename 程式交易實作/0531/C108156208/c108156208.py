import talib as talib
import numpy as np

KBar = {}

x=[ i.strip('\n').split(',') for i in open('./0050.csv') ]
data = [ i[4] for i in x]
date = [ i[0] for i in x]
data.remove("close")
float_data = [float(x) for x in data]

#x=[10.,11.,12.,15.,10.,8.,15.,18.,19.,15.,14.]
KBar['P'] = np.array(float_data)
y=talib.SMA(KBar['P'],21)
round_ma = [round(num,2) for num in y]

for i in range(20,len(float_data)):
    if float_data[i-1]<y[i-1] and float_data[i]>=y[i]:
        print("日期: {date} 收盤:{data} MA值: {round_ma}".format(date = date[i],data = data[i-1],round_ma = round_ma[i]))
