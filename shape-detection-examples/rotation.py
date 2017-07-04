import cv2
import numpy as np
import imutils

image = cv2.imread('../images/player.png')

# loop over rotation angles and show image
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(0)
