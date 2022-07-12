from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class plate_selenium():
    def __init__(self,plate) :
        self.plate=plate
        driver=webdriver.Chrome()
        url="https://www.centraalbeheer.nl/verzekeringen/autoverzekering/kentekencheck"
        driver.get(url)
        
        time.sleep(2)
        
        # entry=driver.find_element(By.XPATH,"//*[@id='tekst1']/div[2]/a[1]")
        # entry.click()
        # time.sleep(2)

        plate=driver.find_element(By.NAME,"kenteken")
        plate.send_keys(self.plate)
        time.sleep(2)


        buton =driver.find_element(By.XPATH,"//*[@id='kenteken-button']")
        buton.click()
        # driver.execute_script("arguments[0].click();", buton)
        
        time.sleep(60)
        driver.quit()
 