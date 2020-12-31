import cv2
print(cv2.__version__)

img = cv2.imread('resources/fig1.png')
cv2.imshow('Output', img)
cv2.waitKey(1000)
