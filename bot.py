import os
from time import sleep, time

from PIL import ImageGrab
from selenium import webdriver
from selenium_helpers import *

IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/images'

def screenGrab():
    box = (0, 194, 2400, 1792)
    screenshot = ImageGrab.grab(box)
    file_location = IMAGE_DIR + '/full_snap__' + str(int(time())) + '.png'
    screenshot.save(file_location, 'PNG')
    print('screenshot saved to {}'.format(file_location))

def main():
    driver = get_chrome_driver()
    try:
        open_game(driver)
        type_in_name(driver, "courtney")
        #select_region(driver)
        start_game(driver)
        print("Waiting for game to start...")
        sleep(3)
        #screenGrab()
        print("sleeping")
        sleep(60)
    except Exception as e:
        print(e)
        driver.close()

if __name__ == '__main__':
    main()
