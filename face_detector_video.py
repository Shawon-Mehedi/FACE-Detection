import cv2
from random import randrange

# load some pretrained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('D:\Python Codes\AI_Project\haarcascade_frontalface_default.xml')

# To capture the video from webcam
webcam=cv2.VideoCapture(0)
# webcam=cv2.VideoCapture("D:\Python Codes\AI_Project\Video.mp4")

while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()

    # must convert to grayscale
    grayscaled_img=cv2.cvtColor( frame,cv2.COLOR_BGR2GRAY)

    # detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangles around the face
    for (x,y,w,h) in face_coordinates:
       # (x,y,w,h) = face_coordinates[0]
       cv2.rectangle(frame,(x,y),(x+w, y+h), (randrange(256),randrange(256),randrange(256)),5)


    cv2.imshow('Hello', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break
    

webcam.release()
print("code complete") 