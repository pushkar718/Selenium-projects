from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# NoSuchWindowException
from selenium.common.exceptions import *
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py



lower_api=[]
list_api=["STANDARD CHARTERED bank personal","STANDARAD CHARTERED Credit card","INDIA GOLD ","TATA CAPITAL USED CAR LOAN ","FAIRCENT PERSONAL","WERIZE PERSONAL","MONEYWIDE PERSONAL","ICICI BUSINESS LOAN OVERDRAFT","AXIS BANK CREDIT CARD","AXIS BANK SAVING ACCOUNT ","AU Bank Credit Card","Yes bank credit card","Cashe","Ruptok gold loan ","Finzy personal loan","Flex Salary ","Mpokket","kreditbee","paysense"]
for i in range(len(list_api)):
    list_api[i]=list_api[i].lower()
# all_personal_file=open("All_personal_data.txt","w")
name=NameGenerator.generator()
list_name=name.split()
pan_card=PanGenerator.generator(name)
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
driver.get("https://qa.referloan.in/")
time.sleep(3)
# with py.hold('ctrl'):
#     py.press('-')
#     py.press('-')
#     py.press('-')
#     py.press('-')
#     py.press('-')
# time.sleep(1)
try:
    for list_count in range(len(list_api)):
        for i in range(1,500):
            # py.prompt("continue")
            # with py.hold('ctrl'):
            #     py.press('-')
            #     py.press('-')
            #     py.press('-')
            #     py.press('-')
            #     py.press('-')
            all_personal = driver.find_element(By.XPATH,"(//*[@tabindex='-1'])[%d]" % (i))
            all_personal_text = all_personal.get_attribute('innerHTML')
            # print(all_personal_text.lower())
            all_personal_url = all_personal.get_attribute('href')
            all_personal_last = driver.find_element(By.XPATH,"(//*[@tabindex='-1'])[last()]").get_attribute('innerHTML')
            # print(list_api[api_list],"DEBUG")
            if list_api[list_count] in all_personal_text.lower():
                driver.get(all_personal_url)
                break
            else:
                continue





            # driver.get(all_personal_url)
            # driver.get(list_api[i])
                time.sleep(2)
                print("Filling",list_api[list_count],"Form\n\n")
                # all_personal_file.write("Filling %s Form\n"%(all_personal_text))
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(0.2)
                scroll_form = driver.find_element(By.XPATH, "(//*[@id='apply-banner'])[1]")
                driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
                full_name = driver.find_element(By.XPATH,
                                                "//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
                action.move_to_element(full_name).perform()
                full_name.click()
                action.send_keys("name").perform()
                phone_number = driver.find_element(By.XPATH,
                                                   "//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
                action.move_to_element(phone_number).perform()
                phone_number.click()
                action.send_keys(int(9667484050)).perform()
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
                verify_otp = driver.find_element(By.XPATH, "//button[@class='mt-4']").click()
                time.sleep(0.8)
                last_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[last()]").text
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(0.2)
                driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
                restart=True
                while restart:
                    restart=False
                    for inputs in range(1,25):
                        available_option = []
                        every_element = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs))
                        every_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
                        time.sleep(0.3)
                        last_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text
                        if 'Title' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
                            all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,13):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                selected_option=random.choice(available_option)
                                if all_options_text==all_options_last:
                                    driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root') and @data-value='"+selected_option+"']").click()
                                    print(driver.find_element(By.XPATH,"//label[contains(@class,'MuiFormLabel-root')][%d]"%(inputs)).text,"->",selected_option)
                                    break
                        elif 'Full Name' in every_element_text:
                            every_element.click()
                            full_name_text=driver.find_element(By.XPATH,"//input[@id='full_name']").text
                            if full_name_text=="":
                                selected_name=action.send_keys("name")
                                selected_name.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Test Name")
                            else:
                                continue
                        elif 'First Name' in every_element_text:
                            every_element.click()
                            first_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'First Name')]").text
                            first_name_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if first_name_check=="":
                                selected_name=action.send_keys(str(list_name[0]))
                                selected_name.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Test")
                            else:
                                continue
                        elif ('Last Name' in every_element_text)or('Middle Name' in every_element_text):
                            every_element.click()
                            last_name_text=driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                            last_name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if last_name_check=="":

                                time.sleep(0.1)
                                selected_name=action.send_keys(str(list_name[1]))
                                selected_name.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Name")
                            else:
                                continue
                        elif ('Phone' in every_element_text) or ('Mobile' in every_element_text)or ('phone' in every_element_text):
                            every_element.click()
                            phone_number_text=driver.find_element(By.XPATH,"//*[contains(text(), 'Phone') or contains(text(), 'Mobile') and contains(@class,'MuiFormLabel-root')]").text
                            check_phone=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_phone=="":

                                time.sleep(0.1)
                                selected_number=action.send_keys(int(9667484050))
                                selected_number.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","9667484050")
                            else:
                                continue
                        elif ('Email' in every_element_text)or('Email Address' in every_element_text):
                            every_element.click()
                            email_text=driver.find_element(By.XPATH,"//*[contains(text(),'Email')]").text
                            check_email = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_email=="":

                                time.sleep(0.1)
                                selected_email=action.send_keys("qa@gmail.com")
                                selected_email.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","qa@gmail.com")
                            else:
                                continue
                        elif 'Gender' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,5):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text==all_options_last:
                                    selected_option=random.choice(available_option)
                                    driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='"+selected_option+"']").click()
                                    print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text,"->",selected_option)
                                    break
                                else:
                                    continue
                        elif 'Loan Amount' in every_element_text:
                            every_element.click()
                            loan_amt_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if loan_amt_check=="":
                                selected_amt=action.send_keys(random.randint(20000,100000))
                                selected_amt.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",selected_amt)
                            else:
                                continue
                        elif ('Pincode' in every_element_text)or('Postal' in every_element_text):
                            every_element.click()
                            pincode_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if pincode_check=="":
                                generated_pincode=random.randint(100000,999990)
                                selected_pincode=action.send_keys(generated_pincode)
                                selected_pincode.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",generated_pincode)
                            else:
                                continue
                        elif ('Date' in every_element_text)or('Birth' in every_element_text)or('DOB' in every_element_text)or('dob' in every_element_text):
                            every_element.click()
                            action.double_click(every_element).perform()
                            dob_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if dob_check=="":
                                final_dob = "10" + "10" + str(random.randint(1960, 2022))
                                if len(final_dob) <= 7:
                                    final_dob = '0' + final_dob
                                    if len(final_dob) == 7:
                                        final_dob = final_dob[:2] + '0' + final_dob[2:]
                                        final_dob=int(final_dob)
                                        action.send_keys(final_dob).perform()
                                    else:
                                        final_dob = int(final_dob)
                                        action.send_keys(final_dob).perform()
                                else:
                                    final_dob = int(final_dob)
                                    action.send_keys(final_dob).perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",final_dob)
                            else:
                                continue
                        elif ('First name As Per Pancard' in every_element_text) or ('First Name As Per Pancard' in every_element_text):
                            every_element.click()
                            name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if name_check == "":
                                selected_name = action.send_keys(list_name[0])
                                selected_name.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", list_name[0])
                            else:
                                continue
                        elif ('Last Name As Per Pancard' in every_element_text) or ('Last name As Per Pancard' in every_element_text):
                            every_element.click()
                            name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if name_check == "":
                                selected_name = action.send_keys(list_name[1])
                                selected_name.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", list_name[1])
                            else:
                                continue
                        elif ('city' in every_element_text)or('City' in every_element_text):
                            every_element.click()
                            city_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if city_check=="":
                                city="Delhi"
                                selected_city=action.send_keys(city)
                                selected_city.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",city)
                            else:
                                continue
                        elif ('Pan' in every_element_text)or('PAN' in every_element_text):
                            every_element.click()
                            city_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if city_check=="":
                                selected_city=action.send_keys(pan_card)
                                selected_city.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",pan_card)
                            else:
                                continue
                        elif 'Marital' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,5):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                else:
                                    continue
                        elif 'Residence Type' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,10):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                else:
                                    continue
                        elif 'Qualification' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,10):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                else:
                                    continue
                        elif 'Occupation' in every_element_text:
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,10):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text==all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                    else:
                                        selected_option=random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='"+selected_option+"']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text,"->",selected_option)
                                        break
                                else:
                                    continue
                        elif ('Dependents' in every_element_text)or('Number Of Dependents'in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1,10):
                                all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", selected_option)
                                        break
                                else:
                                    continue

                        elif ('Type' in every_element_text)or('type' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Income' in every_element_text)or('Monthly Income' in every_element_text):
                            every_element.click()
                            income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if income_amt_check == "":
                                selected_amt = action.send_keys(random.randint(20000, 100000))
                                selected_amt.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",selected_amt)
                            else:
                                continue
                        elif ('Profession Type' in every_element_text)or('Professional Type' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Company name' in every_element_text) or ('Company Name' in every_element_text):
                            every_element.click()
                            company_name_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company name')or contains(text(),'Company Name')]").text
                            check_com_name = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_com_name == "":

                                time.sleep(0.1)
                                selected_name = action.send_keys(NameGenerator.generator())
                                selected_name.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",NameGenerator.generator())
                            else:
                                continue
                        elif ('Company Address' in every_element_text):
                            every_element.click()
                            company_addr_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company Address')or contains(text(),'Company address')]").text
                            check_add = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_add == "":
                                selected_name = action.send_keys("Dummy Address 123")
                                selected_name.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Dummy Address 123")
                            else:
                                continue
                        elif ('Years Stayed' in every_element_text) or ('Years stayed' in every_element_text):
                            every_element.click()
                            stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                            stayed_text_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if stayed_text_check == "":
                                time.sleep(0.1)
                                time_selected=random.randint(0,50)
                                selected_stayed = action.send_keys(time_selected)
                                selected_stayed.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", time_selected)
                            else:
                                continue
                        elif ('Address' in every_element_text):
                            every_element.click()
                            company_addr_text = driver.find_element(By.XPATH, "//*[contains(text(),'Address')or contains(text(),'address')]").text
                            check_add = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_add == "":
                                selected_name = action.send_keys("Dummy Address 123")
                                selected_name.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Dummy Address 123")
                            else:
                                continue
                        elif ('working Years' in every_element_text)or('Current Company Working Years' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Document Type' in every_element_text)or('Document type' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Salary Mode' in every_element_text)or('Salary mode' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Document number' in every_element_text) or ('Document Number' in every_element_text)or ('Document No' in every_element_text)or ('Document no' in every_element_text):
                            every_element.click()
                            company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company name')]").text
                            check_com_phone = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_com_phone == "":
                                selected_phone = action.send_keys("9876543210")
                                selected_phone.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","9876543210")
                            else:
                                continue
                        elif ('state' in every_element_text) or ('State' in every_element_text) or (
                                'Company State' in every_element_text):
                            every_element.click()
                            state_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if state_check == "":
                                state = "Delhi"
                                selected_state = action.send_keys(state)
                                selected_state.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", state)
                            else:
                                continue
                        elif ('Current Total Emi Paid Per Month' in every_element_text) or ('Paid Per Month' in every_element_text)or ('Total Emi' in every_element_text)or ('Emi Paid' in every_element_text):
                            every_element.click()
                            company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Emi')]").text
                            check_com_phone = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_com_phone == "":
                                selected_phone = action.send_keys(random.randint(20000, 100000))
                                selected_phone.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",selected_phone)
                            else:
                                continue
                        elif ('Bank Name' in every_element_text)or('Name Of Bank' in every_element_text):
                            every_element.click()
                            bank_name_text = driver.find_element(By.XPATH, "//*[contains(text(),'Bank name')or contains(text(),'Bank Name')]").text
                            check_bank = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_bank == "":
                                selected_bank = action.send_keys("Test Bank")
                                selected_bank.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Test Bank")
                            else:
                                continue
                        elif ('Email' in every_element_text) or ('Email Address' in every_element_text)or ('Email ID' in every_element_text)or ('Email Id' in every_element_text):
                            every_element.click()
                            email_text = driver.find_element(By.XPATH, "//*[contains(text(),'Email')]").text
                            check_email = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_email == "":
                                selected_email = action.send_keys("qa@gmail.com")
                                selected_email.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", "qa@gmail.com")
                            else:
                                continue
                        elif ('Designation' in every_element_text)or('Position' in every_element_text)or('Current Designation' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif ('Education' in every_element_text)or('Qualification' in every_element_text)or('qualification' in every_element_text):
                            every_element.click()
                            time.sleep(0.3)
                            all_options_last = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                            for i in range(1, 30):
                                all_options_text = driver.find_element(By.XPATH,"(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                                available_option.append(all_options_text)
                                if all_options_text == all_options_last:
                                    if 'Select option' in available_option:
                                        available_option.remove('Select option')
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                                    else:
                                        selected_option = random.choice(available_option)
                                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                        break
                        elif 'Father Name' in every_element_text:
                            every_element.click()
                            father_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'Father Name')]").text
                            father_name_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if father_name_check=="":
                                selected_name=action.send_keys(name)
                                selected_name.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",name)
                            else:
                                continue
                        elif 'Mother Name' in every_element_text:
                            every_element.click()
                            mother_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'Mother Name')]").text
                            mother_name_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if mother_name_check=="":
                                selected_name=action.send_keys(name)
                                selected_name.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",name)
                            else:
                                continue
                        elif ('Income' in every_element_text)or('Monthly Income' in every_element_text):
                            every_element.click()
                            income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if income_amt_check == "":
                                amount=random.randint(20000, 100000)
                                selected_amt = action.send_keys(int(amount))
                                selected_amt.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",amount)
                            else:
                                continue
                        elif ('Phone' in every_element_text) or ('Company Phone' in every_element_text):
                            every_element.click()
                            company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company')]").text
                            check_com_phone = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if check_com_phone == "":
                                selected_phone = action.send_keys(int(9667484050))
                                selected_phone.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","9667484050")
                            else:
                                continue
                        elif ('Loan Tenure' in every_element_text) or ('Tenure' in every_element_text):
                            every_element.click()
                            tenure_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                            tenure_text_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if tenure_text_check == "":
                                time.sleep(0.1)
                                time_selected=random.randint(6,64)
                                selected_tenure = action.send_keys(time_selected)
                                selected_tenure.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", time_selected)
                            else:
                                continue
                        elif ('Years Stayed' in every_element_text) or ('Years stayed' in every_element_text):
                            every_element.click()
                            stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                            stayed_text_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if stayed_text_check == "":
                                time.sleep(0.1)
                                time_selected=random.randint(6,64)
                                selected_stayed = action.send_keys(time_selected)
                                selected_stayed.perform()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", time_selected)
                            else:
                                continue
                        elif ('Pincode' in every_element_text) or ('Postal' in every_element_text)or('pincode' in every_element_text):
                            every_element.click()
                            pincode_check = driver.find_element(By.XPATH,
                                                                "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if pincode_check == "":
                                generated_pincode = random.randint(100000, 999990)
                                selected_pincode = action.send_keys(generated_pincode)
                                selected_pincode.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", generated_pincode)
                            else:
                                continue
                        elif ('city' in every_element_text) or ('City' in every_element_text):
                            every_element.click()
                            city_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                            if city_check == "":
                                city = "Delhi"
                                selected_city = action.send_keys(city)
                                selected_city.perform()
                                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,"->", city)
                            else:
                                continue
                        if every_element_text==last_element_text:
                            break
                    submit_button=driver.find_element(By.XPATH,"//button[@class='mt-4']")
                    submit_button.click()
                    time.sleep(4)
                    if (driver.find_element(By.XPATH,"//*[@class='loanStep__wrapper']/descendant::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')]")):
                        if 'Thank You' in driver.find_element(By.TAG_NAME,"html").text:
                            time.sleep(1)
                            screenshot = driver.find_element(By.XPATH, "//div[@class='jumbotron text-center']")
                            with py.hold('ctrl'):
                                py.press('+')
                                py.press('+')
                                py.press('+')
                                py.press('+')
                                py.press('+')
                            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                            time.sleep(0.2)
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
                            time.sleep(0.2)
                            screenshot.screenshot(driver.find_element(By.XPATH,"//span[contains(@style,'text-transform: capitalize')]").text+".png")
                            time.sleep(1)
                            break
                        else:
                            print("-" * 5, "Professional Details", "-" * 5)

                    restart = True

        time.sleep(2)
        driver.close()
except (NoSuchElementException,NoSuchWindowException)as e:
    print("Something unusual happened")
    print(e)