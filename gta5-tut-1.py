import numpy as np
from PIL import ImageGrab
import cv2
import time

def capture_screen(wait=True):
    box = (0, 194, 1200, 800)
    screen =  np.array(ImageGrab.grab(box))
    # timer
    # convert color
    # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    # show image in new window
    cv2.imshow('window',screen)
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

capture_screen()
#screen_record()
