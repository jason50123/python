
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import StockData.function_data as fdata
import MABol.MABolStrategy as MAB
import Ui_HW0524_GUI 

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow() 
    ui = Ui_HW0524_GUI.Ui_MainWindow() 
    ui.setupUi(MainWindow)
    #------------------------------------------------
    # 取得資料
    kb = fdata.stockdataclass()
    KBar=kb.getKbar()
    # 呼叫策略類別MABolClass產生物件實體mab
    mab = MAB.MABolClass()
    # 呼叫繼承自類別的策略方法-買入持有
    ui.radioButton.clicked.connect(lambda: mab.BuyAndHold(ui,KBar))    
    # 呼叫繼承自類別的策略方法-低點買進+停損停利
    ui.radioButton_2.clicked.connect(lambda: mab.StopProfitLoss(ui,KBar)) 
    #------------------------------------------------    
    MainWindow.show() 
    sys.exit(app.exec_())
