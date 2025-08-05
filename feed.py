import numpy as np
import cv2 as cv

cap = cv.VideoCapture('http://192.168.31.231:8080/video')

if not cap.isOpened():
    print("Cannot Open Camera")
    exit()
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Cant recieve frame (stream end ?), Exiting.....")
        break
    
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()