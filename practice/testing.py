from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py


# all_personal_file=open("All_personal_data.txt","w")
temp_url="https://qa.referloan.in/apply-gold-loan"
name=NameGenerator.generator()
list_name=name.split()
pan_card=PanGenerator.generator(name)
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
driver.get("https://qa.referloan.in/")
time.sleep(3)
for i in range(1,10):
    try:
        innerhtml_text=driver.find_element(By.XPATH,"(//*[contains(@class,'loanType')])[%d]"%(i)).get_attribute('innerHTML')
        if 'select' in innerhtml_text:
            print(driver.find_element(By.XPATH,"(//*[contains(@class,'loanType')])[%d]/child::*/option[@selected='']"%(i)).text,"is input")
        elif 'input' in innerhtml_text:
            print(driver.find_element(By.XPATH,"(//*[contains(@class,'loanType')])[%d]/child::input"%(i)).get_attribute('placeholder'),"are input")

    except:
        exit(1)

time.sleep(2)
driver.close()