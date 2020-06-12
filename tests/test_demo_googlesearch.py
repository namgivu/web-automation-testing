from src.service.selenium import load_webdriver, BROWSER
from tests._util_ import run_googlesearchdemo

class Test:
    """
    b   aka  browser_name
    wd  aka  webdriver
    """

    def test_Chrome(self):
        b=BROWSER.Chrome    ; run_googlesearchdemo(wd=load_webdriver(b), tag=f'{b}_demo')

    def test_Firefox(self):
        b=BROWSER.Firefox   ; run_googlesearchdemo(wd=load_webdriver(b), tag=f'{b}_demo')
