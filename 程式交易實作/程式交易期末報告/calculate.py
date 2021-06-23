from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import datetime 
from talib import SMA,STDDEV 
import numpy as np

class MABolClass():
    def ma_5(self, ui, KBar):    
        self.ui = ui
        #from function import getKbar
        import datetime
        from talib import SMA
        import numpy as np

        # 計算移動平均線 、 標準差 、 低點 
        KBar['MA'] = SMA(KBar['Close'], timeperiod= 60)
        KBar['5MA'] = SMA(KBar['Close'], timeperiod= 5)
        KBar['MA']= np.where(np.isnan(KBar['MA']), 0, KBar['MA'])
        KBar['5MA']= np.where(np.isnan(KBar['5MA']), 0, KBar['5MA'])

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
        #輸贏計數
        win= 0
        lose = 0

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
                
        for i in range(1,len(KBar['Date'])):
            Date = KBar['Date'][i]
            Close = KBar['Close'][i]
            LastClose = KBar['Close'][i-1]
            ma_5_old = KBar['5MA'][i-1]
            ma_60_old = KBar['MA'][i-1]
            ma_5 = KBar['5MA'][i]
            ma_60 = KBar['MA'][i]
            #print("i = ", i, "ma_5_old",ma_5_old,"ma_60_old",ma_60_old,"ma_5",ma_5,"ma_60",ma_60)

            status = []
            # 進場條件
            if ma_5_old < ma_60_old and ma_5 >= ma_60 and OrderQty == 0:
                # 進場時間、價格、數量
                OrderDate = KBar['Date'][i+1]
                OrderPrice = KBar['Open'][i+1]
                OrderQty = int(InitCapital/(Close)/1000)
                # 停損價、停利價
                TakeProfit = OrderPrice *1.6
                status = ' 低點 '
                print( '買進時間:', OrderDate.strftime('%Y-%m-%d') , '買進價格:',OrderPrice , '買進數量:' ,OrderQty )
                data['買進時間'].append(OrderDate.strftime('%Y-%m-%d'))
                data['買進原因'].append(status)
                data['買進價格'].append(OrderPrice)
                data['數量'].append(OrderQty)
            # 停損判斷
            elif OrderQty != 0 and ma_5_old >= ma_60_old and ma_5 < ma_60 :#等等這一段大小於要注意
                # 出場時間、價格
                CoverDate = KBar['Date'][i+1]
                CoverPrice = KBar['Open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停損 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'虧損:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
                
            # 停利判斷
            elif OrderQty != 0 and Close > TakeProfit   :
                # 出場時間、價格
                CoverDate = KBar['Date'][i+1]
                CoverPrice = KBar['Open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停利 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'獲利:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
            # 回測時間結束，則出場
            elif OrderQty != 0 and i == len(KBar['Date'])-1:
                # 出場時間、價格
                CoverDate = Date
                CoverPrice = Close
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 結束 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'盈虧:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
        result = pd.DataFrame(data) #把字典轉成DataFrame
        self.change_data(result, self.ui.tableWidget)
        print( '交易次數:' , TotalTreadeNum , '總盈虧:', sum(TotalProfit) )
        all_profit = round(sum(TotalProfit))
        win_Probability = win/TotalTreadeNum
        final_to_print = '交易次數: ' + str(TotalTreadeNum) + '次 總盈虧: '+ str(all_profit) + " 平均損益: " + str(round(all_profit/TotalTreadeNum)) + "\n" +"勝率: "+ str(win_Probability)
        #result = pd.DataFrame(data)
        #print(result)
        #self.change_data(result, self.ui.tableWidget)

        KPI_dict = {'交易次數' : [TotalTreadeNum],
                    '總盈虧' : [sum(TotalProfit)]
                    }
        KPI_df = pd.DataFrame(KPI_dict)
        self.change_data(KPI_df, self.ui.tableWidget_2)
        
        import matplotlib.pyplot as plt # 匯出績效圖表
        import matplotlib.ticker as plticker
        plot_X = list(range(1, len(TotalProfit) + 1))
        plot_Y = np.cumsum(TotalProfit)
        ax = plt.subplot(111)           # 新增繪圖圖片
        
        ax.bar( plot_X, plot_Y )      # 繪製圖案 ( X軸物件, Y軸物件 )
        ax.ticklabel_format(style = "plain") # 設定Y軸為實數顯示，否則預設顯示為科學符號
        
        # 設定X軸間隔為1
        loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
        ax.xaxis.set_major_locator(loc)
        
        # 設定文字
        for x, y in zip(plot_X, plot_Y):
            text_show = int(y)
            # plt.text(X座標, Y座標, 顯示內容, 水平對齊方式, 垂直對齊方式)
            if y > 0:
                plt.text(x ,y ,text_show, ha = "center", va = "bottom")
            else:
                plt.text(x ,y ,text_show, ha = "center", va = "top") 
        
        plt.savefig("bar_chart.png")
        self.change_plot("bar_chart.png")
        self.print_final(final_to_print)

    def ma_10(self, ui, KBar):    
            self.ui = ui
            #from function import getKbar
            import datetime
            from talib import SMA
            import numpy as np

            # 計算移動平均線 、 標準差 、 低點 
            KBar['MA'] = SMA(KBar['Close'], timeperiod= 60)
            KBar['10MA'] = SMA(KBar['Close'], timeperiod= 10)
            KBar['MA']= np.where(np.isnan(KBar['MA']), 0, KBar['MA'])
            KBar['10MA']= np.where(np.isnan(KBar['10MA']), 0, KBar['10MA'])

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
            #輸贏計數
            win= 0
            lose = 0

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
                    
            for i in range(1,len(KBar['Date'])):
                Date = KBar['Date'][i]
                Close = KBar['Close'][i]
                LastClose = KBar['Close'][i-1]
                ma_10_old = KBar['10MA'][i-1]
                ma_60_old = KBar['MA'][i-1]
                ma_10 = KBar['10MA'][i]
                ma_60 = KBar['MA'][i]
                #print("i = ", i, "ma_5_old",ma_5_old,"ma_60_old",ma_60_old,"ma_5",ma_5,"ma_60",ma_60)

                status = []
                # 進場條件
                if ma_10_old < ma_60_old and ma_10 >= ma_60 and OrderQty == 0:
                    # 進場時間、價格、數量
                    OrderDate = KBar['Date'][i+1]
                    OrderPrice = KBar['Open'][i+1]
                    OrderQty = int(InitCapital/(Close)/1000)
                    # 停損價、停利價
                    TakeProfit = OrderPrice *1.6
                    status = ' 低點 '
                    print( '買進時間:', OrderDate.strftime('%Y-%m-%d') , '買進價格:',OrderPrice , '買進數量:' ,OrderQty )
                    data['買進時間'].append(OrderDate.strftime('%Y-%m-%d'))
                    data['買進原因'].append(status)
                    data['買進價格'].append(OrderPrice)
                    data['數量'].append(OrderQty)
                # 停損判斷
                elif OrderQty != 0 and ma_10_old >= ma_60_old and ma_10 < ma_60 :#等等這一段大小於要注意
                    # 出場時間、價格
                    CoverDate = KBar['Date'][i+1]
                    CoverPrice = KBar['Open'][i+1]
                    # 績效紀錄
                    Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                    if Profit >= 0:
                        win += 1
                    else:
                        lose += 1
                    TotalProfit += [Profit]
                    TotalTreadeNum += 1
                    # InitCapital += Profit
                    # 下單數量歸零，重新進場
                    OrderQty = 0
                    status = ' 停損 '
                    print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'虧損:',Profit  )
                    data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                    data['售出原因'].append(status)
                    data['售出價格'].append(CoverPrice)
                    data['獲利'].append(Profit)
                    
                # 停利判斷
                elif OrderQty != 0 and Close > TakeProfit   :
                    # 出場時間、價格
                    CoverDate = KBar['Date'][i+1]
                    CoverPrice = KBar['Open'][i+1]
                    # 績效紀錄
                    Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                    if Profit >= 0:
                        win += 1
                    else:
                        lose += 1
                    TotalProfit += [Profit]
                    TotalTreadeNum += 1
                    # InitCapital += Profit
                    # 下單數量歸零，重新進場
                    OrderQty = 0
                    status = ' 停利 '
                    print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'獲利:',Profit  )
                    data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                    data['售出原因'].append(status)
                    data['售出價格'].append(CoverPrice)
                    data['獲利'].append(Profit)
                # 回測時間結束，則出場
                elif OrderQty != 0 and i == len(KBar['Date'])-1:
                    # 出場時間、價格
                    CoverDate = Date
                    CoverPrice = Close
                    # 績效紀錄
                    Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                    if Profit >= 0:
                        win += 1
                    else:
                        lose += 1
                    TotalProfit += [Profit]
                    TotalTreadeNum += 1
                    # InitCapital += Profit
                    # 下單數量歸零，重新進場
                    OrderQty = 0
                    status = ' 結束 '
                    print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'盈虧:',Profit  )
                    data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                    data['售出原因'].append(status)
                    data['售出價格'].append(CoverPrice)
                    data['獲利'].append(Profit)
            result = pd.DataFrame(data) #把字典轉成DataFrame
            self.change_data(result, self.ui.tableWidget)
            print( '交易次數:' , TotalTreadeNum , '總盈虧:', sum(TotalProfit) )
            all_profit = round(sum(TotalProfit))
            win_Probability = win/TotalTreadeNum
            final_to_print = '交易次數: ' + str(TotalTreadeNum) + '次 總盈虧: '+ str(all_profit) + " 平均損益: " + str(round(all_profit/TotalTreadeNum)) + "\n" +"勝率: "+ str(win_Probability)
            #result = pd.DataFrame(data)
            #print(result)
            #self.change_data(result, self.ui.tableWidget)

            KPI_dict = {'交易次數' : [TotalTreadeNum],
                        '總盈虧' : [sum(TotalProfit)]
                        }
            KPI_df = pd.DataFrame(KPI_dict)
            self.change_data(KPI_df, self.ui.tableWidget_2)
            
            import matplotlib.pyplot as plt # 匯出績效圖表
            import matplotlib.ticker as plticker
            plot_X = list(range(1, len(TotalProfit) + 1))
            plot_Y = np.cumsum(TotalProfit)
            ax = plt.subplot(111)           # 新增繪圖圖片
            
            ax.bar( plot_X, plot_Y )      # 繪製圖案 ( X軸物件, Y軸物件 )
            ax.ticklabel_format(style = "plain") # 設定Y軸為實數顯示，否則預設顯示為科學符號
            
            # 設定X軸間隔為1
            loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
            ax.xaxis.set_major_locator(loc)
            
            # 設定文字
            for x, y in zip(plot_X, plot_Y):
                text_show = int(y)
                # plt.text(X座標, Y座標, 顯示內容, 水平對齊方式, 垂直對齊方式)
                if y > 0:
                    plt.text(x ,y ,text_show, ha = "center", va = "bottom")
                else:
                    plt.text(x ,y ,text_show, ha = "center", va = "top") 
            
            plt.savefig("bar_chart.png")
            self.change_plot("bar_chart.png")
            self.print_final(final_to_print)
    

    def ma_20(self, ui, KBar):    
        self.ui = ui
        #from function import getKbar
        import datetime
        from talib import SMA
        import numpy as np

        # 計算移動平均線 、 標準差 、 低點 
        KBar['MA'] = SMA(KBar['Close'], timeperiod= 60)
        KBar['20MA'] = SMA(KBar['Close'], timeperiod= 20)
        KBar['MA']= np.where(np.isnan(KBar['MA']), 0, KBar['MA'])
        KBar['20MA']= np.where(np.isnan(KBar['20MA']), 0, KBar['20MA'])

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
        #輸贏計數
        win= 0
        lose = 0

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
                
        for i in range(1,len(KBar['Date'])):
            Date = KBar['Date'][i]
            Close = KBar['Close'][i]
            LastClose = KBar['Close'][i-1]
            ma_20_old = KBar['20MA'][i-1]
            ma_60_old = KBar['MA'][i-1]
            ma_20 = KBar['20MA'][i]
            ma_60 = KBar['MA'][i]


            status = []
            # 進場條件
            if ma_20_old < ma_60_old and ma_20 >= ma_60 and OrderQty == 0:
                # 進場時間、價格、數量
                OrderDate = KBar['Date'][i+1]
                OrderPrice = KBar['Open'][i+1]
                OrderQty = int(InitCapital/(Close)/1000)
                # 停損價、停利價
                TakeProfit = OrderPrice *1.6
                status = ' 低點 '
                print( '買進時間:', OrderDate.strftime('%Y-%m-%d') , '買進價格:',OrderPrice , '買進數量:' ,OrderQty )
                data['買進時間'].append(OrderDate.strftime('%Y-%m-%d'))
                data['買進原因'].append(status)
                data['買進價格'].append(OrderPrice)
                data['數量'].append(OrderQty)
            # 停損判斷
            elif OrderQty != 0 and ma_20_old >= ma_60_old and ma_20 < ma_60 :#等等這一段大小於要注意
                # 出場時間、價格
                CoverDate = KBar['Date'][i+1]
                CoverPrice = KBar['Open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停損 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'虧損:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
                
            # 停利判斷
            elif OrderQty != 0 and Close > TakeProfit   :
                # 出場時間、價格
                CoverDate = KBar['Date'][i+1]
                CoverPrice = KBar['Open'][i+1]
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 停利 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'獲利:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
            # 回測時間結束，則出場
            elif OrderQty != 0 and i == len(KBar['Date'])-1:
                # 出場時間、價格
                CoverDate = Date
                CoverPrice = Close
                # 績效紀錄
                Profit = (CoverPrice-OrderPrice)*OrderQty*1000
                if Profit >= 0:
                    win += 1
                else:
                    lose += 1
                TotalProfit += [Profit]
                TotalTreadeNum += 1
                # InitCapital += Profit
                # 下單數量歸零，重新進場
                OrderQty = 0
                status = ' 結束 '
                print( '售出時間:', CoverDate.strftime('%Y-%m-%d') , '售出價格:' , CoverPrice ,'盈虧:',Profit  )
                data['售出時間'].append(CoverDate.strftime('%Y-%m-%d'))
                data['售出原因'].append(status)
                data['售出價格'].append(CoverPrice)
                data['獲利'].append(Profit)
        result = pd.DataFrame(data) #把字典轉成DataFrame
        self.change_data(result, self.ui.tableWidget)
        print( '交易次數:' , TotalTreadeNum , '總盈虧:', sum(TotalProfit) )
        all_profit = round(sum(TotalProfit))
        win_Probability = win/TotalTreadeNum
        final_to_print = '交易次數: ' + str(TotalTreadeNum) + '次 總盈虧: '+ str(all_profit) + " 平均損益: " + str(round(all_profit/TotalTreadeNum)) + "\n" +"勝率: "+ str(win_Probability)
        #result = pd.DataFrame(data)
        #print(result)
        #self.change_data(result, self.ui.tableWidget)

        KPI_dict = {'交易次數' : [TotalTreadeNum],
                    '總盈虧' : [sum(TotalProfit)]
                    }
        KPI_df = pd.DataFrame(KPI_dict)
        self.change_data(KPI_df, self.ui.tableWidget_2)
        
        import matplotlib.pyplot as plt # 匯出績效圖表
        import matplotlib.ticker as plticker
        plot_X = list(range(1, len(TotalProfit) + 1))
        plot_Y = np.cumsum(TotalProfit)
        ax = plt.subplot(111)           # 新增繪圖圖片
        
        ax.bar( plot_X, plot_Y )      # 繪製圖案 ( X軸物件, Y軸物件 )
        ax.ticklabel_format(style = "plain") # 設定Y軸為實數顯示，否則預設顯示為科學符號
        
        # 設定X軸間隔為1
        loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
        ax.xaxis.set_major_locator(loc)
        
        # 設定文字
        for x, y in zip(plot_X, plot_Y):
            text_show = int(y)
            # plt.text(X座標, Y座標, 顯示內容, 水平對齊方式, 垂直對齊方式)
            if y > 0:
                plt.text(x ,y ,text_show, ha = "center", va = "bottom")
            else:
                plt.text(x ,y ,text_show, ha = "center", va = "top") 
        
        plt.savefig("bar_chart.png")
        self.change_plot("bar_chart.png")
        self.print_final(final_to_print)
    
    def print_final(self,label_print):
        _translate = QtCore.QCoreApplication.translate

        self.ui.label_3.setText(_translate("Dialog",label_print))

#----------------------------------------------------
    def change_plot(self, plot_path):
        # 根據lineEdit 中的文字，呼叫 yF_Kbar 製作 K 線圖
        self.ui.label_2.setPixmap(QtGui.QPixmap("bar_chart.png")) # label 置換圖片
    
    def change_data(self, df, target):
        columns_num = df.shape[1] # DataFrame 的 欄位數
        index_num = df.shape[0] # DataFrame 的 列數
        df_columns = df.columns # DataFrame 的 欄位名稱
        df_index = df.index # DataFrame 的 索引列表
        
        target.setColumnCount(columns_num) # 修改 Table Wedget 的欄位數
        target.setRowCount(index_num) # 修改 Table Wedget 的列數
        
        _translate = QtCore.QCoreApplication.translate
        
        # 修改欄位相關資訊
        for c in range(columns_num):
            item = QtWidgets.QTableWidgetItem()
            target.setHorizontalHeaderItem(c, item) # 依據欄位列表依序建構欄位
            
            item = target.horizontalHeaderItem(c) # 選取該欄位
            item.setText(_translate("MainWindow", df_columns[c])) # 修改欄位標題文字
            
        for i in range(index_num):
            item = QtWidgets.QTableWidgetItem()
            target.setVerticalHeaderItem(i, item) # 依據索引列表依序建構欄位
            
            item = target.verticalHeaderItem(i) # 選取該索引
            item.setText(_translate("MainWindow", str(df_index[i]) )) # 修改索引標題文字
            
        for c in range(columns_num): # 走訪欄位
            for i in range(index_num): # 走訪索引
                item = QtWidgets.QTableWidgetItem()
                target.setItem(i, c, item) # 建構儲存格

                item = target.item(i, c) # 選取儲存格
                item.setText(_translate("MainWindow", str(df.iloc[i, c]))) # 修改儲存格文字




