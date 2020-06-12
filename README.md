# webdriver infra via selenium hub
ref. https://github.com/SeleniumHQ/docker-selenium#via-docker-compose

# install & run test
require python & pipenv ref. bit.ly/nnpipenv
```bash
pipenv sync

PYTHONPATH=`pwd` pipenv run pytest ./tests/test_demo_googlesearch.py::Test::test_Chrome
PYTHONPATH=`pwd` pipenv run pytest ./tests/test_demo_googlesearch.py::Test::test_Firefox
```


# misc hint

## speed up by using headless
avoid starting Xvfb server
-e START_XVFB=false
https://github.com/SeleniumHQ/docker-selenium#running-in-headless-mode


## aftermath seleniumhub check
/wd/hub/status endpoint
https://github.com/SeleniumHQ/docker-selenium#waiting-for-the-grid-to-be-ready

check-grid.sh script
https://github.com/SeleniumHQ/docker-selenium#adding-a-healthcheck-to-the-grid
