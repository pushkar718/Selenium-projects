from selenium import webdriver
import time
import subprocess
from selenium.webdriver.chrome.options import Options
from slack_sdk.webhook import WebhookClient
import url
import requests

chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()

try:
    url = url.slack_url()
    webhook = WebhookClient(url)
    driver.get("https://qa.referloan.in")
    response = requests.get("https://qa.referloan.in")
    while True:
        for i in range(0,1000):
            driver.refresh()
            time.sleep(2)
            if 'Refer' in driver.title:
                if i<1:
                    subprocess.Popen(['notify-send', "QA REFERLOAN IS WORKING AGAIN"])
                    response=webhook.send(text="QA REFERLOAN IS WORKING AGAIN")
                    time.sleep(60)
                else:
                    time.sleep(60)
            else:
                subprocess.Popen(['notify-send', "QA IS DOWN WITH STATUS CODE: %d" % response.status_code])
                response = webhook.send(text="QA IS DOWN")
                time.sleep(60)
                break
except KeyboardInterrupt:
    print("Stopped By User..!")
except:
    print("Some More Error Here")