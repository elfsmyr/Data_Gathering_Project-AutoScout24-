from PyQt5 import QtWidgets,uic

class StartWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(StartWindow, self).__init__()
        uic.loadUi('CarUI.ui', self)
        
        self.show()