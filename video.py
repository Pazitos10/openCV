import numpy as np
import cv2
import time 

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/pablo/Descargas/haarcascade_frontalface_default.xml')


n_frames = 1
start = time.time()

while(True):
    # Capture frame-by-frame
    
    ret, frame = cap.read()
    total_time = time.time() - start
    fps = n_frames / total_time
    print str(fps)
    start = time.time()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()