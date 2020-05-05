import unittest

from src.config import WEBDRIVER_REMOTE_HUB
from src.service.selenium_.snapshot_debug import takeSnapshot
from src.service.selenium_.webdriver import loadWebDriver, wait4VisibleXPath
from src.service.selenium_.window_size import WindowSize


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

    def tearDown(self): pass  # nothing here for now


    def test_1(self):
        url = 'https://www.google.com'

        self.wd.get(url)

        title = self.wd.title
        assert title == 'Google'


    def test_2(self):
        url = 'https://www.google.com'

        self.wd.get(url)

        # locate logo and take snapshot and stored under ./src/_snapshot_/vault/
        x = '//*[@id="hplogo"]'
        _ = wait4VisibleXPath(self.wd, x); takeSnapshot(self.wd, forceSnapshot=True)
