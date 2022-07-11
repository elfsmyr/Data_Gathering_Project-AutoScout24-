from PyQt5 import QtWidgets,uic
import weather 
import database 
import requests
from PyQt5.QtWidgets import  QTableWidgetItem
from PyQt5.QtGui import QImage , QPixmap

class StartWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        self.obj = database.carsdata()
        super(StartWindow, self).__init__()
        uic.loadUi('CarUI.ui', self)
        self.StartButton.clicked.connect(self.data_info)
        self.cars_widget.clicked.connect(self.on_click)
        self.show()
   
        
        
    def data_info(self):
        self.brand = self.Models.currentText()
        self.info = self.obj.cars_info(self.brand)
        self.num = self.obj.total_data()
        self.Total.setText(str(self.num))
        self.cars_widget.setRowCount(len(self.info))
        for i in range(len(self.info)):
                self.cars_widget.setItem(i,0,QTableWidgetItem(self.brand+" "+self.info[i][0]))
                self.cars_widget.setItem(i,1,QTableWidgetItem(self.info[i][1]))
                self.cars_widget.setItem(i,2,QTableWidgetItem(str(self.info[i][2])))
    
    def on_click(self):
        for i in self.cars_widget.selectedItems():
            column_num = i.column()
            if column_num == 0:
                self.sp_info(i.text())
            elif column_num == 1:
                self.plate_search(i.text())
                
    def sp_info(self,model):
        self.model = model
        self.model = self.model.split()
        self.car_model = self.model.pop(0)
        self.brand = " ".join(self.model)
        self.info = self.obj.special_info(self.car_model,self.brand)
        self.km = self.info[0][0]
        self.price_ = self.info[0][1]
        self.cityname = self.info[0][2]
        self.year_= self.info[0][3]
        self.url_image= self.info[0][4]
        self.make_model.setText(self.brand)
        self.kilometer.setText(self.km)
        self.price.setText(self.price_)
        self.year.setText(self.year_)
        self.city.setText(self.cityname)
        self.CityName.setText(self.cityname)
        self.image=QImage()
        self.image.loadFromData(requests.get(self.url_image).content)
        self.CarPicture.setPixmap(QPixmap(self.image))
        self.weather_info()
        
    def weather_info(self):
        a = weather.Weather(self.cityname)
        self.day1,self.day2,self.day3 = a.three_days()
        self.FirstDay.setText(self.day1[0]+"\n"+str(self.day1[2])+"-"+str(self.day1[1])+"°C")
        self.SecondDay.setText(self.day2[0]+"\n"+str(self.day2[2])+"-"+str(self.day2[1])+"°C")
        self.ThirdDay.setText(self.day3[0]+"\n"+str(self.day3[2])+"-"+str(self.day3[1])+"°C")
        self.d1_url_image = "http:"+self.day1[3]
        self.d2_url_image = "http:"+self.day2[3]
        self.d3_url_image = "http:"+self.day3[3]
        self.image.loadFromData(requests.get(self.d1_url_image).content)
        self.Picture1.setPixmap(QPixmap(self.image))
        self.image.loadFromData(requests.get(self.d2_url_image).content)
        self.Picture2.setPixmap(QPixmap(self.image))
        self.image.loadFromData(requests.get(self.d3_url_image).content)
        self.Picture3.setPixmap(QPixmap(self.image))
    
    def plate_search(self,plate):
        self.plate=plate
        self.PlateNum.setText(self.plate)
        
       
        
        

