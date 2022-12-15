from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import NameGenerator
import PanGenerator
import time
import pyautogui as py


name=NameGenerator.generator()
list_name=name.split()
pan_card=PanGenerator.generator(name)
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
driver.get("https://qa.referloan.in/")
time.sleep(3)
all_element_last=driver.find_element(By.XPATH,"(//a[@tabindex='-1'])[last()]")

# test=py.prompt("test")
while True:
    form_name = py.prompt("Enter name of form | Press Cancel to quit")
    if form_name==None:
        print("Script cancelled")
        time.sleep(1)
        driver.quit()
        exit (1)

    print("Choosen name = ",form_name)
    form_name=form_name.lower()

    with py.hold('ctrl'):
        py.press('-')
        py.press('-')
        py.press('-')
        py.press('-')
        py.press('-')
    for loop in range(1,500):
        all_element=driver.find_element(By.XPATH,"(//a[@tabindex='-1'])[%d]"%(loop))
        all_element_last_text=all_element_last.get_attribute('innerHTML').lower()
        all_element_url=all_element.get_attribute('href')
        # all_element_url=all_element_url.replace("?utm_source=direct_visitors&utm_medium=self&utm_campaign=&utm_id=", '')
        all_element_name=all_element.get_attribute('innerHTML').lower()
        form_name_url=form_name.replace(" ","-")
        if (form_name in all_element_name)or(form_name_url in all_element_url):
            print("First URL found:", "\n", all_element_url)
            driver.get(all_element_url)
            if all_element_last_text==all_element_name:
                break
    print("First URL found:","\n",all_element_url)
    time.sleep(1.5)
    scroll_form = driver.find_element(By.XPATH, "(//*[@id='apply-banner'])[1]")
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(0.2)
    driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
    full_name=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
    action.move_to_element(full_name).perform()
    full_name.click()
    action.send_keys("name").perform()
    phone_number=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
    action.move_to_element(phone_number).perform()
    phone_number.click()
    action.send_keys(int(9667484050)).perform()
    otp_box=driver.find_element(By.XPATH,"//input[@id='otpCheckbox']")
    action.move_to_element(otp_box).perform()
    otp_box.click()
    submit_button=driver.find_element(By.XPATH,"//button[@class='mt-4']")
    # action.move_to_element(submit_button).perform()
    # submit_button.click()
    time.sleep(0.8)
    user_otp=py.prompt("Found OTP Page, Please enter the OTP to continue")
    if user_otp==None:
        print("Can't fill otp, Quitting")
        time.sleep(1)
        driver.quit()
        exit(1)
    otp_field=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input']")
    otp_field.click()
    time.sleep(0.5)
    action.send_keys(user_otp).perform()
    time.sleep(0.5)
    verify_otp=driver.find_element(By.XPATH,"//button[@class='mt-4']").click()
    time.sleep(0.8)
    last_element_text=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(0.2)
    driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
    restart=True
    try:
        while restart:
            restart=False
            for inputs in range(1, 25):
                available_option = []
                every_element = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs))
                every_element_text = driver.find_element(By.XPATH,
                                                         "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
                time.sleep(0.3)
                last_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[last()]").text
                if 'Title' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]")
                    all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 13):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        selected_option = random.choice(available_option)
                        if all_options_text == all_options_last:
                            driver.find_element(By.XPATH,
                                                "//*[contains(@class,'MuiButtonBase-root') and @data-value='" + selected_option + "']").click()
                            print(driver.find_element(By.XPATH,
                                                      "//label[contains(@class,'MuiFormLabel-root')][%d]" % (inputs)).text,
                                  "->", selected_option)
                            break
                elif 'Full Name' in every_element_text:
                    every_element.click()
                    full_name_text = driver.find_element(By.XPATH, "//input[@id='full_name' or @id='name']").text
                    if full_name_text == "":
                        selected_name = action.send_keys(name)
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              name)
                    else:
                        continue
                elif 'First Name' in every_element_text:
                    every_element.click()
                    # first_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'First Name')]").text
                    first_name_check = driver.find_element(By.XPATH,
                                                           "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if first_name_check == "":
                        selected_name = action.send_keys(str(list_name[0]))
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              str(list_name[0]))
                    else:
                        continue
                elif ('Last Name' in every_element_text) or ('Middle Name' in every_element_text):
                    every_element.click()
                    # last_name_text=driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                    last_name_check = driver.find_element(By.XPATH,
                                                          "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if last_name_check == "":

                        time.sleep(0.1)
                        selected_name = action.send_keys(str(list_name[1]))
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              str(list_name[1]))
                    else:
                        continue
                elif ('Phone' in every_element_text) or ('Mobile' in every_element_text) or ('phone' in every_element_text):
                    every_element.click()
                    # phone_number_text=driver.find_element(By.XPATH,"//*[contains(text(), 'Phone') or contains(text(), 'Mobile') and contains(@class,'MuiFormLabel-root')]").text
                    check_phone = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_phone == "":

                        time.sleep(0.1)
                        selected_number = action.send_keys(int(9667484050))
                        selected_number.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              "9667484050")
                    else:
                        continue
                elif ('Email' in every_element_text) or ('Email Address' in every_element_text):
                    every_element.click()
                    # email_text=driver.find_element(By.XPATH,"//*[contains(text(),'Email')]").text
                    check_email = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_email == "":

                        time.sleep(0.1)
                        selected_email = action.send_keys("qa@gmail.com")
                        selected_email.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              "qa@gmail.com")
                    else:
                        continue
                elif 'Gender' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 5):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            selected_option = random.choice(available_option)
                            driver.find_element(By.XPATH,
                                                "//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                            print(driver.find_element(By.XPATH,
                                                      "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text,
                                  "->", selected_option)
                            break
                        else:
                            continue
                elif ('Loan Amount' in every_element_text) or ('loanAmount' in every_element_text):
                    every_element.click()
                    loan_amt_check = driver.find_element(By.XPATH,
                                                         "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if loan_amt_check == "":
                        amount = random.randint(20000, 100000)
                        selected_amt = action.send_keys(amount)
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              amount)
                    else:
                        continue
                elif ('Pincode' in every_element_text) or('Pin code' in every_element_text)or('Pin Code' in every_element_text)or ('Postal' in every_element_text) or ('PinCode' in every_element_text)or ('Pin-Code' in every_element_text)or ('Pin-code' in every_element_text):
                    every_element.click()
                    pincode_check = driver.find_element(By.XPATH,
                                                        "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if pincode_check == "":
                        generated_pincode = random.randint(100000, 999990)
                        selected_pincode = action.send_keys(generated_pincode)
                        selected_pincode.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              generated_pincode)
                    else:
                        continue
                elif ('Date' in every_element_text) or ('Birth' in every_element_text) or ('DOB' in every_element_text) or (
                        'dob' in every_element_text):
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
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              final_dob)
                    else:
                        continue
                elif ('First name As Per Pancard' in every_element_text) or ('First Name As Per Pancard' in every_element_text):
                    every_element.click()
                    name_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if name_check == "":
                        selected_name = action.send_keys(list_name[0])
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              list_name[0])
                    else:
                        continue
                elif ('Last Name As Per Pancard' in every_element_text) or ('Last name As Per Pancard' in every_element_text):
                    every_element.click()
                    name_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if name_check == "":
                        selected_name = action.send_keys(list_name[1])
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              list_name[1])
                    else:
                        continue
                elif ('city' in every_element_text) or ('City' in every_element_text):
                    every_element.click()
                    city_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if city_check == "":
                        city = "Delhi"
                        selected_city = action.send_keys(city)
                        selected_city.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              city)
                    else:
                        continue
                elif ('Pan' in every_element_text) or ('PAN' in every_element_text):
                    every_element.click()
                    city_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if city_check == "":
                        selected_city = action.send_keys(pan_card)
                        selected_city.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              pan_card)
                    else:
                        continue
                elif 'Marital' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 5):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            if 'Select option' in available_option:
                                available_option.remove('Select option')
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                        else:
                            continue
                elif 'Residence Type' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 10):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            if 'Select option' in available_option:
                                available_option.remove('Select option')
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                        else:
                            continue
                elif 'Qualification' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 10):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            if 'Select option' in available_option:
                                available_option.remove('Select option')
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                        else:
                            continue
                elif 'Occupation' in every_element_text:
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 10):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            if 'Select option' in available_option:
                                available_option.remove('Select option')
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                        else:
                            continue
                elif ('Dependents' in every_element_text) or ('Number Of Dependents' in every_element_text):
                    every_element.click()
                    time.sleep(0.3)
                    all_options_last = driver.find_element(By.XPATH,
                                                           "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                    for i in range(1, 10):
                        all_options_text = driver.find_element(By.XPATH,
                                                               "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                        available_option.append(all_options_text)
                        if all_options_text == all_options_last:
                            if 'Select option' in available_option:
                                available_option.remove('Select option')
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,
                                                    "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                        else:
                            continue

                elif ('Type' in every_element_text) or ('type' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif ('Income' in every_element_text) or ('Monthly Income' in every_element_text):
                    every_element.click()
                    income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if income_amt_check == "":
                        selected_amt = action.send_keys(random.randint(20000, 100000))
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              selected_amt)
                    else:
                        continue
                elif 'Credit Score' in every_element_text:
                    every_element.click()
                    income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if income_amt_check == "":
                        amount = random.randint(700, 850)
                        selected_amt = action.send_keys(amount)
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              amount)
                    else:
                        continue
                elif ('Rent' in every_element_text) or ('rent' in every_element_text):
                    every_element.click()
                    income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if income_amt_check == "":
                        amount = random.randint(10000, 100000)
                        selected_amt = action.send_keys(amount)
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              amount)
                    else:
                        continue
                elif ('Credit Bureau' in every_element_text) or ('credit bureau' in every_element_text) or (
                        'Credit bureau' in every_element_text):
                    every_element.click()
                    income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if income_amt_check == "":
                        amount = "Equifax"
                        selected_amt = action.send_keys(amount)
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              amount)
                    else:
                        continue
                elif ('Reason' in every_element_text) or ('Reason of Loan' in every_element_text) or (
                        'Reason of Loan Apply' in every_element_text) or ('reason' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                # elif ('Profession Type' in every_element_text) or ('Professional Type' in every_element_text) or (
                #         'Profession' in every_element_text):
                #     every_element.click()
                #     time.sleep(0.3)
                #     all_options_last = driver.find_element(By.XPATH,
                #                                            "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
                #     for i in range(1, 30):
                #         all_options_text = driver.find_element(By.XPATH,
                #                                                "(//li[contains(@class,'MuiButtonBase-root')])[%d]" % (i)).text
                #         available_option.append(all_options_text)
                #         if all_options_text == all_options_last:
                #             if 'Select option' in available_option:
                #                 available_option.remove('Select option')
                #                 selected_option = random.choice(available_option)
                #                 driver.find_element(By.XPATH,
                #                                     "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                #                 print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                #                     inputs)).text, "->", selected_option)
                #                 break
                #             else:
                #                 selected_option = random.choice(available_option)
                #                 driver.find_element(By.XPATH,
                #                                     "//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                #                 print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                #                     inputs)).text, "->", selected_option)
                #                 break
                elif ('Company name' in every_element_text) or ('Company Name' in every_element_text) or (
                        'Company' in every_element_text):
                    every_element.click()
                    # company_name_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company name')or contains(text(),'Company Name')]").text
                    check_com_name = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_com_name == "":

                        time.sleep(0.1)
                        selected_name = action.send_keys(NameGenerator.generator())
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              NameGenerator.generator())
                    else:
                        continue
                elif ('Company Address' in every_element_text):
                    every_element.click()
                    # company_addr_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company Address')or contains(text(),'Company address')]").text
                    check_add = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_add == "":
                        selected_name = action.send_keys("Dummy Address 123")
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Dummy Address 123")
                    else:
                        continue
                elif ('Address Proof' in every_element_text) or ('Proof Number' in every_element_text):
                    every_element.click()
                    # company_addr_text = driver.find_element(By.XPATH, "//*[contains(text(),'Address')or contains(text(),'address')]").text
                    check_add = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_add == "":
                        selected_name = action.send_keys("9876543210")
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","9876543210")
                    else:
                        continue
                # elif ('Years Stayed' in every_element_text) or ('Years stayed' in every_element_text):
                #     every_element.click()
                #     stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
                #     stayed_text_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                #     if stayed_text_check == "":
                #         time.sleep(0.1)
                #         time_selected=random.randint(0,50)
                #         selected_stayed = action.send_keys(time_selected)
                #         selected_stayed.perform()
                #         print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", time_selected)
                #     else:
                #         continue
                elif ('Address' in every_element_text):
                    every_element.click()
                    # company_addr_text = driver.find_element(By.XPATH, "//*[contains(text(),'Address')or contains(text(),'address')]").text
                    check_add = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_add == "":
                        selected_name = action.send_keys("Dummy Address 123")
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Dummy Address 123")
                    else:
                        continue
                elif ('working Years' in every_element_text) or ('Current Company Working Years' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif ('Document Type' in every_element_text) or ('Document type' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif ('Salary Mode' in every_element_text) or ('Salary mode' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif ('Document number' in every_element_text) or ('Document Number' in every_element_text) or (
                        'Document No' in every_element_text) or ('Document no' in every_element_text):
                    every_element.click()
                    # company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Document')]").text
                    check_com_phone = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_com_phone == "":
                        selected_phone = action.send_keys("9876543210")
                        selected_phone.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","9876543210")
                    else:
                        continue
                elif ('state' in every_element_text) or ('State' in every_element_text) or (
                        'Company State' in every_element_text):
                    every_element.click()
                    state_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if state_check == "":
                        state = "Delhi"
                        selected_state = action.send_keys(state)
                        selected_state.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              state)
                    else:
                        continue
                elif ('Current Total Emi Paid Per Month' in every_element_text) or ('Paid Per Month' in every_element_text) or (
                        'Total Emi' in every_element_text) or ('Emi Paid' in every_element_text) or (
                        'emi' in every_element_text):
                    every_element.click()
                    # emi_text = driver.find_element(By.XPATH, "(//*[contains(text(),'Emi') or contains(text(),'emi')])[1]").text
                    check_emi = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_emi == "":
                        emi = random.randint(20000, 100000)
                        selected_emi = action.send_keys(emi)
                        selected_emi.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              emi)
                    else:
                        continue
                elif ('Bank Name' in every_element_text) or ('Name Of Bank' in every_element_text):
                    every_element.click()
                    # bank_name_text = driver.find_element(By.XPATH, "//*[contains(text(),'Bank name')or contains(text(),'Bank Name')]").text
                    check_bank = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_bank == "":
                        selected_bank = action.send_keys("Test Bank")
                        selected_bank.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","Test Bank")
                    else:
                        continue
                elif ('Email' in every_element_text) or ('Email Address' in every_element_text) or (
                        'Email ID' in every_element_text) or ('Email Id' in every_element_text):
                    every_element.click()
                    # email_text = driver.find_element(By.XPATH, "//*[contains(text(),'Email')]").text
                    check_email = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_email == "":
                        selected_email = action.send_keys("qa@gmail.com")
                        selected_email.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","qa@gmail.com")
                    else:
                        continue
                elif ('Designation' in every_element_text) or ('Position' in every_element_text) or (
                        'Current Designation' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif ('Education' in every_element_text) or ('Qualification' in every_element_text) or (
                        'qualification' in every_element_text):
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
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                            else:
                                selected_option = random.choice(available_option)
                                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[contains(text(),'" + selected_option + "')]").click()
                                print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                                    inputs)).text, "->", selected_option)
                                break
                elif 'Father Name' in every_element_text:
                    every_element.click()
                    # father_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'Father Name')]").text
                    father_name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if father_name_check == "":
                        selected_name = action.send_keys(name)
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              name)
                    else:
                        continue
                elif 'Mother Name' in every_element_text:
                    every_element.click()
                    # mother_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'Mother Name')]").text
                    mother_name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if mother_name_check == "":
                        selected_name = action.send_keys(name)
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              name)
                    else:
                        continue
                elif ('Income' in every_element_text) or ('Monthly Income' in every_element_text):
                    every_element.click()
                    income_amt_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if income_amt_check == "":
                        amount = random.randint(20000, 100000)
                        selected_amt = action.send_keys(int(amount))
                        selected_amt.perform()
                        print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              amount)
                    else:
                        continue
                elif ('Phone' in every_element_text) or ('Company Phone' in every_element_text):
                    every_element.click()
                    # company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company')]").text
                    check_com_phone = driver.find_element(By.XPATH,
                                                          "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if check_com_phone == "":
                        selected_phone = action.send_keys(int(9667484050))
                        selected_phone.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              "9667484050")
                    else:
                        continue
                elif ('Loan Tenure' in every_element_text) or ('Tenure' in every_element_text) or (
                        'tenure' in every_element_text):
                    every_element.click()
                    # tenure_text = driver.find_element(By.XPATH,"//label[contains(text(), 'tenure') or contains(text(), 'Tenure') and contains(@class,'MuiFormLabel-root')]").text
                    tenure_text_check = driver.find_element(By.XPATH,
                                                            "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if tenure_text_check == "":
                        time.sleep(0.1)
                        time_selected = random.randint(6, 64)
                        selected_tenure = action.send_keys(time_selected)
                        selected_tenure.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              time_selected)
                    else:
                        continue
                elif ('Total Experience Months' in every_element_text) or ('Experience Months' in every_element_text) or (
                        'Experience' in every_element_text):
                    every_element.click()
                    # exp_text = driver.find_element(By.XPATH,"//label[contains(text(), 'tenure') or contains(text(), 'Tenure') and contains(@class,'MuiFormLabel-root')]").text
                    exp_text_check = driver.find_element(By.XPATH,
                                                         "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if exp_text_check == "":
                        time.sleep(0.1)
                        time_selected = random.randint(0, 200)
                        selected_exp = action.send_keys(time_selected)
                        selected_exp.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              time_selected)
                    else:
                        continue
                elif ('Years Stayed' in every_element_text) or ('Years stayed' in every_element_text):
                    every_element.click()
                    # stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Year') or contains(text(), 'Stay') and contains(@class,'MuiFormLabel-root')]").text
                    stayed_text_check = driver.find_element(By.XPATH,
                                                            "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if stayed_text_check == "":
                        time.sleep(0.1)
                        time_selected = random.randint(6, 64)
                        selected_stayed = action.send_keys(time_selected)
                        selected_stayed.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              time_selected)
                    else:
                        continue
                elif ('IFSC' in every_element_text) or ('ifsc' in every_element_text):
                    every_element.click()
                    # stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Year') or contains(text(), 'Stay') and contains(@class,'MuiFormLabel-root')]").text
                    stayed_text_check = driver.find_element(By.XPATH,
                                                            "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if stayed_text_check == "":
                        time.sleep(0.1)
                        ifsc = "SBIN0011513"
                        selected_stayed = action.send_keys(ifsc)
                        selected_stayed.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              ifsc)
                    else:
                        continue
                elif 'Account Number' in every_element_text:
                    every_element.click()
                    # stayed_text = driver.find_element(By.XPATH,"//label[contains(text(), 'Year') or contains(text(), 'Stay') and contains(@class,'MuiFormLabel-root')]").text
                    stayed_text_check = driver.find_element(By.XPATH,
                                                            "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if stayed_text_check == "":
                        time.sleep(0.1)
                        ac_no = "39238765008"
                        selected_stayed = action.send_keys(ac_no)
                        selected_stayed.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              ac_no)
                    else:
                        continue
                elif ('Account Holder Name' in every_element_text) or ('Holder Name' in every_element_text):
                    every_element.click()
                    full_name_text = driver.find_element(By.XPATH,
                                                         "//input[@id='full_name' or @id='name' or @id='accountHolderName']").text
                    if full_name_text == "":
                        selected_name = action.send_keys(name)
                        selected_name.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              name)
                    else:
                        continue
                elif ('city' in every_element_text) or ('City' in every_element_text):
                    every_element.click()
                    city_check = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
                    if city_check == "":
                        city = "Delhi"
                        selected_city = action.send_keys(city)
                        selected_city.perform()
                        print(driver.find_element(By.XPATH,
                                                  "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",
                              city)
                    else:
                        continue
                if every_element_text == last_element_text:
                    break
            submit_button = driver.find_element(By.XPATH, "//button[@class='mt-4']")
            submit_button.click()
            time.sleep(4)
            if (driver.find_element(By.XPATH,
                                    "//*[@class='loanStep__wrapper']/descendant-or-self::*[contains(text(),'Details') or contains(text(),'Thank') or contains(text(),'detail')or contains(text(),'Other')or contains(text(),'other')]")):
                if 'Thank You' in driver.find_element(By.TAG_NAME, "html").text:
                    time.sleep(1)
                    screenshot = driver.find_element(By.XPATH, "//div[@class='jumbotron text-center']")
                    with py.hold('ctrl'):
                        py.press('+')
                        py.press('+')
                        py.press('+')
                        py.press('+')
                    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                    time.sleep(0.2)
                    driver.execute_script("arguments[0].scrollIntoView();", scroll_form)
                    time.sleep(0.2)
                    screenshot.screenshot(
                        driver.find_element(By.XPATH, "//span[contains(@style,'text-transform: capitalize')]").text + ".png")
                    time.sleep(1)
                    break
                else:
                    print("-" * 5, "Professional Details", "-" * 5)

            restart = True


    except NoSuchElementException as e:
        print("Something unusual happened")
        print(e)
    except:
        print("Something unusual happened")
time.sleep(2)
driver.close()