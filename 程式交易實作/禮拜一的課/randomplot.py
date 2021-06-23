# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomplot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

col = 2
row = 100
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 620)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 120, 351, 221))
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(450, 120, 381, 211))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "畫圖"))
        self.pushButton.clicked.connect(self.onclick)

    def onclick(self):
        _translate = QtCore.QCoreApplication.translate
        data= []
        x = np.linspace(0, 10, row)
        data.append(x)
        data.append(np.sin(x))
        # print(data)
        for c in range(col): # 走訪欄位
            x = data[c]
            for i in range(row): # 走訪索引
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, c, item) # 建構儲存格
                item = self.tableWidget.item(i, c) # 選取儲存格
                item.setText(_translate("MainWindow", str(x[i]))) # 修改儲存格文字        
        self.draw_bar_chart(data)
        
    def draw_bar_chart(self, x):
        print(x)
        plt.plot(x[0], x[1])        
        plt.savefig("sinplot.png")
        self.label.setPixmap(QtGui.QPixmap("sinplot.png")) # label 置換圖片
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

