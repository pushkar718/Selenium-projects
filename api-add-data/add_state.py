import pyautogui as pt
import time

state_name=['Arunachal Pradesh','Jharkhand','Karnataka','Kerala','Madya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Assam','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttaranchal','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Chandigarh','Bihar','Dadar and Nagar Haveli','Daman and Diu','Delhi','Lakshadeep','Pondicherry','Telangana','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir']
state_code=['AR','JH','KA','KL','MP','MH','MN','ML','MZ','NL','OR','AS','PB','RJ','SK','TN','TR','UL','UP','WB','AN','CH','BR','DN','DD','DL','LD','PY','TG','CG','GA','GJ','HR','HP','JK']
i=0
time.sleep(4)
for i in range(0,35):
    pt.typewrite(state_name[i])
    pt.press("tab")
    pt.typewrite(state_code[i])
    pt.press("tab")