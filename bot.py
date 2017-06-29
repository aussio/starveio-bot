import os
import pyautogui
import math
import threading
import sys

from multiprocessing import Process
from circle import move_mouse_in_circle
from threading import Thread
from time import sleep, time
from PIL import ImageGrab
from selenium import webdriver
from selenium_helpers import *

IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/images'


def screenGrab():
    box = (0, 194, 2400, 1594)
    screenshot = ImageGrab.grab(box)
    file_location = IMAGE_DIR + '/full_snap__' + str(int(time())) + '.png'
    screenshot.save(file_location, 'PNG')
    print('screenshot saved to {}'.format(file_location))

def key_press():
    pyautogui.keyDown('w')
    sleep(0)
    pyautogui.keyUp('w')
    pyautogui.keyDown('a')
    sleep(0)
    pyautogui.keyUp('a')
    pyautogui.keyDown('s')
    sleep(0)
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')
    sleep(0)
    pyautogui.keyUp('d')

def move_circle():
    radius = 200
    steps = 15
    duration = 1
    distance = (math.pi * 2 * radius) / steps
    step_duration = duration / steps
    # generate 360 decimal coordiantes for a circle'ish shape mouse movement
    for i in range(0,steps):
        # Get the decimal coordinate of each 'tick' [0.0,1.0]
        # using sin/cos function
        j = (((i/steps)*2)*math.pi)
        x = math.cos(j)
        y = math.sin(j)
        # plot the mouse coordinates along a oval shape that
        # is centered on the middle of the screen.
        pyautogui.moveRel(distance * x,
                          distance * y,
                          duration = step_duration, # How long it takes to move the mouse each step
                          _pause=False) # Don't add an arbitrary pause between movements

def main():
    driver = get_chrome_driver()
    try:
        open_game(driver)
        type_in_name(driver, "zach")
        #select_region(driver)
        start_game(driver)
        print("Waiting for game to start...")
        sleep(5)
        #click on the screen
        pyautogui.click(600, 300)
        x = 0 
        while x < 5:
            Thread(target = key_press).start()
            Thread(target = move_circle).start()
            x += 1
        #screenGrab()
        #print("sleeping")
        #sleep(60)

    except Exception as e:
        print(e)
        #driver.close()

if __name__ == '__main__':  
    main()
    input("Press enter to quit...")