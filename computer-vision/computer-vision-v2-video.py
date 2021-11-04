# This script will detect + track an individual oscilating face via your webcam
# First of its kind frontal classifier + tracking system
# SHPE Innovation Challenge 2021 - Santiago Gomez Paz

import cv2
import math
import sys
from pathlib import Path

THRESHOLD_A = 20
THRESHOLD_B = 50

# Import video captures
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = "./videos/santi.mp4"

cap = cv2.VideoCapture(path)

# Create the lbp cascade, better performance than haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")

# Get first set of frames
ret, last_frame = cap.read()

# Initialize variables
tracker_cnt = 0
face_w = 100
face_h = 100
face_x = int((last_frame.shape[1] - face_w) / 2)
face_y = int((last_frame.shape[0] - face_h) / 2)

center_x = 0
center_y = 0
prev_center_x = 0
prev_center_y = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=4,
        minSize=(20, 20)
    )

    # Draw a rectangle around the face
    cnt = 0
    prev_center_x = center_x
    prev_center_y = center_y
    if(type(faces) != tuple):
        tracker_cnt = 0
        for (x, y, w, h) in faces:
            if(cnt == 0):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                face_x = x
                face_y = y
                face_w = w
                face_h = h
                center_x = x + w/2
                center_y = y + h/2
                cnt = cnt + 1

    elif(type(faces) == tuple):  # If there's no face, the type of faces is tuple
        if(tracker_cnt == 0):

            # Set up tracker.
            tracker_type = 'MIL'

            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
            if tracker_type == 'CSRT':
                tracker = cv2.TrackerCSRT_create()
            if tracker_type == 'MOSSE':
                tracker = cv2.TrackerMOSSE_create()

            # Define an initial bounding box
            bbox = (face_x, face_y, face_w, face_h)

            # Initialize tracker with first frame and bounding box
            ok = tracker.init(last_frame, bbox)

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            center_x = int(bbox[0] + bbox[2]/2)
            center_y = int(bbox[1] + bbox[3]/2)
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        tracker_cnt = tracker_cnt + 1

    # Save last frame
    last_frame = frame

    # Display face movement speed
    speed = math.sqrt(pow(center_x - prev_center_x, 2) +
                      pow(center_y - prev_center_y, 2))
    speed = int(speed * 100) / 100   # Round to 2 decimals

    # Display speed in the frame
    if (speed < THRESHOLD_A):
        cv2.putText(frame, "Motion: " + str(speed), (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    elif (speed < THRESHOLD_B):
        cv2.putText(frame, "Motion: " + str(speed), (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
    else:
        cv2.putText(frame, "Motion: " + str(speed), (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
