import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('window-size=1000,1000')
    chrome_options.add_argument('window-position=0,0')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def get_firefox_driver():
    return webdriver.Firefox()

def type_in_name(driver, name):
    nickname_input = driver.find_element_by_id('nickname_input')
    actions = ActionChains(driver)
    actions.move_to_element(nickname_input)
    actions.click(nickname_input)
    actions.send_keys(name)
    actions.perform()

def minimize_screen(driver):
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.COMMAND, Keys.SUBTRACT)

def open_game(driver):
    #driver.set_window_position(0, 0)
    print("Loading game")
    driver.get("http://starve.io/")
    print("Game loaded!")
    print("wait for some animations")
    time.sleep(2)
