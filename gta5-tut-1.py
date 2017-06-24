import numpy as np
from PIL import ImageGrab
import cv2
import time

TOP_LEFT_X = 0
TOP_LEFT_Y = 100
BOT_RIGHT_X = 720
BOT_RIGHT_Y = 800

WIDTH = BOT_RIGHT_X - TOP_LEFT_X
HEIGHT = BOT_RIGHT_Y - TOP_LEFT_Y

def capture_screen(wait=True):
    box = (TOP_LEFT_X * 2,
           TOP_LEFT_Y * 2,
           BOT_RIGHT_X * 2,
           BOT_RIGHT_Y * 2
           )
    screen = np.array(ImageGrab.grab(box).convert('RGB'))
    # convert color
    b, g, r = cv2.split(screen)
    screen = cv2.merge([r, g, b])
    # setup window settings
    window_title = "ZachWasHere"
    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
    # resize window
    cv2.resizeWindow(window_title, WIDTH, HEIGHT)
    # resize image
    screen = cv2.resize(screen, (WIDTH, HEIGHT))
    # create window and display image
    cv2.imshow(window_title, screen)
    if wait:
        cv2.waitKey()

def screen_record():
    last_time = time.time()
    while(True):
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        capture_screen(wait=False)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

#capture_screen()
screen_record()
