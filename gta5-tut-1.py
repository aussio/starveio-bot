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
        self.captured_area = {}

    def get_image(self):
        try:
            with mss() as sct:
                # We retrieve monitors informations:
                monitors = sct.enum_display_monitors()

                # Get rid of the first, as it represents the "All in One" monitor:
                for num, monitor in enumerate(monitors[1:], 1):
                    # Get raw pixels from the screen.
                    # This method will store screen size into `width` and `height`
                    # and raw pixels into `image`.
                    # Don't capture chrome header
                    monitor['top'] = monitor['top'] + TOP_LEFT_Y
                    monitor['width'] = monitor['width'] // 2
                    monitor['height'] = monitor['height'] - TOP_LEFT_Y
                    # set self.monitor for sharing.
                    self.captured_area = monitor
                    sct.get_pixels(self.captured_area)

                    # Create an Image
                    size = (sct.width, sct.height)
                    return Image.frombytes('RGB', size, sct.image)
        except ScreenshotError as ex:
            print(ex)

    def capture_screen(self, wait=True):
        screen = np.array(self.get_image())
        # convert color
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        # setup window settings
        window_title = "ZachWasHere"
        cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
        # resize window
        cv2.resizeWindow(window_title,
                         self.captured_area['width'],
                         self.captured_area['height'])
        # resize image
        screen = cv2.resize(screen,
                            (self.captured_area['width'],
                             self.captured_area['height'])
                           )

        # create window and display image
        cv2.imshow(window_title, screen)
        if wait:
            cv2.waitKey()

    def screen_record(self):
        last_time = time.time()
        while(True):
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            self.capture_screen(wait=False)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == '__main__':
    sc = ScreenCapture()
    #sc.capture_screen()
    sc.screen_record()
