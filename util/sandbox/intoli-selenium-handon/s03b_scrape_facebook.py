from selenium import webdriver

from s03a_config import *
from s03a_config_local import *


##region webdriver option

#create options that be passed to the WebDriver initializer
options = webdriver.ChromeOptions()

#tell selenium to use the beta/dev channel version of chrome
options.binary_location = '/usr/bin/google-chrome-unstable'

#set headless mode for chrome
options.add_argument('headless')

#set the window size
options.add_argument('window-size=1200x600')

#more options go here ref. https://sites.google.com/a/chromium.org/chromedriver/capabilities

##endregion webdriver option


#initialize the driver
driver = webdriver.Chrome(chrome_options=options) #If nothing happens then everything worked! Normally, a new browser window would pop open at this point with a warning about being controlled by automated test software. It not appearing is exactly what we want to happen in headless mode and it means that we could be running our code on a server that doesn't even have a graphical environment. Everything from here on out is just standard Selenium so if you were only trying to figure out how to get it working with Chrome in headless mode then that's it!


##regoin scraping facebook account
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
driver.get_screenshot_as_file('%s/00.fb-login-page.png' % PRIVATE_HOME)


#do login
loginBtn.click() #this click might lead to 2-factor login page
driver.implicitly_wait(1)
driver.get_screenshot_as_file('%s/01.fb-after-login.png' % PRIVATE_HOME)

#navigate to my profile
driver.get('https://www.facebook.com/%s' % FB_USER)

# take another screenshot
driver.get_screenshot_as_file('%s/02.fb-profile-page.png' % PRIVATE_HOME)

##endregoin scraping facebook account
