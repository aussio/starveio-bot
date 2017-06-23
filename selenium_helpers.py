import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Amount of pixels the top of the Chrome browser takes up
Y_OFFSET = 97

def get_chrome_driver():
    '''
    The Chrome browser by default has an info bar that Selenium opened it with a test.
    This disables that, sets the window size, and ensures its in the top-right corner.
    '''
    chrome_options = Options()
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('window-size=1000,1000')
    chrome_options.add_argument('window-position=0,0')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def get_firefox_driver():
    return webdriver.Firefox()

def type_in_name(driver, name):
    '''
    The nickname input isn't part of the canvas, so we can select the id.
    This selects it and types the passed name.
    '''
    nickname_input = driver.find_element_by_id('nickname_input')
    actions = ActionChains(driver)
    actions.move_to_element(nickname_input)
    actions.click(nickname_input)
    actions.send_keys(name)
    actions.perform()

def minimize_screen(driver):
    ''' Doesn't seem to work for some reason...'''
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.COMMAND, Keys.SUBTRACT)

def open_game(driver):
    '''
    Open the starve.io page and wait a sec for things to load.
    '''
    #driver.set_window_position(0, 0)
    print("Loading game")
    driver.get("http://starve.io/")
    time.sleep(2)
    print("Game Loaded!")

def start_game(driver):
    '''
    Click the "PLAY" button.
    To move to a specific pixel location, you have to move FROM an element.
    Therefor, we're moving from the top-left by using the game_body, which is the whole game.
    '''
    top_left = driver.find_element_by_id("game_body")
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(top_left, 500, 670 - Y_OFFSET).click().perform()
    print("Clicking the PLAY button!")
