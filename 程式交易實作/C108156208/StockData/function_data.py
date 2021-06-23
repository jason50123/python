# -*- coding: UTF-8 -*-
import pandas as pd
class stockdataclass():

    def getKbar(self):
        # 取得資料
        import datetime
        import numpy as np
        filename='./0050.csv'
        Data=open(filename).readlines()
        # 進行資料解析
        Data01 = [ i.strip('\n').split(',') for i in Data ][1:] 
        # 存成 dictionary 格式
        KBar = {}
        KBar['date'] = [ datetime.datetime.strptime(i[0],'%Y/%m/%d') for i in Data01 ]
        KBar['open'] = np.array([ float(i[1]) for i in Data01 ])
        KBar['high'] = np.array([ float(i[2]) for i in Data01 ])
        KBar['low'] = np.array([ float(i[3]) for i in Data01 ])
        KBar['close'] = np.array([ float(i[4]) for i in Data01 ])
        return KBar
    
