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

def key_press(key1, key2, key3, key4, timing):
    pyautogui.keyDown(key1)
    sleep(timing)
    pyautogui.keyUp(key1)
    pyautogui.keyDown(key2)
    sleep(timing)
    pyautogui.keyUp(key2)
    pyautogui.keyDown(key3)
    sleep(timing)
    pyautogui.keyUp(key3)
    pyautogui.keyDown(key4)
    sleep(timing)
    pyautogui.keyUp(key4)

def move_circle(radius, steps, duration):
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
        
        p1 = Process(target = key_press, args = ('w', 'a', 's', 'd', 1))
        p2 = Process(target = move_circle, args = (200, 15, 4))

        pyautogui.click(600, 300)

        p1.start()
        p2.start()

    except Exception as e:
        print(e)
        driver.close()

if __name__ == '__main__':  
    main()
    