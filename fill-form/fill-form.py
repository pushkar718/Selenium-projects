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


name=NameGenerator.generator()
list_name=name.split()
pan_card=PanGenerator.generator(name)
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
driver.get("https://qa.referloan.in/")
form_name=py.prompt("Enter name of form")
# form_name=form_name.replace('yes',"".join('')).replace('hdfc',"".join('')).replace('icici',"".join('')).replace('au',"".join('')).replace('sbi',"".join(''))
if (form_name=='') or (form_name==None):
    print("Nothing in prompt.\n----Trying URL----")
    form_url=py.prompt("Enter URL of the page")
    if form_url=='' or form_url==None:
        print("Nothing entered in URL.\n----Quiting script----")
        py.alert("Quitting script")
        time.sleep(1)
        driver.quit()
else:
    print("Choosen name = ",form_name)
form_name=form_name.lower()
for loop in range(1,500):
    all_element=driver.find_element(By.XPATH,"(//a[@tabindex='-1'])[%d]"%(loop))
    all_element_url=all_element.get_attribute('href')
    all_element_name=all_element.get_attribute('innerHTML').lower()
    form_name_url=form_name.replace(" ","-")
    if (form_name in all_element_name)or(form_name_url in all_element_url):
        driver.get(all_element_url)
        break
print("First URL found:","\n",all_element_url.replace("?utm_source=direct_visitors&utm_medium=self&utm_campaign=&utm_id=",''))
time.sleep(1.5)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(0.2)
driver.execute_script("window.scrollBy(0,200)","")
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
last_element_text=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(0.2)
driver.execute_script("window.scrollBy(0,350)","")
for inputs in range(1,25):
    available_option = []
    every_element = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs))
    every_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
    time.sleep(0.3)
    every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
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
            pan_number="ASDFN1789R"
            selected_city=action.send_keys(pan_card)
            selected_city.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",pan_number)
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

    if every_element_text==last_element_text:
        break

time.sleep(1)
submit_button=driver.find_element(By.XPATH,"//button[@class='mt-4']")
submit_button.click()
time.sleep(1.2)
if (driver.find_element(By.XPATH,"//h3[contains(text(),'Professional')] or contains(text(),'Other') or contains(text(),'Details')").is_displayed()==True):
    print("-"*5,"Professional Details","-"*5)
    for inputs in range(1, 25):
        time.sleep(0.8)
        available_option = []
        every_element = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs))
        every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
        time.sleep(0.3)
        every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
        every_element_last=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text

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
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                        break
                    else:
                        selected_option = random.choice(available_option)
                        driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                        break
        elif ('Type of company' in every_element_text)or('Type Of company' in every_element_text)or('Type Of Company' in every_element_text):
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
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->", selected_option)
                        break
                    else:
                        selected_option = random.choice(available_option)
                        driver.find_element(By.XPATH,
                                            "//*[contains(@class,'MuiButtonBase-root')]/em[text()='" + selected_option + "']").click()
                        print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (
                            inputs)).text, "->", selected_option)
                        break
        elif ('Company name' in every_element_text) or ('Company Name' in every_element_text):
            every_element.click()
            company_name_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company name')]").text
            check_com_name = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
            if check_com_name == "":
                selected_name = action.send_keys(NameGenerator.generator())
                selected_email.perform()
                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->",NameGenerator.generator())
            else:
                continue
        elif ('Company Phone No' in every_element_text) or ('Company Phone Number' in every_element_text):
            every_element.click()
            company_phone_text = driver.find_element(By.XPATH, "//*[contains(text(),'Company name')]").text
            check_com_phone = driver.find_element(By.XPATH, "//*[contains(@class,'MuiInputBase-input') and @value='']").text
            if check_com_phone == "":
                selected_phone = action.send_keys(int(9667484050))
                selected_phone.perform()
                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]" % (inputs)).text, "->","9667484050")
            else:
                continue
        elif ('Designation' in every_element_text)or('Position' in every_element_text):
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

        elif ('Document Type' in every_element_text)or('Document type' in every_element_text):
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


        if every_element_text==every_element_last:
            submit_button = driver.find_element(By.XPATH, "//button[@class='mt-4']")
            submit_button.click()
            time.sleep(1)
            break

if driver.find_element(By.XPATH,"//p[@class='form-error']").text=="Something went wrong!":
    print("Check referloan-error channel")
    screenshot = driver.find_element(By.XPATH, "//div[@class='loanStep__wrapper']")
    screenshot.screenshot(all_element_name+".png")
    exit(1)
    driver.close()
else:
    print("Data submitted successfully")

if driver.find_element(By.XPATH,"//*[@class='display-3']").text=="Thank You!":
    screenshot=driver.find_element(By.XPATH,"//div[@class='jumbotron text-center']")
    screenshot.screenshot(driver.find_element(By.XPATH,"//span[contains(@style,'text-transform: capitalize')]").text+".png")
time.sleep(2)
driver.close()
