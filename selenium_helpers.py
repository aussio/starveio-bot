import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

# Amount of pixels the top of the Chrome browser takes up
Y_OFFSET = 97
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

def get_chrome_driver():
    '''
    The Chrome browser by default has an info bar that Selenium opened it with a test.
    This disables that, sets the window size, and ensures its in the top-right corner.
    1200x900 seems to be the max height on our laptops and just wide enough to not cut off items.
    '''
    chrome_options = Options()
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument(f'window-size={SCREEN_WIDTH},{SCREEN_HEIGHT}')
    chrome_options.add_argument('window-position=0,0')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def type_in_name(driver, name):
    '''
    The nickname input isn't part of the canvas, so we can select the id.
    This selects it and types the passed name.
    '''
    nickname_input = driver.find_element_by_id('nickname_input')
    actions = ActionChains(driver)
    actions.click(on_element=nickname_input)
    actions.send_keys(name)
    actions.perform()

def select_region(driver, region='WA#7'):
    '''
    Selects the specified region from the dropdown on the starting screen.
    Should do retries for world full later...
    '''
    select = Select(driver.find_element_by_id('region_select'))
    options = select.options
    for option in options:
        if region in option.get_attribute("value"):
            option.click()

def open_game(driver):
    '''
    Open the starve.io page and wait a sec for things to load.
    '''
    #driver.set_window_position(0, 0)
    print("Loading game")
    driver.get("http://starve.io/")
    sleep(2)
    print("Game Loaded!")

def start_game(driver):
    '''
    Click the "PLAY" button.
    To move to a specific pixel location, you have to move FROM an element.
    Therefor, we're moving from the top-left by using the game_body, which is the whole game.
    '''
    top_left = driver.find_element_by_id("game_body")
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(top_left,
        SCREEN_WIDTH / 2,
        590 - Y_OFFSET)
    actions.click()
    actions.perform()
    print("Clicking the PLAY button!")
