import numpy as np
import cv2
import os
from PIL import Image


def collect(id):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    #For each person provide a numeric face id
    faceID = id
    #  input('\n enter a user id and press <return> ==> ')
    print ( "\n [INFO] Initializing face capture. Look the camera and wait...")

    # Initialize individual sampling face count
    count = 0
    while(True):
        ret, image = cap.read()
        # frame = cv2.flip(frame, -1) # Flip camera vertically / no need on windows camera
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( gray_image, 1.2, 5 ) # returns rectangles with (x,y,w,h) coordinates for each face

        #(x,y) top right corner, w for width, h for height 
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            count +=1
            roi_gray = gray_image[y:y+h, x:x+w] # take only the square
            cv2.imwrite("dataset/User." + str(faceID) + '.' + str(count) + ".jpg", roi_gray)
            cv2.imshow('image', image)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
        elif count >= 30: # Take 30 face sample and stop video
            break
        
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")

    cap.release()
    cv2.destroyAllWindows()