from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
driver.get("https://referloan.in")
time.sleep(3)
no_profile=open("No-Profile.txt",'w')
try:
    for b in range(1,500):
        check=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[%d]"%(b))
        check_text = driver.find_element(By.XPATH, "(//ul/li/a[@tabindex='-1'])[%d]" % (b)).text
        check_last=driver.find_element(By.XPATH,"(//ul/li/a[@tabindex='-1'])[last()]").text
        check_url=check.get_attribute('href')
        time.sleep(0.2)
        driver.get(check_url)
        time.sleep(1.2)
        check_banner=driver.find_element(By.XPATH,"//img[@class='p-4']").size
        check_profile=driver.find_element(By.XPATH,"//div[@class='CardImg_box']").size
        if (check_banner["height"]==214) and (check_banner["width"]==340):
            continue
        else:
            print("Profile Not Found in",driver.find_element(By.XPATH,"//span[contains(@style,'text-transform')]").text)
            no_banner.write("Profile Not Found in "+driver.find_element(By.XPATH,"//span[contains(@style,'text-transform')]").text)
            no_banner.write("\n")
except:
    time.sleep(3)
    driver.close()
