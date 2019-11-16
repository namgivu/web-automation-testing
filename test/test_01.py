import unittest

from src.config import WEBDRIVER_REMOTE_HUB
from src.service.selenium_.webdriver import loadWebDriver
from src.service.selenium_.window_size import WindowSize


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)

    def tearDown(self): pass  # nothing here for now

    def test_homepage(self):
        url = 'https://aptechvietnam.com.vn/apkathon2019/'
        self.wd.get(url)
        title = self.wd.title
        assert title=='Cuộc thi Apkathon 2019 - Hệ thống Đào tạo Lập trình viên Quốc tế Aptech'
