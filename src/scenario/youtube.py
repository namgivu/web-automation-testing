from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

from src.service.selenium_.snapshot_debug import *
from src.service.selenium_.webdriver import *
from src.service.selenium_.window_size import *
from src.config import WEBDRIVER_REMOTE_HUB

url = 'https://www.youtube.com/user/aprotrainaptechvn'
username = 'demo.apkathon.1@gmail.com'
password = 'demo12345'
wd = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)
driver = webdriver.Chrome()

def human_wise():
    sleep(randint(3, 6))

def login():
    driver.get(url)
    human_wise()
    # click sign in button
    login_btn = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button').click()
    #region input username and password into textbox
    username_box = driver.find_element_by_id('identifierId').send_keys(username)
    human_wise()
    u_next_btn = driver.find_element_by_id('identifierNext')
    ActionChains(driver).move_to_element(u_next_btn)
    u_next_btn.click()
    human_wise()
    password_box = driver.find_element_by_name("password").send_keys(password)
    human_wise()
    p_next_btn = driver.find_element_by_id('passwordNext')
    ActionChains(driver).move_to_element(p_next_btn)
    p_next_btn.click()
    #endregion
    human_wise()

def subscribe():
    human_wise()
    sub_btn = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button')
    if sub_btn.get_attribute('subscribed') == False:
        ActionChains(driver).move_to_element(sub_btn)
        sub_btn.click()
    human_wise()

def like_video():
    human_wise()
    # click video tab
    video_tab = driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]/div')
    ActionChains(driver).move_to_element(video_tab)
    video_tab.click()

    human_wise()
    video = driver.find_elements_by_id('video-title')
    print(len(video))
    for i in video:
        ActionChains(driver).move_to_element(i)
        i.click()
        human_wise()
        for j in video:
            human_wise()
            like_btn = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a')
            ActionChains(driver).move_to_element(like_btn)
            like_btn.click()
            human_wise()
            driver.back()


login()
subscribe()
like_video()