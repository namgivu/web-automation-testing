from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv


def load_envvar(envvar_name):
    AH    = os.path.abspath(f'{__file__}/../../..')  # AH aka APP_HOME
    env_f = f'{AH}/.env'
    load_dotenv(dotenv_path=env_f, override=True)
    v = os.environ.get(envvar_name)
    return v


def load_webdriver(b:'browser choice'):
    SELENIUM_HUB_URL = load_envvar('SELENIUM_HUB_URL')
    if not SELENIUM_HUB_URL: raise Exception('SELENIUM_HUB_URL is required in envvar')
    #TODO ensure we have a working seleniumhub at :SELENIUM_HUB_URL

    #region create :wd
    options = Options()
    options.add_argument("--start-maximized")

    wd = webdriver.Remote(  # wd aka webdriver
        options=options,
        command_executor=SELENIUM_HUB_URL,
        desired_capabilities=desired_capabilities_from_browser_choice(b),
    )
    wd.implicitly_wait(20)
    return wd
    #endregion create :wd


def desired_capabilities_from_browser_choice(b:'browser choice'):
    dc = None  # dc aka desired_capabilities
    if b==BROWSER.Chrome:  dc=DesiredCapabilities.CHROME
    if b==BROWSER.Firefox: dc=DesiredCapabilities.FIREFOX
    return dc


class BROWSER:
    Chrome  = 'chrome'
    Firefox = 'firefox'
