import cv2
import numpy as np
from matplotlib import pyplot as plt

print("This is a opencv exercise to convert a file to grayscale and save in png format.")
#read the picture in grayscale first
img = cv2.imread('house1.jpg', cv2.IMREAD_GRAYSCALE)

#this will display the image in grayscale
cv2.imshow('image',img)

#click on the gray picture and waiting for user to press any key
cv2.waitKey(0)

#once any key is pressed, cv2 will save to the new filename
cv2.imwrite('house1gray.png', img)

#and after saving the new filename, will then close the gray picture file
cv2.destroyAllWindows()
