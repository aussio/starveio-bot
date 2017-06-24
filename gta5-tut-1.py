import numpy as np
import cv2
import time

from PIL import ImageGrab, Image
from mss.darwin import MSS as mss

TOP_MAC_BAR = 21
CHROME_EXTRAS = 97
TOP_LEFT_Y = CHROME_EXTRAS - TOP_MAC_BAR

class ScreenCapture:
    def __init__(self):
        '''  '''
        self.captured_area = {}

    def capture_screen(self):
        '''
        Captures an Image based upon the relative size of the computer's first monitor.

        Right now we've hardcoded to only capture the left-half of the screen and to not capture
            the top part of a Chrome window (without bookmarks bar).
        '''
        try:
            with mss() as sct:
                # We retrieve monitors informations:
                monitors = sct.enum_display_monitors()

                # Get rid of the first, as it represents the "All in One" monitor:
                for num, monitor in enumerate(monitors[1:], 1):
                    # Capture starting from below the Chrome header
                    self.captured_area['top'] = monitor['top'] + TOP_LEFT_Y
                    # Capture starting from far left of screen
                    self.captured_area['left'] = monitor]['left']
                    # Capture only half the width of the monitor
                    self.captured_area['width'] = monitor['width'] // 2
                    # Capture entire rest of monitor height
                    self.captured_area['height'] = monitor['height'] - captured_area['top']

                    # This functions sets the sct.width, sct.height, and sct.image for below
                    sct.get_pixels(self.captured_area)

                    size = (sct.width, sct.height)
                    return Image.frombytes('RGB', size, sct.image)
        except ScreenshotError as ex:
            print(ex)

    def process_image(self, screen, color_conversion_type):
        '''
        Convert image's color to color_conversion_type, and resize image to window's size.
        '''
        # convert color
        screen = cv2.cvtColor(screen, color_conversion_type)
        # resize image
        screen = cv2.resize(screen,
                            (self.captured_area['width'],
                             self.captured_area['height'])
                           )
        return screen

    def create_window(self, wait=True):
        screen = np.array(self.capture_screen())
        screen = self.process_image(screen, cv2.COLOR_RGB2BGR)

        # setup window settings
        window_title = "ZachWasHere"
        cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
        # resize window
        cv2.resizeWindow(window_title,
                         self.captured_area['width'],
                         self.captured_area['height'])

        # create window and display image
        cv2.imshow(window_title, screen)
        if wait:
            cv2.waitKey()

    def screen_record(self):
        last_time = time.time()
        while(True):
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            self.create_window(wait=False)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == '__main__':
    sc = ScreenCapture()
    #sc.capture_screen()
    sc.screen_record()
