from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess
from selenium.webdriver.chrome.options import Options

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.referloan.in")
time.sleep(2)
driver.find_element(By.TAG_NAME,"html")
driver.execute_script("document.body.style.zoom='50%'")

time.sleep(2)
driver.close()