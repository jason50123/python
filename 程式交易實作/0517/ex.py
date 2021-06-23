
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '0517.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd,talib

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(967, 726)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 90, 151, 61))
        font = QtGui.QFont()
        font.setFamily("華康新儷粗黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("華康新儷粗黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily("華康新儷粗黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(360, 90, 221, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 220, 211, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 360, 241, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 480, 631, 121))
        font = QtGui.QFont()
        font.setFamily("華康新儷粗黑")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(680, 180, 221, 141))
        font = QtGui.QFont()
        font.setFamily("華康新儷粗黑")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.onclick)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "收盤價均線日數:"))
        self.label_2.setText(_translate("Dialog", "成交量均線日數:"))
        self.label_3.setText(_translate("Dialog", "成交量倍率:"))
        self.label_4.setText(_translate("Dialog", "計算的數值放這邊"))
        self.pushButton.setText(_translate("Dialog", "按我計算"))
        
    def onclick(self):
        _translate = QtCore.QCoreApplication.translate
        df = pd.read_csv( "0050.csv" )

        df["收盤價"] = df["close"] 
        df["成交量"] = df["volume"]
        df["賣出收盤價"] = df["close"].shift(-3)

        df = df.loc[:,["date", "收盤價", "成交量","賣出收盤價"]] 
        print(df)
        Cavg = talib.SMA(df["收盤價"],int(self.lineEdit.text()))
        Vavg = talib.SMA(df["成交量"],int(self.lineEdit_2.text()))
        dfC = df['收盤價'] >= Cavg
        dfV = df['成交量'] >= Vavg * float(self.lineEdit_3.text())
        df = df[(dfC & dfV)]
        df["損益"] = ( df["賣出收盤價"] - df["收盤價"] ) * 1000
        total_profit = df["損益"].sum() 
        avg_profit = df["損益"].mean() 
        trade_times = df["損益"].count()
        label_print = '總收益=' + str(round(total_profit,2))+ '\n' + '平均收益' + str(round(avg_profit,2)) + '\n' + '交易次數=' + str(trade_times)

        self.label_4.setText(_translate("Dialog",label_print))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
