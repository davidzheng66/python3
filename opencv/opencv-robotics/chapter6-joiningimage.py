import cv2
import numpy as np 
img = cv2.imread('resources/lena.jpg')

horizontal_image = np.hstack((img, img))
vertical_image = np.vstack((img, img))

cv2.imshow('Horizontal', horizontal_image)
cv2.imshow('Vertical', vertical_image)

cv2.waitKey(0)

