import os
import time

from PIL import ImageGrab
from selenium import webdriver
from selenium_helpers import *

IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/images'

def screenGrab():
    box = ()
    screenshot = ImageGrab.grab()
    screenshot.save(IMAGE_DIR + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    driver = get_chrome_driver()
    try:
        open_game(driver)
        type_in_name(driver, "courtney")
        print("sleeping")
        time.sleep(60)
        #screenGrab()
    except Exception as e:
        print(e)
        driver.close()

if __name__ == '__main__':
    main()
