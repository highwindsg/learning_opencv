import cv2
import numpy as np

# Imnage file to read in, and read in as color
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# Start by drawing a line on the image file that was read in earlier.
# Line starts at location (0,0), ends at (150,150),
# and color of the line :
# B(blue)G(green)R(red)
# Blue color is (255,0,0)
# Green color is (0,255,0)
# Red color is (0,0,255)
# White color is (255,255,255)
# Black color is (0,0,0)
# And finally 15 pixels.
cv2.line(img, (0,0), (150,150), (255,255,255), 15)

# To show/display the image that we drew the line on.
cv2.imshow('image', img)

# Wait for user to press any key before closing all image window.
cv2.waitKey(0)
cv2.destroyAllWindows()
