import datetime
from typing import ClassVar
import numpy as np
class stockdataclass():
    
    def getKbar(self):
        # 取得資料
        Data=open("./stock.csv").readlines()
        # 進行資料解析
        Data01 = [ i.strip('\n').split(',') for i in Data ][1:] 
        # 存成 dictionary 格式
        KBar = {}
        KBar['Date'] = [ datetime.datetime.strptime(i[0],'%Y-%m-%d') for i in Data01 ]
        KBar['Open'] = np.array([ float(i[1]) for i in Data01 ])
        KBar['High'] = np.array([ float(i[2]) for i in Data01 ])
        KBar['Low'] = np.array([ float(i[3]) for i in Data01 ])
        KBar['Close'] = np.array([ float(i[4]) for i in Data01 ])
        return KBar