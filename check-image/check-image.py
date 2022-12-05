from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
driver.get("https://qa.referloan.in")
time.sleep(3)
for b in range(1,500):
    check=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[%d]"%(b))
    check_text = driver.find_element(By.XPATH, "(//ul/li/a[@tabindex='-1'])[%d]" % (b)).text
    check_last=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[last()]").text
    check_url=check.get_attribute('href')
    time.sleep(0.2)
    driver.get(check_url)
    # driver.get("https://referloan.in/credit-card/yes-bank-credit-card")
    time.sleep(1.2)
    # check=driver.find_element(By.XPATH,"//img[@class='p-4']").text
    check=driver.find_element(By.XPATH,"//img[@class='p-4']").size
    # print(check)
    if (check["height"]==308) and (check["width"]==1296):
        continue
        # print("Image Found in",driver.find_element(By.XPATH,"//span[contains(@style,'text-transform')]").text)
    else:
        print("Image Not Found in",driver.find_element(By.XPATH,"//span[contains(@style,'text-transform')]").text)
    # if check_text==check_last:
    #     break
time.sleep(3)
driver.close()
