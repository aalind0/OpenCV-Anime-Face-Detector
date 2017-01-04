# Haar Cascade Anime Face Detection
import cv2
import numpy as np

# loading in the cascades.
face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Reading the image.
img = cv2.imread('anime.jpg')

# detection and drawing rectangles
while True:
    #converting the image to grayscale for easier processing.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
      
    # Press 'ESC' to release the camera.        
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
