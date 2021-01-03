import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
	# Images, Videos and Live Video
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
	# Live video
	capture.set(3, 640) # Width
	capture.set(4, 480) # Height
	capture.set(10, 100) # Brightness


cv.imshow('Cats', img)
cv.imshow('Cats Resized', rescaleFrame(img))

# Reading Videos
capture = cv.VideoCapture('resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if (cv.waitKey(20) & 0xFF) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
