"""ref. http://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example"""

from common import *
from s03a_config_local import *

from selenium.webdriver.support.ui import WebDriverWait #available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC #available since 2.26.0

driver = loadWebDriverCHROME() #use chrome-webdriver
driver.get('http://fb.com/%s' % FB_USER) #open profile page of the facebook user
WebDriverWait(driver, timeout=10).until(EC.title_contains(FB_USER_FULLNAME)) #wait to ensure it's loaded
html = driver.page_source #get html text of the page

#search string with regex ref. https://stackoverflow.com/a/4667014/248616
import re
m = re.search('meta http-equiv="refresh" content="0; URL=/([^?]+)\?', html)
username = m.group(1)
print(username)