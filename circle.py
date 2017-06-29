import pyautogui
import math
import sys
from time import sleep, time

def move_mouse_in_circle(radius, steps, duration=1):
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


#if __name__ == '__main__':
#	sleep(5)
#    num_circles = 10
#    for _ in range(num_circles):
#        move_mouse_in_circle(200, 15, 1)