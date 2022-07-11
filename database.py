import psycopg2
class carsdata():
        def __init__(self):
            self.conn = psycopg2.connect(
                    host = "localhost",
                    database = "auto",
                    user = "postgres",
                    password = "me5842")
            self.cur = self.conn.cursor()
        
        def brands(self):
            self.cur.execute("""
            select distinct brand  from cars
            
            """
            )
            self.brands_ = self.cur.fetchall()
            return self.brands_
            
        def all_auto(self):

            pass
            # self.cur.execute("""             
            #  insert into cars" (id, "Brand", "Model", "KM", "Plate", "Price", "Cityname", year, "Image") 
            #  VALUES ({},{},{},{},{},{},{},{},{})
            # """.format()
            # )
            
        def cars_info(self,brand):
            
            self.brand=brand
            self.cur.execute("""
            select id,model,plate,year from cars
            where Brand='{}'
            """.format(self.brand)
            )
            self.info = self.cur.fetchall()
            return self.info
            
        def special_info(self,plate):
            self.plate=plate
            self.cur.execute("""
            select model,km,price,cityname,year from cars
            where Plate='{}'
            """.format(self.plate),
            )
            self.cityname = self.cur.fetchall()
            return self.cityname
        
        def total_data(self):
            
            self.cur.execute("""
           SELECT COUNT(*) FROM cars """
            )
            self.datanumber = self.cur.fetchall()
            return self.datanumber[0][0]
a=carsdata()
print(a.brands())
        