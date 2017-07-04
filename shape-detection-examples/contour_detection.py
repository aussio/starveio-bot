import cv2
import numpy as np

class Images():
    def __init__(self):
        self.image_list = {}

    def add_to_image_list(self, name, image):
        self.image_list[name] = np.copy(image)
        return image

    def show_image(self, name, image):
        print('showing image:', name)
        cv2.imshow(name, image)
        cv2.waitKey(0)

    def show_multiple_images(self, names):
        '''
        Params:
            names - a tuple of names
        '''
        def get_value(name):
            return self.image_list[name]

        images = tuple(map(get_value, names))
        combo = np.concatenate(images, axis=1)
        self.show_image('-'.join(names), combo)

if __name__ == '__main__':
    i = Images()
    # original
    image = i.add_to_image_list('original',
                                cv2.imread('../images/starveio-example-objects.png'))
    # convert to gray
    image = i.add_to_image_list('grayscale',
                                cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
    # threshold to get better grayscale
    # I manually found to use 62 to capture the trees but not the ground spots
    image = i.add_to_image_list('threshold',
                                cv2.threshold(image, 62, 255, cv2.THRESH_BINARY)[1])
    # find all contours
    _, contours, hierarchy = cv2.findContours(image,
                                              cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)
    image = i.add_to_image_list('contours',
                                cv2.drawContours(image,
                                                 contours,
                                                 -1,        # which contours to draw
                                                 (124,252,124), # color of drawn lines
                                                 2))        # thickness of drawn lines

    i.show_multiple_images(('grayscale', 'threshold', 'contours'))
