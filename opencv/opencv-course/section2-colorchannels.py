#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)