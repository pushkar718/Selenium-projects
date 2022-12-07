from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py

driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
driver.get("https://qa.referloan.in/loans/kreditbee-personal-loan")
time.sleep(3)
full_name_text=NameGenerator.generator()
pan_card=PanGenerator.generator(full_name_text)
with py.hold('ctrl'):
    py.press('-')
    py.press('-')
    py.press('-')
    py.press('-')
    py.press('-')
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
scroll_form=driver.find_element(By.XPATH,"(//*[@id='apply-banner'])[1]")
driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
full_name=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
action.move_to_element(full_name).perform()
full_name.click()
action.send_keys(full_name_text).perform()
phone_number=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
action.move_to_element(phone_number).perform()
phone_number.click()
action.send_keys(int(9667484050)).perform()
otp_box=driver.find_element(By.XPATH,"//input[@id='otpCheckbox']")
action.move_to_element(otp_box).perform()
otp_box.click()
submit_button=driver.find_element(By.XPATH,"//button[@class='mt-4']")
action.move_to_element(submit_button).perform()
submit_button.click()
time.sleep(0.8)
user_otp=py.prompt("Found OTP Page, Please enter the OTP to continue")
otp_field=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input']")
otp_field.click()
time.sleep(0.5)
action.send_keys(user_otp).perform()
time.sleep(0.5)
verify_otp=driver.find_element(By.XPATH,"//button[@class='mt-4']").click()
time.sleep(0.8)
last_element=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text
restart=True
while restart:
    restart=False
    for i in range(1,30):
        time.sleep(0.2)
        available_option=[]
        every_element=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiInputBase-root')])[%d]"%(i))
        every_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (i)).text
        # print(every_element_text)
        if 'mobile' in every_element_text.lower():
            if driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']"):
                every_element.click()
                action.send_keys(9667484050).perform()
        elif 'email' in every_element_text.lower():
            if driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']"):
                every_element.click()
                action.send_keys("qa@gmail.com").perform()
        elif 'pan' in every_element_text.lower():
            if driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']"):
                every_element.click()
                action.send_keys(pan_card).perform()
        elif 'first' in every_element_text.lower():
            if driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']"):
                every_element.click()
                action.send_keys(full_name_text).perform()
        elif 'Last' in every_element_text.lower():
            if driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']"):
                every_element.click()
                action.send_keys("qa@gmail.com").perform()
        elif 'gender' in every_element_text.lower():
            every_element.click()
            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
            for i in range(1, 5):
                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                available_option.append(all_options_text)
                if all_options_text == all_options_last:
                    selected_option = random.choice(available_option)
                    driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                    # print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (i)).text, "->",selected_option)
                    break
                else:
                    continue
        elif 'pin' in every_element_text.lower():
            every_element.click()
            action.send_keys(random.randint(10000,999999)).perform()
        elif ('Date' in every_element_text) or ('Birth' in every_element_text) or ('DOB' in every_element_text) or ('dob' in every_element_text):
            every_element.click()
            action.double_click(every_element).perform()
            dob_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
            if dob_check == "":
                final_dob = "10" + "10" + str(random.randint(1960, 2022))
                if len(final_dob) <= 7:
                    final_dob = '0' + final_dob
                    if len(final_dob) == 7:
                        final_dob = final_dob[:2] + '0' + final_dob[2:]
                        final_dob = int(final_dob)
                        action.send_keys(final_dob).perform()
                    else:
                        final_dob = int(final_dob)
                        action.send_keys(final_dob).perform()
                else:
                    final_dob = int(final_dob)
                    action.send_keys(final_dob).perform()

        if 'Employee Type' in every_element_text:
            every_element.click()
            time.sleep(0.3)
            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
            for i in range(1, 10):
                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                available_option.append(all_options_text)
                if all_options_text == all_options_last:
                    if 'Select option' in available_option:
                        available_option.remove('Select option')
                        selected_option = random.choice(available_option)
                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (i)).text, "->", selected_option)
                        break
                    else:
                        selected_option = random.choice(available_option)
                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (i)).text, "->", selected_option)
                        break

        if every_element_text==last_element:
            break
    submit_button=driver.find_element(By.XPATH,"//button[@class='mt-4']")
    submit_button.click()
    time.sleep(1.5)
    if driver.find_element(By.XPATH, "//*[@class='display-3']").is_displayed() == True:
        screenshot = driver.find_element(By.XPATH, "//div[@class='jumbotron text-center']")
        screenshot.screenshot(driver.find_element(By.XPATH, "//span[contains(@style,'text-transform: capitalize')]").text + ".png")
    else:
        restart=True

time.sleep(2)
driver.close()