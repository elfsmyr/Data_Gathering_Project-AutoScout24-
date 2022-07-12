import psycopg2
import json
class carsdata():
        def __init__(self):
            self.conn = psycopg2.connect(
                    host = "localhost",
                    database = "auto",
                    user = "postgres",
                    password = "me5842")
            self.cur = self.conn.cursor()
        
            
        def all_auto(self):
            self.cur.execute("""             
             delete from cars values"""
            )
            with open('autoproject/auto.json') as f:
                data = json.load(f)
                for i in range(len(data)):
                    self.cur.execute("""             
             insert into cars (id, brand, model, km, plate, price, cityname, year, image) 
             VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(i+1,data[i]["brand"],data[i]["model"],data[i]["km"],data[i]["plate"],data[i]["price"],data[i]["city"],data[i]["year"],data[i]["image"])
            )
              
        def cars_info(self,brand):
            
            self.brand = brand
            
            self.cur.execute("""
            select model,plate,year from cars
            where brand = '{}'
            """.format(self.brand)
            )
            self.info = self.cur.fetchall()
            return self.info
            
        def special_info(self,brand,model):
            self.brand = brand
            self.model = model
            self.cur.execute("""
            select km,price,cityname,year,image from cars
            where model= '{}' and brand= '{}'
            """.format(self.model,self.brand),
            )
            self.info = self.cur.fetchall()
            return self.info
        
        def total_data(self):
            
            self.cur.execute("""
           SELECT COUNT(*) FROM cars  where brand = '{}'""".format(self.brand)
            )
            self.datanumber = self.cur.fetchall()
            return self.datanumber[0][0] 
        
        def close_(self):
            self.cur.close()
            self.conn.commit()
            if self.conn is not None:
                self.conn.close()
                

a = carsdata()
a.all_auto()
a.close_()