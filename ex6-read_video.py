# https://pythonprogramming.net/drawing-writing-python-opencv-tutorial/?completed=/loading-video-python-opencv-tutorial/

import cv2
import numpy as np

# Imnage file to read in, and read in as color
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# Start by drawing a line on the image file that was read in earlier.
# Line starts at location (0,0), ends at (150,150).
# (0,0) means location (x,y) which is the top left corner of the image frame.
# Therefore the line draw from top left and down to center of the frame.
#
# And color of the line :
# B(blue)G(green)R(red)
# Blue color is (255,0,0)
# Green color is (0,255,0)
# Red color is (0,0,255)
# White color is (255,255,255)
# Black color is (0,0,0)
# And finally 15 pixels.
cv2.line(img, (0,0), (150,150), (255,255,255), 15)

# Drawing a rectangle.
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)

# To show/display the image that we drew the line on.
cv2.imshow('image', img)

# To draw a circle.
# (100,63) is the center of the circle
# 55 is the radius of the circle
# (0,0,255) is red color
# -1 means the circle will be fill-in the color of the circle.
cv2.circle(img, (100,63), 55, (0,0,255), -1)

# Wait for user to press any key before closing all image window.
cv2.waitKey(0)
cv2.destroyAllWindows()
