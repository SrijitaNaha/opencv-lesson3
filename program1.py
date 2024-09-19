##### Grayscaling of an image read as colored

import cv2
 
image = cv2.imread('pika.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 