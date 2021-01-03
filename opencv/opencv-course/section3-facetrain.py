#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'resources/Faces/train'
people = []
for person in os.listdir(DIR):
    people.append(person)

print(people)

haar_cascade = cv.CascadeClassifier('resources/Xml/haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # face region of image
                features.append(faces_roi)
                labels.append(label)
 
create_train()
print('Training done ---------------')

# print('The length of features: ', len(features))
# print('The length of labels: ', len(labels))

features = np.array(features, dtype='object')
labels = np.array(labels)

# print('The shape of features: ', features.shape)
# print('The shape of labels: ', labels.shape)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('resources/Xml/face_trained.yml')
np.save('resources/Xml/features.npy', features)
np.save('resources/Xml/labels.npy', labels)