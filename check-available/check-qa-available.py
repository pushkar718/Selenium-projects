import subprocess
import urllib.request,url,requests,time
from slack_sdk.webhook import WebhookClient


# CODE TO CHECK REFERLOAN.IN AVAILABLITY
url = url.slack_url()
webhook = WebhookClient(url)
def check(chost="https://google.com"):
    global check_response
    try:
        check_response=requests.get(chost)
        subprocess.Popen(["notify-send", "Connected to google..!"])
        urllib.request.urlopen(chost)
        return True
    except:
        check_response=subprocess.Popen(["notify-send","Cannot connect to google..!"])
        return False
def connect(host='http://referloan.in'):
    global response
    try:
        response=requests.get(host)
        urllib.request.urlopen(host)
        return True
    except:
        response = webhook.send(text="Referloan is DOWN with status code %d"%response.status_code)
        return False

if __name__=="__main__":
    time.sleep(5)
    if check():
        while True:
            try:
                connect()
                time.sleep(60)
            except:
                continue
        # END CODE