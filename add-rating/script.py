from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

url=pyautogui.prompt("Enter 1st URL")
url1=pyautogui.prompt("Enter 2nd URL")
url2=pyautogui.prompt("Enter 3rd URL")
try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,250)")
    time.sleep(3)
    for i in range(random.randint(65,80)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[5]").click()
    for i in range(random.randint(30,40)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[4]").click()
    time.sleep(2)

    driver.get(url1)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,250)")
    time.sleep(3)
    for i in range(random.randint(40,80)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[5]").click()
    for i in range(random.randint(20,40)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[4]").click()
    time.sleep(2)

    driver.get(url2)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,250)")
    time.sleep(3)
    for i in range(random.randint(40,80)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[5]").click()
    for i in range(random.randint(20,40)):
        driver.find_element(By.XPATH,"(//span[@class='star'])[4]").click()
    time.sleep(2)
    driver.close()
except:
    print("Finished with error")
finally:
    pyautogui.alert("RATING HACKED SUCCESSFULLY")