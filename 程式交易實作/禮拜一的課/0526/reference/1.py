# -*- coding: UTF-8 -*-

# 載入函數
from function import getKbar
import datetime

# 取得資料
KBar=getKbar()

# 初始資金
InitCapital=1000000
OrderPrice = None
OrderQty = 0
CoverPrice = None

# 買進日期
OrderDate = datetime.datetime.strptime('2004/1/5' , '%Y/%m/%d')

# 賣出日期
CoverDate = datetime.datetime.strptime('2018/12/28' , '%Y/%m/%d')

for i in range(len(KBar['date'])):
    Date=KBar['date'][i]
    # 如果指定時間購買
    if Date == OrderDate and OrderQty == 0 :
        # 開盤價買進
        OrderPrice = KBar['open'][i]
        OrderQty = int(InitCapital/(KBar['close'][i-1])/1000)
    if Date == CoverDate and OrderQty != 0 :
        # 最後一個收盤價賣出
        CoverPrice = KBar['close'][i]
        break

print( '買進時間:', OrderDate.strftime('%Y/%m/%d'),'買進價格:',OrderPrice , '買進數量:' ,OrderQty )
print( '售出時間:', CoverDate.strftime('%Y/%m/%d') , '售出價格:' , CoverPrice )
print( '獲利:',(CoverPrice-OrderPrice)*OrderQty*1000 )



