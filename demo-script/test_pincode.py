from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import form_1
from selenium import *
import time

        # CODE HERE

def testing_pincode():
    drop_list=["Home Loan","Personal Loan","Business Loan","Gold Loan","Loan Against Property","Builder Loan","Hospital Loan","Used Car Loan","New Car Loan","Education Loan","Working Capital OD Limit"]
    driver=webdriver.Chrome()
    driver.maximize_window()
    try:
        for i in range(0,10):
            if i ==1:
                try:
                    choice = random.choice(drop_list)
                    driver.get("https://qa.referloan.in")
                    time.sleep(1)
                    select = Select(driver.find_element(By.NAME, "product_id"))
                    time.sleep(1)
                    select.select_by_visible_text(choice)
                    driver.find_element(By.ID, "salary").send_keys("11")
                    driver.find_element(By.ID, "pincode").send_keys("1234")
                    time.sleep(1)
                    if driver.find_element(By.XPATH,"//*[contains(text(),'Invalid')]").is_displayed() == True:
                        print("Invalid Pincode error on pincode less than 6 digits")
                    driver.find_element(By.CLASS_NAME, "search-button").click()
                    time.sleep(2)
                    driver.find_element(By.XPATH,"//a[@class='grabDeal' and (contains(@href, 'tata-capital') or contains(@href, 'icici') or contains(@href, 'finance-peer') or contains(@href, 'hero-fin') or contains(@href,'axis-bank') or contains(@href,'ruptok-gold') or contains(@href, 'apply-gold-loan'))]").click()
                    time.sleep(5)
                    # driver.close()
                except:
                    print("")

            elif i==2:
                try:
                    choice = random.choice(drop_list)
                    driver.get("https://qa.referloan.in")
                    time.sleep(1)
                    select = Select(driver.find_element(By.NAME, "product_id"))
                    time.sleep(1)
                    select.select_by_visible_text(choice)
                    driver.find_element(By.ID, "salary").send_keys("11")
                    driver.find_element(By.ID, "pincode").send_keys("123456789")
                    time.sleep(1)
                    if driver.find_element(By.XPATH,"//*[contains(text(),'Invalid')]").is_displayed() == True:
                        print("Invalid Pincode error on pincode more than 6 digits")
                    time.sleep(1)
                    driver.find_element(By.CLASS_NAME, "search-button").click()
                    time.sleep(2)
                    driver.find_element(By.XPATH,"//a[@class='grabDeal' and (contains(@href, 'tata-capital') or contains(@href, 'icici') or contains(@href, 'finance-peer') or contains(@href, 'hero-fin') or contains(@href,'axis-bank') or contains(@href,'ruptok-gold') or contains(@href, 'apply-gold-loan'))]").click()
                    time.sleep(5)
                    # driver.close()
                except:
                    print("")

            elif i==3:
                try:
                    choice = random.choice(drop_list)
                    driver.get("https://qa.referloan.in")
                    time.sleep(1)
                    select = Select(driver.find_element(By.NAME, "product_id"))
                    # time.sleep(1)
                    select.select_by_visible_text(choice)
                    driver.find_element(By.ID, "salary").send_keys("11")
                    driver.find_element(By.ID, "pincode").send_keys("123456")
                    # time.sleep(1)
                    driver.find_element(By.CLASS_NAME, "search-button").click()
                    time.sleep(2)
                    if driver.find_element(By.XPATH,"//a[@class='grabDeal' and (contains(@href, 'tata-capital') or contains(@href, 'icici') or contains(@href, 'finance-peer') or contains(@href, 'hero-fin') or contains(@href,'axis-bank') or contains(@href,'ruptok-gold') or contains(@href, 'apply-gold-loan'))]").is_displayed() ==False:
                        driver.execute_script("windows.scrollBy(0,250)","")
                        driver.find_element(By.XPATH,"//a[@class='grabDeal' and (contains(@href, 'tata-capital') or contains(@href, 'icici') or contains(@href, 'finance-peer') or contains(@href, 'hero-fin') or contains(@href,'axis-bank') or contains(@href,'ruptok-gold') or contains(@href, 'apply-gold-loan'))]").click()
                        time.sleep(2)
                    else:
                        driver.find_element(By.XPATH,"//a[@class='grabDeal' and (contains(@href, 'tata-capital') or contains(@href, 'icici') or contains(@href, 'finance-peer') or contains(@href, 'hero-fin') or contains(@href,'axis-bank') or contains(@href,'ruptok-gold') or contains(@href, 'apply-gold-loan'))]").click()
                        # time.sleep(5)
                        time.sleep(2)
                except:
                    print("")
            else:
                driver.get("https://qa.referloan.in")
                time.sleep(5)
                action = ActionChains(driver)
                action.move_to_element(driver.find_element(By.LINK_TEXT,"Card")).perform()
                time.sleep(1)
                action.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT,"Card By Bank")).perform()
                time.sleep(1)
                action.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT,"Kotak")).click().perform()
                time.sleep(3)
        driver.close()
    except:
        print("")
    # CODE END