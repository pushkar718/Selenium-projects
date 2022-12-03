from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random
from selenium.webdriver import *
import time


def testing_form_1():
    driver=webdriver.Chrome()
    driver.find_element(By.NAME,"full_name").send_keys("Qa Qa")
    driver.find_element(By.NAME, "phone_no").send_keys("9717156422")
    driver.find_element(By.ID,"otpCheckbox").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "mt-4").click()