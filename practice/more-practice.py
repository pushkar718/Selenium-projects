from selenium import webdriver
import time
import subprocess
from selenium.webdriver.chrome.options import Options
from slack_sdk.webhook import WebhookClient
# import url
import requests

chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()

try:
    while True:
        # url = url.slack_url()
        # webhook = WebhookClient(url)
        driver.get("https://qa.referloan.in")
        response = requests.get("https://qa.referloan.in")
        # subprocess.Popen(['notify-send', "QA IS DOWN WITH STATUS CODE: %d"%response.status_code])
        if 'refer' in driver.title.lower():
            print(driver.title.lower())
        else:
            print(driver.title)
        time.sleep(6)
except KeyboardInterrupt:
    print("Stopped By User..!")
except:
    print("Some More Error Here")