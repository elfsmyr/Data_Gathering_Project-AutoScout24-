import requests
import json

class Weather():
    def __init__(self,city) :
        self.city = city
        api_url = "http://api.weatherapi.com/v1/forecast.json?key=94fcb3a48d06483ea3b141553220707&q=" + city + ",NL&days=3"
        self.result = requests.get(api_url)
        self.result = self.result.json()["forecast"]["forecastday"]
        
      
    def three_days(self):
        info = []
        
        for i in self.result:
            day=[]
            day.append(i ["date"])
            day.append(i ["day"] ["maxtemp_c"])
            day.append(i ["day"] ["mintemp_c"])
            day.append(i ["day"] ["condition"]["icon"])
            info.append(day)    
            
        return info

