import requests
import json

class Weather():
    def __init__(self,city) :
        self.city = city
        api_url = "http://api.weatherapi.com/v1/forecast.json?key=94fcb3a48d06483ea3b141553220707&q=" + city + ",NL&days=3"
        result = requests.get(api_url)
        result = result.json()["forecast"]["forecastday"]
        for i in result:
            print("------------")
            print(i ["date"])
            print("max temp {}".format(i ["day"] ["maxtemp_c"]))
            print("min temp {}".format(i ["day"] ["mintemp_c"]))
            print("icon {}".format(i ["day"] ["condition"]["icon"]))
            
        print("------------")
            
        
    

a=Weather("utrecht")
print(a)