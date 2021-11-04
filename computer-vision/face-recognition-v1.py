# This script will detect faces via your webcam.
# SHPE Innovation Challenge 2021 - Santiago Gomez Paz

import cv2

cap = cv2.VideoCapture(0)

# Create the haar cascade
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface.xml")
# faceCascade = cv2.CascadeClassifier("lbpcascade_profileface.xml")
faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
# faceCascade = cv2.CascadeClassifier("haarcascade_eye.xml")


x_coord = 0
y_coord = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    # Save previous coordinates
    prev_x_coord = x_coord
    prev_y_coord = y_coord

    # Draw a rectangle around the face
    cnt = 0
    for (x, y, w, h) in faces:
        if(True):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            x_coord = x + w / 2
            y_coord = y + h / 2
            cnt = cnt+1

    # Print difference between previous and current coordinates
    difference = pow(x_coord - prev_x_coord, 2) + \
        pow(y_coord - prev_y_coord, 2)
    print(difference)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
