#snapshot debug
SNAPSHOT_DEBUG = True   # means DO   take snapshot during the test run - CAUTION: your snapshot folder, eg. $CODE/_snapshot_ may consume lots of your volume, don't forget to clean it up after used
SNAPSHOT_DEBUG = False  # means DONT take snapshot during the test run

#webdriver hub address
WEBDRIVER_REMOTE_HUB = ''                               # use webdriver directly aka. no-hub
WEBDRIVER_REMOTE_HUB = 'http://localhost:4444/wd/hub'   # use webdriver via selenium hub on port 4444 locally
WEBDRIVER_REMOTE_HUB = 'http://0.1.22.333:4444/wd/hub'  # use webdriver via selenium hub on port 4444 served from this ip
