# Tutorial from https://pythonprogramming.net/loading-images-python-opencv-tutorial/

import cv2
import numpy as np
from matplotlib import pyplot as plt

print("This is a opencv exercise to convert a file to grayscale and save in png format.")
print("Select the grayscale image and press any key to proceed.")
# Read the picture in grayscale first
# as the default is going to be IMREAD_COLOR
#img = cv2.imread('house1.jpg', cv2.IMREAD_GRAYSCALE)

# Rather than using the IMREAD_COLOR, you can also use numbers
# For the second parameter, you can use -1, 0 or 1
# Color is 1, grayscale is 0 and unchanged is -1
img = cv2.imread('watch.jpg', 0)

# This will display the image in grayscale,
# and we use cv2.imshow(title,image) to show the image.
cv2.imshow('image', img)

# Click on the gray picture and waiting for user to press any key
cv2.waitKey(0)

# Once any key is pressed, cv2 will save to the new filename
#cv2.imwrite('house1gray.png', img)
cv2.imwrite('watch.png', img)

# And after saving the new filename, will then close the gray picture file
cv2.destroyAllWindows()
