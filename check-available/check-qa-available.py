import subprocess
import urllib.request,requests,time
import url
from slack_sdk.webhook import WebhookClient


# CODE TO CHECK REFERLOAN.IN AVAILABLITY
url = url.slack_url()
webhook = WebhookClient(url)
def check(chost="https://google.com"):
    global check_response
    try:
        check_response=requests.get(chost)
        subprocess.Popen(["notify-send", "Internet Working"])
        urllib.request.urlopen(chost)
        return True
    except:
        check_response=subprocess.Popen(["notify-send","Internet Not Working"])
        return False
def connect(host='http://referloan.in'):
    global response
    try:
        response=requests.get(host)
        urllib.request.urlopen(host)
        # subprocess.Popen(["notify-send", "Successfully connected to referloan..!"])
        return True
    except:
        if response.status_code!=200:
            response = webhook.send(text="Referloan is DOWN with status code %d"%response.status_code)
        subprocess.Popen(["notify-send", "Internet Not Working"])
        return False

if __name__=="__main__":
    time.sleep(5)
    while True:
        if check():
            time.sleep(5)
            while True:
                if connect():
                    time.sleep(60)
                else:
                    time.sleep(5)
                    break
        else:
            time.sleep(5)
            # END CODE