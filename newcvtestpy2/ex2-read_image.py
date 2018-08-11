# Tutorial from https://pythonprogramming.net/loading-images-python-opencv-tutorial/

import cv2
import numpy as np
from matplotlib import pyplot as plt

print("This is a opencv exercise using matplotlib to convert a file to grayscale and save in png format.")
print("Select the grayscale image and press any key to proceed.")

img = cv2.imread('house1.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])    # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300], 'c', linewidth = 5 )
plt.show()

cv2.waitKey(0)
cv2.imwrite('house1.png', img)
cv2.destroyAllWindows()
