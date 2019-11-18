from src.service.selenium_.snapshot_debug import *
from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB
from time import sleep

url = 'https://www.facebook.com/aptechvietnam.hcm'
username = 'vippro56@yahoo.com.vn'
password = 'matkhau1'
wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

#TODO Trang 1 create human_wise() to sleep() in random
#TODO Trang 2 add comment at each step to clarify what it is for

wd.get(url)
sleep(3)

#region TODO Trang 2a login facebook
username_box = wd.find_element_by_id("email").send_keys(username)
sleep(3)

password_box = wd.find_element_by_id("pass").send_keys(password)
sleep(3)
#endregion


#TODO Trang 2x what is this step for?
login_btn = wd.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()
sleep(3)
takeSnapshot(wd, printOutcome=True, suffix='snap0', forceSnapshot=True)
