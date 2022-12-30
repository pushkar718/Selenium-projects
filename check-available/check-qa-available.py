import requests
from selenium import webdriver
import urllib.request
import time
import subprocess
from selenium.webdriver.chrome.options import Options
from slack_sdk.webhook import WebhookClient
import url

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
# test
while True:
    time.sleep(2)
    if connect():
        time.sleep(3)
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(options=chrome_options)
        # driver=webdriver.Chrome()
        driver.maximize_window()
        try:
            url = url.slack_url()
            webhook = WebhookClient(url)
            driver.get("https://qa.referloan.in")
            response=requests.get("https://qa.referloan.in")
            while True:
                for i in range(0,1000):
                    driver.refresh()
                    time.sleep(2)
                    if 'Refer' in driver.title:
                        if i<1:
                            subprocess.Popen(['notify-send', "QA IS WORKING NOW"])
                            response=webhook.send(text="QA REFERLOAN IS WORKING AGAIN")
                            time.sleep(60)
                        else:
                            time.sleep(60)
                    else:
                        response = webhook.send(text="QA IS DOWN WITH STATUS CODE %d"%response.status_code)
                        subprocess.Popen(['notify-send', "QA IS DOWN WITH STATUS CODE: %d" % response.status_code])
                        time.sleep(60)
                        break
        except KeyboardInterrupt:
            print("Stopped By User..!")
        except Exception as e:
            print("Some More Error Here")
            print(e)
    else:
        continue
