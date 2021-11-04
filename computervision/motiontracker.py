from streamlit_webrtc import VideoProcessorBase
import math
import cv2
import av


class VideoProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(image, format="bgr24")


# class VideoProcessor(VideoProcessorBase):
#     def __init__(self):
#         self.faceCascade = cv2.CascadeClassifier(
#             "./computervision/classifiers/lbpcascade_frontalface_improved.xml")

#         # Initialize variables
#         self.tracker_cnt = 0
#         self.face_w = 100
#         self.face_h = 100
#         self.face_x = 0
#         self.face_y = 0

#         self.center_x = 0
#         self.center_y = 0
#         self.prev_center_x = 0
#         self.prev_center_y = 0

#         self.THRESHOLD_A = 20
#         self.THRESHOLD_B = 50

#     def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
#         img = frame.to_ndarray(format="bgr24")

#         # Detect faces in the image
#         faces = self.faceCascade.detectMultiScale(
#             img,
#             scaleFactor=1.1,
#             minNeighbors=3,
#             minSize=(30, 30)
#         )

#         # Draw a rectangle around the face
#         cnt = 0
#         self.prev_center_x = self.center_x
#         self.prev_center_y = self.center_y

#         if(type(faces) != tuple):
#             self.tracker_cnt = 0
#             for (x, y, w, h) in faces:
#                 if(cnt == 0):
#                     img = cv2.rectangle(
#                         img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#                     self.face_x = x
#                     self.face_y = y
#                     self.face_w = w
#                     self.face_h = h
#                     self.center_x = x + w/2
#                     self.center_y = y + h/2
#                     cnt = cnt + 1

#         elif(type(faces) == tuple):  # If there's no face, the type of faces is tuple
#             if(self.tracker_cnt == 0):
#                 # Set up tracker
#                 self.tracker = cv2.TrackerMIL_create()

#                 # Define an initial bounding box
#                 bbox = (self.face_x, self.face_y, self.face_w, self.face_h)

#                 # Initialize tracker with first frame and bounding box
#                 try:
#                     ok = self.tracker.init(self.last_img, bbox)
#                 except:
#                     ok = self.tracker.init(img, bbox)
#             # Update tracker
#             ok, bbox = self.tracker.update(img)

#             # Draw bounding box
#             if ok:
#                 # Tracking success
#                 p1 = (int(bbox[0]), int(bbox[1]))
#                 p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
#                 self.center_x = int(bbox[0] + bbox[2]/2)
#                 self.center_y = int(bbox[1] + bbox[3]/2)
#                 img = cv2.rectangle(img, p1, p2, (255, 0, 0), 2, 1)
#             else:
#                 # Tracking failure
#                 img = cv2.putText(img, "Tracking failure detected", (100, 80),
#                                   cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

#             self.tracker_cnt = self.tracker_cnt + 1

#         # Save last frame
#         self.last_img = img

#         # Display face movement speed
#         speed = math.sqrt(pow(self.center_x - self.prev_center_x, 2) +
#                           pow(self.center_y - self.prev_center_y, 2))
#         speed = int(speed * 100) / 100   # Round to 2 decimals

#         # Display speed in the frame
#         if (speed < self.THRESHOLD_A):
#             img = cv2.putText(img, "Motion: " + str(speed), (100, 50),
#                               cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
#         elif (speed < self.THRESHOLD_B):
#             img = cv2.putText(img, "Motion: " + str(speed), (100, 50),
#                               cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
#         else:
#             img = cv2.putText(img, "Motion: " + str(speed), (100, 50),
#                               cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

#         return av.VideoFrame.from_ndarray(img, format="bgr24")
