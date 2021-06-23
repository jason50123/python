# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import yF_Kbar as kbar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 391, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 80, 381, 321))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("起始圖.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "畫k線圖"))
        self.label.setText(_translate("MainWindow", "讀取資料筆數"))
        # 按下按鈕後，觸發 onclick 函數
        self.pushButton.clicked.connect(self.onclick)
    
    def onclick(self):
        amount = int(self.lineEdit.text()) # 讀取 lineEdit 中的文字

        df= kbar.import_csv(amount)
        self.change_data(df) 
    
    def change_data(self, df):
        # 根據lineEdit 中的文字，呼叫 yF_Kbar 製作 K 線圖
        kbar.draw_candle_chart(df) 
        self.label_2.setPixmap(QtGui.QPixmap("stock_Kbar.png")) # label 置換圖片

        columns_num = df.shape[1] # DataFrame 的 欄位數
        index_num = df.shape[0] # DataFrame 的 列數
        df_columns = df.columns # DataFrame 的 欄位名稱
        df_index = df.index # DataFrame 的 索引列表
        
        self.tableWidget.setColumnCount(columns_num) # 修改 Table Wedget 的欄位數
        self.tableWidget.setRowCount(index_num) # 修改 Table Wedget 的列數
        
        _translate = QtCore.QCoreApplication.translate
        
        # 修改欄位相關資訊
        for c in range(columns_num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(c, item) # 依據欄位列表依序建構欄位
            
            item = self.tableWidget.horizontalHeaderItem(c) # 選取該欄位
            item.setText(_translate("MainWindow", df_columns[c])) # 修改欄位標題文字
            
        for i in range(index_num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item) # 依據索引列表依序建構欄位
            
            item = self.tableWidget.verticalHeaderItem(i) # 選取該索引
            item.setText(_translate("MainWindow", str(df_index[i]) )) # 修改索引標題文字
            
        for c in range(columns_num): # 走訪欄位
            for i in range(index_num): # 走訪索引
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, c, item) # 建構儲存格

                item = self.tableWidget.item(i, c) # 選取儲存格
                item.setText(_translate("MainWindow", str(df.iloc[i, c]))) # 修改儲存格文字

if __name__ == "__main__":
    data=[ i.strip('\n').split(',') for i in open('./0050.csv') ]
    stock_id = "0000"
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
