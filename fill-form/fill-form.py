from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time
import pyautogui as py


# available_option=[]
driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
time.sleep(0.5)
driver.get("https://qa.referloan.in/")
form_name=py.prompt("Enter name of form")
form_name=form_name.replace('yes',"".join('')).replace('hdfc',"".join('')).replace('icici',"".join('')).replace('au',"".join('')).replace('sbi',"".join(''))
# print(form_name)
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
form_name=form_name.title()
choosen_form_name=driver.find_element(By.XPATH,"//a[@tabindex='-1' and contains(text(),'"+form_name+"')]")
found_url=choosen_form_name.get_attribute('href')
print("First URL found:","\n",found_url.replace("?utm_source=direct_visitors&utm_medium=self&utm_campaign=&utm_id=",''))
time.sleep(1)
driver.get(found_url)
time.sleep(1.5)
driver.execute_script("window.scrollBy(0,300)","")
full_name=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='full_name']")
action.move_to_element(full_name).perform()
full_name.click()
action.send_keys("Test name").perform()
phone_number=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input' and @name='phone_no']")
action.move_to_element(phone_number).perform()
# driver.execute_script("window.scrollBy(0,70)", "")
phone_number.click()
action.send_keys("9667484050").perform()
# driver.execute_script("window.scrollBy(0,70)","")
otp_box=driver.find_element(By.XPATH,"//input[@id='otpCheckbox']")
action.move_to_element(otp_box).perform()
otp_box.click()
generate_otp=driver.find_element(By.XPATH,"//button[@class='mt-4']")
action.move_to_element(generate_otp).perform()
generate_otp.click()
time.sleep(0.8)
user_otp=py.prompt("Found OTP Page, Please enter the OTP to continue")
otp_field=driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiInput-input']")
otp_field.click()
time.sleep(0.5)
action.send_keys(user_otp).perform()
time.sleep(0.5)
verify_otp=driver.find_element(By.XPATH,"//button[@class='mt-4']").click()
time.sleep(2)
last_element_text=driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[last()]").text
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(0.8)
driver.execute_script("window.scrollBy(0,220)","")
for inputs in range(1,25):
    available_option = []
    every_element = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs))
    every_element_text = driver.find_element(By.XPATH, "(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
    # print(every_element_text,'DEBUG------>')
    # print(every_element_text,'DEBUG')
    # while every_element_text!=last_element_text
    # if every_element_text==last_element_text:
    #     print("completed-------")
    #     # every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
    #     break
    # while True:
    time.sleep(1)
    # if every_element_text!=last_element_text:
    every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
    # print(every_element_text,'DEBUG')
    if 'Title' in every_element_text:
        every_element.click()
        time.sleep(0.5)
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
            selected_name=action.send_keys("Test Name")
            selected_name.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Test Name")
        else:
            continue

    elif 'First Name' in every_element_text:
        every_element.click()
        first_name_text=driver.find_element(By.XPATH,"//*[contains(text(),'First Name')]").text
        first_name_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
        if first_name_check=="":
            selected_name=action.send_keys("Test")
            selected_name.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Test")
        else:
            continue

    elif ('Last Name' in every_element_text)or('Middle Name' in every_element_text):
        every_element.click()
        last_name_text=driver.find_element(By.XPATH,"//label[contains(text(), 'Last') or contains(text(), 'Middle') and contains(@class,'MuiFormLabel-root')]").text
        last_name_check = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
        if last_name_check=="":
            selected_name=action.send_keys("Name")
            selected_name.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","Name")
        else:
            continue

    elif ('Phone' in every_element_text) or ('Mobile' in every_element_text):
        every_element.click()
        phone_number_text=driver.find_element(By.XPATH,"//*[contains(text(), 'Phone') or contains(text(), 'Mobile') and contains(@class,'MuiFormLabel-root')]").text
        check_phone=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
        if check_phone=="":
            selected_number=action.send_keys("9667484050")
            selected_number.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","9667484050")
        else:
            continue

    elif ('Email' in every_element_text)or('Email Address' in every_element_text):
        every_element.click()
        email_text=driver.find_element(By.XPATH,"//*[contains(text(),'Email')]").text
        check_email = driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
        # print(check_email,'EMAIL DEBUG')
        if check_email=="":
            selected_email=action.send_keys("qa@gmail.com")
            selected_email.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->","qa@gmail.com")
        else:
            continue

    elif 'Gender' in every_element_text:
        every_element.click()
        time.sleep(0.5)
        # all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
        # all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
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
        # loan_amt_text=driver.find_element(By.XPATH,"//*[contains(text(),'Loan Amount') and contains(@class,'MuiFormLabel-root')] ").text
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
        dob_check=driver.find_element(By.XPATH,"//*[contains(@class,'MuiInputBase-input') and @value='']").text
        if pincode_check=="":
            generated_pincode=random.randint(100000,999990)
            selected_pincode=action.send_keys(generated_pincode)
            selected_pincode.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",generated_pincode)
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
            selected_city=action.send_keys(pan_number)
            selected_city.perform()
            print(driver.find_element(By.XPATH, "(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text, "->",pan_number)
        else:
            continue

    elif 'Marital' in every_element_text:
        every_element.click()
        time.sleep(0.5)
        # all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
        # all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
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

    elif 'Residence Type' in every_element_text:
        every_element.click()
        time.sleep(0.5)
        # all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
        # all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
        all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
        for i in range(1,5):
            all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
            available_option.append(all_options_text)
            if all_options_text==all_options_last:
                available_option.remove('Select option')
                selected_option=random.choice(available_option)
                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='"+selected_option+"']").click()
                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text,"->",selected_option)
                break
            else:
                continue

    elif 'Qualification' in every_element_text:
        every_element.click()
        time.sleep(0.5)
        # all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
        # all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
        all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
        for i in range(1,8):
            all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
            available_option.append(all_options_text)
            if all_options_text==all_options_last:
                available_option.remove('Select option')
                selected_option=random.choice(available_option)
                print(selected_option,'-1-2-3-4-')
                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='"+selected_option+"']").click()
                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text,"->",selected_option)
                break
            else:
                continue

    elif 'Occupation' in every_element_text:
        every_element.click()
        time.sleep(0.5)
        # all_options=driver.find_element(By.XPATH,"//li[contains(@class,'MuiButtonBase-root')]")
        # all_options_text = driver.find_element(By.XPATH, "//li[contains(@class,'MuiButtonBase-root')]").text
        all_options_last = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[last()]").text
        for i in range(1,8):
            all_options_text = driver.find_element(By.XPATH, "(//li[contains(@class,'MuiButtonBase-root')])[%d]"%(i)).text
            available_option.append(all_options_text)
            available_option.remove('Select option')
            if all_options_text==all_options_last:
                selected_option=random.choice(available_option)
                driver.find_element(By.XPATH,"//*[contains(@class,'MuiButtonBase-root')]/em[text()='"+selected_option+"']").click()
                print(driver.find_element(By.XPATH,"(//label[contains(@class,'MuiFormLabel-root')])[%d]"%(inputs)).text,"->",selected_option)
                break
            else:
                continue

    if every_element_text==last_element_text:
        break


# //*[contains(text(),'Pincode') and contains(@class,'MuiFormLabel-root')]


time.sleep(2)
driver.close()


'''
TO-DO-ISSUES
-------
1. Different names, classes and attibutes everywhere
'''

'''
IDEA for the blunder:
    if every_element_text==last_element_text:
        print("completed-------")
        # every_element_text = driver.find_element(By.XPATH,"(//*[contains(@class,'MuiFormControl-root')])[%d]" % (inputs)).text
        # break
    # elif every_element_text!=last_element_text:
    ----Remove this---- LINE-69 
    
LOGIC--:
if every-element = last element then do the work and break the loop 
while true:
    fill the data
    and if every-element=last element:
        break
this will execute the script untill break is not hit

if last-element is reached, it will will the data and check the condition, and will break the while true loop

standard chartered bank personal loan


add this dob
final=str(random.randint(1,12))+str(random.randint(1,31))+str(random.randint(1960,2022))
if len(final)<=7:
    final='0'+final
    if len(final)==7:
        final=final[:2]+'0'+final[2:]
print(final)
'''