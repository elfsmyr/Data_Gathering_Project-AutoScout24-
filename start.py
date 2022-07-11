from PyQt5 import QtWidgets,uic
import weather 
import database 

class StartWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(StartWindow, self).__init__()
        uic.loadUi('CarUI.ui', self)
        
        self.StartButton.clicked.connect(self.all_data)
        self.show()
        
    def all_data(self):
        data_num=database.carsdata()
        self.Total.setText(str(data_num.total_data()))
   
        
    def city_weather(self):
        pass
        # self.city="almere"
        # days=weather.Weather(self.city)
        # self.CityName.setText(self.city.upper())
        
    def data_info(self):
        pass