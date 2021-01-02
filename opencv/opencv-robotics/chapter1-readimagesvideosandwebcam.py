import cv2
import pandas

print(cv2.__version__)

# Read an image
img = cv2.imread('resources/lena.jpg')
print(img.shape)

imgResize = cv2.resize(img, (500, 500))
cv2.imshow('Output', imgResize)

cv2.waitKey(0)

# Read a video
# cap = cv2.VideoCapture('resources/massage.mp4')

# while True:
# 	success, img = cap.read()
# 	cv2.imshow('Video', img)
# 	if cv2.waitKey(1) & (0xFF == ord('q')):
# 		break

#Read a WebCam
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Width
cap.set(4, 480) # Height
cap.set(10, 100) # Brightness

while True:
	success, img = cap.read()
	cv2.imshow('Video', img)
	if (cv2.waitKey(1) & 0xFF) == ord('q'):
		break
