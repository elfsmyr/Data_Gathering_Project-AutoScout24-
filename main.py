from start import StartWindow
from PyQt5 import QtWidgets
import sys                   

app = QtWidgets.QApplication(sys.argv)
window = StartWindow()
app.exec_()