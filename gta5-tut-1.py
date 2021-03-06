import numpy as np
import cv2
import time


from PIL import ImageGrab, Image
from mss.darwin import MSS as mss
#from directkeys import PressKey, W, A, S, D



TOP_MAC_BAR = 21
CHROME_EXTRAS = 97
TOP_LEFT_Y = CHROME_EXTRAS - TOP_MAC_BAR

class ScreenCapture:
    def __init__(self):
        self.captured_area = {}

    def capture_screen(self):
        '''
        Captures an Image based upon the relative size of the computer's first monitor.

        Right now we've hardcoded to only capture the left-half of the screen and to not capture
            the top part of a Chrome window (without bookmarks bar).

        Returns:
            PIL.Image
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
                    self.captured_area['left'] = monitor['left']
                    # Capture only half the width of the monitor
                    self.captured_area['width'] = monitor['width'] // 2
                    # Capture entire rest of monitor height
                    self.captured_area['height'] = monitor['height'] - self.captured_area['top']

                    # This functions sets the sct.width, sct.height, and sct.image for below
                    sct.get_pixels(self.captured_area)

                    size = (sct.width, sct.height)
                    return Image.frombytes('RGB', size, sct.image)
        except ScreenshotError as ex:
            print(ex)

    def process_image(self, image, color_conversion_type, canny=True):
        '''
        Convert image's color to color_conversion_type, and resize image to window's size.

        Params:
            screen: A numpy.array of an image
            color_conversion_type: A cv2 color conversion constant

        Returns:
            numpy.array
        '''
        original_image = image
        # convert color
        image = cv2.cvtColor(image, color_conversion_type)

        if canny:
            # edge detection
            min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
            max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
            image = cv2.Canny(image, min_value, max_value)
            #image = cv2.Canny(image, 40, 65)

        # resize image
        image = cv2.resize(image,
                            (self.captured_area['width'],
                             self.captured_area['height'])
                           )
        return image

    def create_window(self, window_title, wait=True):
        '''
        Creates a window that is the same size as the created image from capture_screen

        Params:
            wait: Whether or not he window should wait for user input before closing.
        '''
        screen = np.array(self.capture_screen())
        screen = self.process_image(screen, cv2.COLOR_RGB2GRAY)

        # setup window settings
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
        '''
        Runs self.create_window() in an endless loop
        Also prints out the time it took to refresh each frame.
        '''
        for i in list(range(4))[::-1]:
            print(i+1)
            time.sleep(1)

        last_time = time.time()
        while(True):
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            self.create_window('canny', wait=False)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == '__main__':
    sc = ScreenCapture()
    #sc.capture_screen()
    sc.screen_record()
