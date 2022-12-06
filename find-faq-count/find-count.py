import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()
action=ActionChains(driver)
driver.get("https://qa.referloan.in")
time.sleep(1.8)
check_last = driver.find_element(By.XPATH, "(//ul/li/a[@tabindex='-1'])[last()]")
check_last_url=check_last.get_attribute('href')
f = open("less_than_5_faq.txt", "w")
w = open("more_than_5_faq.txt", "w")
page_count=0
for b in range(1, 500):
    try:
        count = 0
        check = driver.find_element(By.XPATH, "(//ul/li/a[@tabindex='-1'])[%d]" % (b))
        page_count+=1
        check_url = check.get_attribute('href')
        driver.get(check_url)
        time.sleep(2)
        page_name = driver.find_element(By.XPATH, "//span[contains(@style,'text-transform')]").text
        time.sleep(0.2)
        faq=driver.find_element(By.XPATH,"//section/div[@class='faqSetion']")
        driver.execute_script("arguments[0].scrollIntoView();", faq)
        time.sleep(1)
        check_faq_count_last = driver.find_element(By.XPATH, "(//button[@class='accordion-button collapsed'])[last()]").text
        for i in range(1,20):
            check_faq_count=driver.find_element(By.XPATH,"(//button[@class='accordion-button collapsed'])[%d]"%(i)).text
            count=count+1
            if check_faq_count==check_faq_count_last:
                if int(count)<5:
                    write=str(page_name)+" Has-> "+str(count)+"FAQs\n"
                    f.write(write)
                    print(page_name, "Has ->", count, "FAQs")
                else:
                    print(page_name, "Has ->", count, "FAQs")
                    w.write("%s Has-> %s FAQs\n"%(page_name,count))
                break

        if check_url==check_last_url:
            break
    except NoSuchElementException:
        print(page_name, "Has ->", count, "FAQs")
    except KeyboardInterrupt:
        print("Stopped by user")
    except:
        print("Other Errors")
time.sleep(1)
f.close()
w.close()
print("\n\nChecked",page_count,"Pages..!")
driver.close()