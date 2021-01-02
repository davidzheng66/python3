import cv2
import numpy as np 

img =cv2.imread('resources/playingcards.jpg')

width, height = 250, 250

pts1 = np.float32([[192, 68], [290, 119], [126, 198], [222, 246]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Image Output', imgOutput)

cv2.waitKey(0)