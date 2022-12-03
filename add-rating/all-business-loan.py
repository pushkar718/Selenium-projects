from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

loan_list=["Hero Fincorp Business Loan",
"Faircent Business Loan",
"HDFC Bank Business Loan",
"IDFC Bank Business Loan",
"ICICI Bank Business Loan",
"Bajaj Finserv Business Loan",
"Tata Capital Business Loan",
"Poonawala Finance Business Loan",
"Lendingkart Business Loan",
"Loan Tap Business Loan",
"Fusion Business Loan",
"Growth Source Business Loan",
"Unity Bank Business Loan",
"Ashv Finance Business Loan",
"Piramal Finance Business Loan"]
driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
for i in loan_list:
    driver.get("https://referloan.in/")
    time.sleep(2)
    list=driver.find_element(By.XPATH,"//*[@class='hasSub_menu' and contains(text(),'Loan')]")
    action.move_to_element(list).perform()
    action.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT,'Business Loan')).perform()
    action.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT,i)).click().perform()
    time.sleep(2)
    try:
        driver.execute_script("window.scrollTo(0,250)")
        time.sleep(3)
        for i in range(random.randint(65,80)):
            driver.find_element(By.XPATH,"(//span[@class='star'])[5]").click()
        for i in range(random.randint(30,40)):
            driver.find_element(By.XPATH,"(//span[@class='star'])[4]").click()
        time.sleep(2)
    except:
        print("Stopped by user..!")


time.sleep(2)
driver.close()