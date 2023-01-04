from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py


driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
final_dob = "10" + "10" + str(random.randint(1980, 2000))
test_number='8240281075'
name=NameGenerator.generator()
temp_url=py.prompt("Enter URL: ")
list_name=name.split()
# temp_url="https://qa.referloan.in/loans/axis-bank-home-loan"
pan_card=PanGenerator.generator(name)
time.sleep(0.5)
driver.get(temp_url)
time.sleep(3)
with py.hold('ctrl'):
    py.press('-')
    py.press('-')
    py.press('-')
    py.press('-')
    py.press('-')
try:
        driver.find_element(By.ID, "salary").click()
        time.sleep(0.1)
        driver.find_element(By.ID, "salary").clear()
        action.send_keys(random.randint(10000, 60000)).perform()
        time.sleep(0.5)
        driver.find_element(By.ID, "pincode").click()
        time.sleep(0.1)
        action.send_keys(random.randint(100000, 999999)).perform()
        time.sleep(0.6)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/form/div[4]/button").click()
        time.sleep(2)
        driver.get(temp_url)
        driver.implicitly_wait(10)
        time.sleep(0.4)
except NoSuchElementException:
    # while driver.find_elements(By.XPATH,):
        try:
            full_name = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
            action.move_to_element(full_name).perform()
            full_name.click()
            full_name.clear()
            action.send_keys(name).perform()
            phone_number = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
            action.move_to_element(phone_number).perform()
            phone_number.click()
            action.send_keys(test_number).perform()
            otp_box = driver.find_element(By.XPATH, "//input[@id='otpCheckbox']")
            action.move_to_element(otp_box).perform()
            otp_box.click()
            submit_button = driver.find_element(By.XPATH, "//button[@class='mt-4']")
            action.move_to_element(submit_button).perform()
            submit_button.click()
            time.sleep(0.8)
            user_otp = py.prompt("Found OTP Page, Please enter the OTP to continue")
            otp_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiInput-input']")
            otp_field.click()
            time.sleep(0.5)
            action.send_keys(user_otp).perform()
            time.sleep(0.5)
            submit_button = driver.find_element(By.XPATH, "//button[@class='mt-4']")
            submit_button.click()
            time.sleep(0.8)
            last_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[last()]").text
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            restart = True
            while restart:
                restart=False
                print("-" * 5, driver.find_element(By.XPATH,
                                                   "//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]").text,
                      "-" * 5)
                for i in range(1,300):
                    random_number=str(random.randint(100,999))+'000'
                    random_salary=str(random.randint(50,100))+'000'
                    available_option=[]
                    element = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]/descendant-or-self::*" % (i))
                    element_last = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]/descendant-or-self::*")
                    element_inner = element.get_attribute('innerHTML')
                    element_text = element.text
                    if 'select' in element_inner:
                        if element.is_displayed() == True:
                            element.click()
                            all_options = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]")
                            all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for input in range(1, 100):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (input)).text
                                available_option.append(all_options_text)
                                for select_option in available_option:
                                    if 'select option' in select_option.lower():
                                        available_option.remove(select_option)
                                if all_options_text == all_options_last:
                                    for select_option in available_option:
                                        if 'select option' in select_option.lower():
                                            available_option.remove(select_option)
                                    selected_option = random.choice(available_option)
                                    options=(driver.find_element(By.XPATH,"//ul/li/em[text()='"+selected_option+"']"))
                                    options.click()
                                    print(element_text,"->", selected_option)
                                    break
                    elif 'input' in element_inner:
                        if element.is_displayed()==True:
                            if ('mobile' in element_text.lower())or('phone' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(test_number).perform()
                                print(element_text, "->", test_number)
                            elif 'address proof' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(test_number).perform()
                                print(element_text, "->", test_number)
                            elif 'email' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("tester123@gmail.com").perform()
                                print(element_text, "->", 'tester123@gmail.com')
                            elif ('bank name' in element_text.lower())or('bank code' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("IDFC").perform()
                                print(element_text, "->", "IDFC")
                            elif ('credit score' in element_text.lower()):
                                random_number=random.randint(650,850)
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(random_number).perform()
                                print(element_text, "->", random_number)
                            elif ('credit bureau' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Equifax").perform()
                                print(element_text, "->", "Equifax")
                            elif 'first name' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(list_name[0]).perform()
                                print(element_text, "->", list_name[0])
                            elif ('last name' in element_text.lower())or('middle name' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(list_name[1]).perform()
                                print(element_text, "->", list_name[1])
                            elif ('full name' in element_text.lower())or('name' in element_text.lower())or('company *' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(name).perform()
                                print(element_text, "->", name)
                            elif ('amount' in element_text.lower())or('rent' in element_text.lower())or('emi' in element_text.lower())or('salary' in element_text.lower())or('income' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(random_salary).perform()
                                print(element_text, "->", random_salary)
                            elif ('pincode' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(random_number).perform()
                                print(element_text, "->", random_number)

                            elif ('months at' in element_text.lower())or('exp' in element_text.lower())or('tenure' in element_text.lower())or('working since' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("8").perform()
                                print(element_text, "->", "8")
                            elif ('address' in element_text.lower())or('landmark' in element_text.lower())or('street' in element_text.lower())or('house' in element_text.lower())or('land mark' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Dummy Address 123").perform()
                                print(element_text, "->", "Dummy Address 123")
                            elif ('city' in element_text.lower())or('state' in element_text.lower())or('locality' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Delhi").perform()
                                print(element_text, "->", "Delhi")
                            elif ('pan' in element_text.lower())or('pancard' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys(pan_card).perform()
                                print(element_text, "->", pan_card)
                            elif ('document number' in element_text.lower())or('aadhaar' in element_text.lower())or('number' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("562453123535").perform()
                                print(element_text, "->", "562453123535")
                            elif 'ifsc' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("IDFB0020158").perform()
                                print(element_text, "->", "IDFB0020158")
                            elif 'type' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Dummy Type").perform()
                                print(element_text, "->", "Dummy Type")
                            elif 'care of' in element_text.lower():
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Dummy Care").perform()
                                print(element_text, "->", "Dummy Care")
                            elif ('dist' in element_text.lower()):
                                element.click()
                                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
                                action.send_keys("Delhi").perform()
                                print(element_text, "->", "Delhi")
                            elif ('date' in element_text.lower()) or ('birth' in element_text.lower()) or('dob' in element_text.lower()):
                                element.click()
                                action.double_click(element).perform()
                                dob_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                                if dob_check == "":
                                    action.send_keys(final_dob).perform()
                                    print(element_text,"->", final_dob)
                                else:
                                    continue
                    if element == element_last:
                        driver.find_element(By.XPATH,"//button[@class='mt-4']").click()
                        time.sleep(2)
                        if (driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]")):
                            if 'Thank You' in driver.find_element(By.TAG_NAME, "html").text:
                                # screenshot = driver.find_element(By.XPATH, "/html/body/div/div/section[1]/div[2]/div")
                                # with py.hold('ctrl'):
                                #     py.press('+')
                                #     py.press('+')
                                #     py.press('+')
                                #     py.press('+')
                                # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                                # time.sleep(0.2)
                                # driver.execute_script("window.scrollTo(0,200)")
                                # time.sleep(0.8)
                                # screenshot.screenshot(driver.find_element(By.XPATH,"//span[contains(@style,'text-transform: capitalize')]").text + ".png")
                                print("-" * 5, driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]").text,"-" * 5)

                                time.sleep(2000)
                                break
                            # else:
                                # print("-" * 5, driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]").text, "-" * 5)
                        restart = True
                        break
        # except NoSuchElementException:
        #     for i in range(1, 300):
        #         if driver.find_element(By.XPATH,
        #                                "(//*[contains(@class,'mt-2 form-control')])/descendant-or-self::*").is_displayed() == True:
        #             document = driver.find_element(By.XPATH,
        #                                            "(//*[contains(@class,'mt-2 form-control')])/descendant-or-self::*")
        #             document.send_keys("/home/wolfie/pythonProject/Selenium-projects/practice/send.png")
        #             time.sleep(3)
        #             print('Upload document here..!')
        #         available_option = []
        #         element = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]/descendant-or-self::*" % (i))
        #         element_last = driver.find_element(By.XPATH,
        #                                            "(//*[contains(@class,'MuiFormControl-root')])[last()]/descendant-or-self::*")
        #         element_inner = element.get_attribute('innerHTML')
        #         element_text = element.text
        #         if 'select' in element_inner:
        #             if element.is_displayed() == True:
        #                 element.click()
        #                 all_options = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]")
        #                 all_options_text = driver.find_element(By.XPATH,
        #                                                        "//li[contains(@class,'MuiButtonBase-root')]").text
        #                 all_options_last = driver.find_element(By.XPATH,
        #                                                        "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
        #                 for input in range(1, 50):
        #                     all_options_text = driver.find_element(By.XPATH,
        #                                                            "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (
        #                                                                input)).text
        #                     available_option.append(all_options_text)
        #                     for select_option in available_option:
        #                         if 'select option' in select_option.lower():
        #                             available_option.remove(select_option)
        #                     if all_options_text == all_options_last:
        #                         for select_option in available_option:
        #                             if 'select option' in select_option.lower():
        #                                 available_option.remove(select_option)
        #                         selected_option = random.choice(available_option)
        #                         options = (
        #                             driver.find_element(By.XPATH, "//ul/li/em[text()='" + selected_option + "']"))
        #                         options.click()
        #                         print(element_text, "->", selected_option)
        #                         break
        #         elif 'input' in element_inner:
        #             if element.is_displayed() == True:
        #                 # if ('office mobile' in element_text.lower())or('office phone' in element_text.lower()):
        #                 #     element.click()
        #                 #     action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        #                 #     action.send_keys('0'+test_number).perform()
        #                 #     # time.sleep(1)
        #                 #     print(element_text, "->", '0'+test_number)
        #                 if ('type' in element_text.lower()) or ('file' in element_text.lower()):
        #                     element.click()
        #                     action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
        #                         Keys.BACKSPACE).perform()
        #                     action.send_keys("PNG").perform()
        #                     print(element_text, "->", "PNG")
        #         if element == element_last:
        #             driver.find_element(By.XPATH, "//button[@class='mt-4']").click()
        #             time.sleep(2)
        #             if (driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]")):
        #                 if 'Thank You' in driver.find_element(By.TAG_NAME, "html").text:
        #                     print("-" * 5, driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]").text,"-" * 5)
        #                     time.sleep(2000)
        #                     break
        #                 # else:
        #                 # print("-" * 5, driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other') or contains(text(),'Info') or contains(text(),'KYC') or contains(text(),'Customer') or contains(text(),'info')]").text, "-" * 5)
        #             restart = True
        #             break
        except Exception as e:
            time.sleep(2000)
            print(e)

except KeyboardInterrupt:
    print("\n\nStopped by user..!")
    exit(1)
except NoSuchWindowException:
    print("Window already closed")
except Exception as e:
    time.sleep(2000)
    print(e)
    # driver.close()
