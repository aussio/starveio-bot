import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    box = (0, 194, 1200, 800)
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  ImageGrab.grab(box)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',np.array(printscreen))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
