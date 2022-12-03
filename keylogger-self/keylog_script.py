from selenium import webdriver
import pyautogui
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pynput.mouse import Listener
import time

def on_click(x,y,button,pressed):
    if pressed:
        print(x,y)
        return x,y

with Listener(on_click=on_click) as listener:


    url="https://referloan.in/loans/paysense-personal-loan"

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(7)


    for b in range(1,5):
            field = driver.find_element(By.XPATH,"(//label[contains(@class,'MuiInputLabel-root')]//parent::label[@data-shrink='true'])[%d]"%(b)).text
            if b>=3:
                if b==3:
                    answer=driver.find_element(By.XPATH,"(//*[@class='MuiInputBase-input MuiInput-input css-mnn31'])[1]").get_attribute('value')
                    print(field, ':', answer)
                elif b==4:
                    answer = driver.find_element(By.XPATH,"(//*[@class='MuiInputBase-input MuiInput-input css-mnn31'])[2]").get_attribute('value')
                    print(field, ':', answer)
            else:
                answer = (driver.find_element(By.XPATH, '(//div/em)[%d]' % (b)).text)
                print(field, ':', answer)
    time.sleep(2)
    driver.close()
    listener.join()
    listener.stop()
