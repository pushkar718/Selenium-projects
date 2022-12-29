import time
import pyautogui as py
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://qa.referloan.in/loans/cashe-personal-loan")
time.sleep(2)
with py.hold("ctrl"):
    py.press("-")
    py.press("-")
    py.press("-")
    py.press("-")
    py.press("-")

rate=driver.find_elements(By.XPATH,"//*[@class='ratingWrapper']")
print(rate[0].text)
if 'product' in rate[0].text.lower():
    print("Found")
else:
    print("Not found")
time.sleep(2)
driver.close()