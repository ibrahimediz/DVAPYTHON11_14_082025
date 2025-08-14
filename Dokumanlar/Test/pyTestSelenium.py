# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
# def get_default_chrome_options():
#     options = webdriver.ChromeOptions()
#     return options

# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)
# driver.get("https://www.google.com/")

# element = driver.find_element_by_name("q")
# element.send_keys("python")
# element.send_keys(Keys.RETURN)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "result-stats"))
#     )
#     print(element.text)
# finally:
#     pass
#     # driver.quit()



####################### 
## pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(Service(ChromeDriverManager().install()))



class SeleniumBot:
    def __init__(self,adres="",username="",password="",*args,**kwargs):
        self.username = username
        self.password = password
        self.adres = adres
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)

    def visit(self,adres):
        self.driver.get(adres)
        time.sleep(2)


if __name__ == "__main__":
    bot = SeleniumBot()
    bot.visit("https://www.google.com")