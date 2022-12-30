import pyautogui as pt
import time
#
state_name=['Architect(B.Arch)','CA','Consultant','Doctor','Employee(Central/State Govt.)','Engineer(B.Tech/B.E)','Lawyer','Others']
state_code=['3','4','5','6','7','8','9','10']
time.sleep(4)
if len(state_code)==len(state_name):
    for i in range(0,len(state_code)):
        # time.sleep(0.5)
        pt.click()
    time.sleep(4)
    for i in range(0,len(state_code)):
        pt.typewrite(state_name[i])
        pt.press("tab")
        pt.typewrite(state_code[i])
        pt.press("tab")
