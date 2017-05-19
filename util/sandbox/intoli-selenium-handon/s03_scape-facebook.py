from selenium import webdriver

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
