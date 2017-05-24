from common import *

from s03a_config import *
from s03a_config_local import *


#define output
SNAPSHOTS=dict(
  loginPage   = '%s/00.fb-login-page.png' % PRIVATE_HOME,
  afterLogin  = '%s/01.fb-after-login.png' % PRIVATE_HOME,
  profilePage = '%s/02.fb-profile-page.png' % PRIVATE_HOME,
)


#load Chrome WebDriver
driver = loadWebDriverCHROME()


##region scraping facebook account
driver.get('https://facebook.com')

#wait up to 10 seconds for the elements to become available
driver.implicitly_wait(1)

#use css selectors to grab the login inputs
email = driver.find_element_by_css_selector('input[type=email]')
passw = driver.find_element_by_css_selector('input[type=password]')
loginBtn = driver.find_element_by_css_selector('#loginbutton > input')


#enter login credentials
email.send_keys(FB_USER)
passw.send_keys(FB_PASS)

#snapshot the login page
driver.get_screenshot_as_file(SNAPSHOTS['loginPage'])


#do login
loginBtn.click() #this click might lead to 2-factor login page
driver.implicitly_wait(1)
driver.get_screenshot_as_file(SNAPSHOTS['afterLogin'])

#navigate to my profile
driver.get('https://www.facebook.com/%s' % FB_USER)

#take another screenshot
driver.get_screenshot_as_file(SNAPSHOTS['profilePage'])

##endregion scraping facebook account


#print output snapshot paths
for name,path in SNAPSHOTS.items():
  print('%s %s' % (name, path) )
