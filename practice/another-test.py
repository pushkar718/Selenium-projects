from selenium import webdriver
import time
import subprocess
from selenium.webdriver.chrome.options import Options


chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()
while True:
    driver.get("https://qa.referloan.in")
    time.sleep(2)
    if 'Refer' not in driver.title:
        subprocess.Popen(['notify-send', "QA IS DOWN"])
        time.sleep(60)
    else:
        subprocess.Popen(['notify-send', "QA REFERLOAN IS UP, GET BACK TO WORK"])
        time.sleep(60)