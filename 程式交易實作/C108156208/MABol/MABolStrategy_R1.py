from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import datetime 
from talib import SMA,STDDEV 
import numpy as np

class MABolClass():
    def BuyAndHold(self, ui, KBar):
        self.ui = ui

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
        
        data = {
               '買進時間:': [OrderDate.strftime('%Y/%m/%d')], 
                '買進價格:': [OrderPrice],
                '買進數量:': [OrderQty],
                '售出時間:': [CoverDate.strftime('%Y/%m/%d')],
                '售出價格:': [CoverPrice],
                '獲利:': [(CoverPrice-OrderPrice)*OrderQty*1000],
                }
                       
        result = pd.DataFrame(data)
        self.change_data(result)
        
    def StopProfitLoss(self, ui, KBar):    
        self.ui = ui
        #from function import getKbar
        import datetime
        from talib import SMA,STDDEV
        import numpy as np

        # 計算移動平均線 、 標準差 、 低點 
        KBar['MA'] = SMA(KBar['close'], timeperiod= 120)
        KBar['STD'] = STDDEV(KBar['close'], timeperiod= 120)
        KBar['BD'] = KBar['MA']-0.75*KBar['STD']

        # 初始資金
        InitCapital=1000000
        # 進場價格 、 進場數量
        OrderPrice = None
        OrderQty = 0
        # 出場價格
        CoverPrice = None
        # 停損 、 停利價
        StopLoss = None
        TakeProfit = None
        # 總獲利 、 交易次數
        TotalProfit = []
        TotalTreadeNum = 0 


        data = {
                '買進時間': [], 
                '買進原因': [],
                '買進價格': [],
                '售出時間': [],
                '售出價格': [],
                '售出原因': [],
                '數量': [],
                '獲利': []#[(CoverPrice-OrderPrice)*OrderQty*1000],
                }   
                
        for i in range(1,len(KBar['date'])):
            Date = KBar['date'][i]
            Close = KBar['close'][i]
            LastClose = KBar['close'][i-1]
            BD = KBar['BD'][i]
            LastBD = KBar['BD'][i-1]
            status = []
            # 進場條件
            if LastClose < LastBD and Close >= BD and OrderQty == 0 :
                # 進場時間、價格、數量
                OrderDate = KBar['date'][i+1]
                OrderPrice = KBar['open'][i+1]
                OrderQty = int(InitCapital/(Close)/1000)
                # 停損價、停利價
                StopLoss = OrderPrice *0.8
                TakeProfit = OrderPrice *1.6
                status = ' 低點 '
                print( '買進時間:', OrderDate.strftime('%Y/%m/%d') , '買進價格:',OrderPrice , '買進數量:' ,OrderQty )
                data['買進時間'].append(OrderDate.strftime('%Y/%m/%d'))
                data['買進原因'].append(status)
                data['買進價格'].append(OrderPrice)
                data['數量'].append(OrderQty)
            # 停損判斷
            elif OrderQty != 0 and Close < StopLoss :
                # 出場時間、價格
                CoverDate = KBar['date'][i+1]
                CoverPrice = KBar['open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停損 '
                print( '售出時間:', CoverDate.strftime('%Y/%m/%d') , '售出價格:' , CoverPrice ,'虧損:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y/%m/%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
                
            # 停利判斷
            elif OrderQty != 0 and Close > TakeProfit   :
                # 出場時間、價格
                CoverDate = KBar['date'][i+1]
                CoverPrice = KBar['open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停利 '
                print( '售出時間:', CoverDate.strftime('%Y/%m/%d') , '售出價格:' , CoverPrice ,'獲利:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y/%m/%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
            # 回測時間結束，則出場
            elif OrderQty != 0 and i == len(KBar['date'])-1:
                # 出場時間、價格
                CoverDate = Date
                CoverPrice = Close
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 結束 '
                print( '售出時間:', CoverDate.strftime('%Y/%m/%d') , '售出價格:' , CoverPrice ,'盈虧:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y/%m/%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)

        print( '交易次數:' , TotalTreadeNum , '總盈虧:', sum(TotalProfit) )
        result = pd.DataFrame(data)
        print(result)
        self.change_data(result)

        import matplotlib.pyplot as plt # 匯出績效圖表
        plot_X = list(range(0, len(TotalProfit)))
        ax = plt.subplot(111)           # 新增繪圖圖片
        ax.bar( plot_X, np.cumsum(TotalProfit) )      # 繪製圖案 ( X軸物件, Y軸物件, 線風格 )
        plt.show()       
        
    def change_data(self, df):
        # 根據lineEdit 中的文字，呼叫 yF_Kbar 製作 K 線圖
        #self.label_2.setPixmap(QtGui.QPixmap("stock_Kbar.png")) # label 置換圖片

        columns_num = df.shape[1] # DataFrame 的 欄位數
        index_num = df.shape[0] # DataFrame 的 列數
        df_columns = df.columns # DataFrame 的 欄位名稱
        df_index = df.index # DataFrame 的 索引列表
        
        self.ui.tableWidget.setColumnCount(columns_num) # 修改 Table Wedget 的欄位數
        self.ui.tableWidget.setRowCount(index_num) # 修改 Table Wedget 的列數
        
        _translate = QtCore.QCoreApplication.translate
        
        # 修改欄位相關資訊
        for c in range(columns_num):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(c, item) # 依據欄位列表依序建構欄位
            
            item = self.ui.tableWidget.horizontalHeaderItem(c) # 選取該欄位
            item.setText(_translate("MainWindow", df_columns[c])) # 修改欄位標題文字
             
        for i in range(index_num):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(i, item) # 依據索引列表依序建構欄位
            
            item = self.ui.tableWidget.verticalHeaderItem(i) # 選取該索引
            item.setText(_translate("MainWindow", str(df_index[i]) )) # 修改索引標題文字
            
        for c in range(columns_num): # 走訪欄位
            for i in range(index_num): # 走訪索引
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget.setItem(i, c, item) # 建構儲存格

                item = self.ui.tableWidget.item(i, c) # 選取儲存格
                item.setText(_translate("MainWindow", str(df.iloc[i, c]))) # 修改儲存格文字
