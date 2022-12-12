from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py


# all_personal_file=open("All_personal_data.txt","w")
# temp_url="https://qa.referloan.in/apply-gold-loan"
name=NameGenerator.generator()
list_name=name.split()
pan_card=PanGenerator.generator(name)
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
for i in range(1,3):
    temp_url="https://qa.referloan.in/credit-card/standard-chartered-bank-credit-cards"
    driver.get(temp_url)
    time.sleep(3)
    with py.hold('ctrl'):
        py.press('-')
        py.press('-')
        py.press('-')
        py.press('-')
        py.press('-')

    full_name = driver.find_element(By.XPATH,
                                        "//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
    action.move_to_element(full_name).perform()
    full_name.click()
    action.send_keys(name).perform()
    phone_number = driver.find_element(By.XPATH,
                                           "//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
    action.move_to_element(phone_number).perform()
    phone_number.click()
    action.send_keys(int(9717156422)).perform()
    otp_box = driver.find_element(By.XPATH, "//input[@id='otpCheckbox']")
    action.move_to_element(otp_box).perform()
    otp_box.click()
    submit_button = driver.find_element(By.XPATH, "//button[@class='mt-4']")
    action.move_to_element(submit_button).perform()
    submit_button.click()
    time.sleep(0.8)
    # user_otp = py.prompt("Found OTP Page, Please enter the OTP to continue")
    otp_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiInput-input']")
    otp_field.click()
    time.sleep(0.5)
    # action.send_keys(user_otp).perform()
    time.sleep(0.5)
    verify_otp = driver.find_element(By.XPATH, "//button[@class='mt-4']").click()
    time.sleep(0.8)
    # last_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[last()]").text
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
# for i in range(1,30):
#
#     # print(element)
#     element = driver.find_element(By.XPATH,
#                                   "(//*[contains(@class,'MuiFormControl-root')])[%d]/descendant-or-self::*" % (i))
#     element_last = driver.find_element(By.XPATH,
#                                        "(//*[contains(@class,'MuiFormControl-root')])[last()]/descendant-or-self::*")
#     element_inner = element.get_attribute('innerHTML')
#     element_text = element.text
#
#     if 'select' in element_inner:
#         print("select -",element_text)
#     elif 'input' in element_inner:
#         print("input -",element_text)
#     if element == element_last:
#         break

time.sleep(2)
driver.close()