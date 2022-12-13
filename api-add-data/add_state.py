import pyautogui as pt
import time

# state_name=['Arunachal Pradesh','Jharkhand','Karnataka','Kerala','Madya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Assam','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttaranchal','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Chandigarh','Bihar','Dadar and Nagar Haveli','Daman and Diu','Delhi','Lakshadeep','Pondicherry','Telangana','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir']
# state_code=['AR','JH','KA','KL','MP','MH','MN','ML','MZ','NL','OR','AS','PB','RJ','SK','TN','TR','UL','UP','WB','AN','CH','BR','DN','DD','DL','LD','PY','TG','CG','GA','GJ','HR','HP','JK']
profession_name=['Sales & Marketing','Finance & Accounting','Operations','Software & IT','Factory Worker','Teacher','Doctor/Nurse/Caregiver/Physio','Core Engineering (Chemical, Civil, Mechanical, Pharma etc.)','BPO/Back Office Executive','Field Executive (Banks, BFSI etc.)','Housekeeping/Facility Management','Electrician/Plumber/Carpenter/Mechanic','Delivery-Boy/Driver','Security Guard','Beautician/Salon Worker','Retail Shop Owner/Business Owner','Others']
profession_code=['28','29','30','31','17','26','32','24','3','8','9','7','33','1','18','12','21']
time.sleep(4)
for i in range(0,len(profession_code)):
    pt.typewrite(profession_name[i])
    pt.press("tab")
    pt.typewrite(profession_code[i])
    pt.press("tab")