import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://qa.referloan.in/loans/kreditbee-personal-loan")
time.sleep(2)

if driver.find_element(By.XPATH, "//*[@class='display-3']").is_displayed() == True:
    screenshot = driver.find_element(By.XPATH, "//div[@class='jumbotron text-center']")
    screenshot.screenshot(
    driver.find_element(By.XPATH, "//span[contains(@style,'text-transform: capitalize')]").text + ".png")
else:
    print("Not available")