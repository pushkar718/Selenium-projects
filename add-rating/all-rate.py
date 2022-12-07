from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# chrome_options=Options()
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(options=chrome_options)
driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
driver.get("https://qa.referloan.in")
time.sleep(2)
check_last=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[last()]")
check_last_url=check_last.get_attribute('href')
try:
    for b in range(1,500):
        check=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[%d]"%(b))
        check_url=check.get_attribute('href')
        time.sleep(1)
        driver.get(check_url)
        time.sleep(2)
        page_name = driver.find_element(By.XPATH, "//span[contains(@style,'text-transform')]").text
        driver.execute_script("window.scrollTo(0,250)")
        time.sleep(1)
        for i in range(random.randint(100,120)):# Change 65,80 to min,max of rating for 5 star
            driver.find_element(By.XPATH,"(//span[@class='star'])[5]").click()
        for i in range(random.randint(30,40)):# Change 30,40 to min,max of rating for 4 star
            driver.find_element(By.XPATH,"(//span[@class='star'])[4]").click()
        for i in range(random.randint(0,20)):  # Change 0,0 to min,max of rating for 3 star
            driver.find_element(By.XPATH, "(//span[@class='star'])[3]").click()
        for i in range(random.randint(0,10)):  # Change 0,0 to min,max of rating for 2 star
            driver.find_element(By.XPATH, "(//span[@class='star'])[2]").click()
        for i in range(random.randint(0,3)):  # Change 0,0 to min,max of rating for 1 star
            driver.find_element(By.XPATH, "(//span[@class='star'])[1]").click()
            time.sleep(2)
            print(page_name, "---Done---")
        if check_url==check_last_url:
            break
except(KeyboardInterrupt):
    print("Stopped By User..!")
except:
    print("Stopped with an unknown error..! Contact dev for details")

time.sleep(2)
driver.close()