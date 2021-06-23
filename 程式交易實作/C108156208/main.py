import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_HW0524_GUI

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow() 
#----------------------------------------    
    ui = Ui_HW0524_GUI.Ui_MainWindow() 
    ui.setupUi(MainWindow) 
#----------------------------------------    
    MainWindow.show() 
    sys.exit(app.exec_())
