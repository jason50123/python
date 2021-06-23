import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import function as data
import calculate as MAB
import Ui_test
import stock


def handleClick():
    stock.stock(ui.onClick())
    KBar()
    ui.changePic()
def KBar():
    kb = data.stockdataclass()
    KBar=kb.getKbar()
    return KBar


    

if __name__ == "__main__":
    
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow() 
    ui = Ui_test.Ui_MainWindow() 
    ui.setupUi(MainWindow)
    MainWindow.show() 
    mab = MAB.MABolClass()
    #------------------------------onclick後，抓輸入的股票資訊
    ui.pushButton.clicked.connect(lambda:handleClick() )
    #------------------------------
    # 呼叫策略類別MABolClass產生物件實體mab
    
    ui.radioButton.clicked.connect(lambda: mab.ma_5(ui,KBar()))
    ui.radioButton_2.clicked.connect(lambda: mab.ma_10(ui,KBar()))
    ui.radioButton_3.clicked.connect(lambda: mab.ma_20(ui,KBar()))
    #------------------------------------------------    
    
    sys.exit(app.exec_())
