from selenium import webdriver
import time
import subprocess
from selenium.webdriver.chrome.options import Options
from slack_sdk.webhook import WebhookClient
import url

#
chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()

try:
    # url = url.slack_url()
    # webhook = WebhookClient(url)
    # response = webhook.send(text=message)
    while True:
        for i in range(0,1000):
            driver.get("https://qa.referloan.in")
            time.sleep(2)
            if 'Refer' not in driver.title:
                subprocess.Popen(['notify-send', "QA IS DOWN"])
                # response = webhook.send(text="QA IS DOWN")
                time.sleep(60)
                break
            else:
                if i<=1:
                    message="QA REFERLOAN IS WORKING AGAIN"
                    subprocess.Popen(['notify-send', "QA REFERLOAN IS WORKING AGAIN"])
                    # response = webhook.send(text="QA REFERLOAN IS WORKING AGAIN")
                    time.sleep(60)
except KeyboardInterrupt:
    print("Stopped By User..!")
except:
    print("Some More Error Here")