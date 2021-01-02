import cv2 as cv

img = cv.imread('resources/Photos/cat.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    if (cv.waitKey(20) & 0xFF) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()