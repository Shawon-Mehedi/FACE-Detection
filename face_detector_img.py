import cv2
from random import randrange

# load some pretrained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('D:\Python Codes\AI_Project\haarcascade_frontalface_default.xml')

# To capture the img
img  = cv2.imread('D:\Python Codes\AI_Project\Human.jpg') 


grayscaled_img=cv2.cvtColor( img,cv2.COLOR_BGR2GRAY)
# detect face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)


# draw rectangles around the face
for (x,y,w,h) in face_coordinates:
 #(x,y,w,h) = face_coordinates[0]
 cv2.rectangle(img,(x,y),(x+w, y+h), (randrange(256),randrange(256),randrange(256)),5)

# display the image with the faces
cv2.imshow('Human Face Detection', img)
cv2.waitKey()
print("code complete")   
