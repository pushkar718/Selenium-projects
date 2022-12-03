import time
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
actions=ActionChains(driver)
driver.get("https://qa.referloan.in")
time.sleep(3)
for b in range(1, 500):
    all=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[%d]"%(b))
    print(all)
    time.sleep(1)
time.sleep(1)
driver.close()