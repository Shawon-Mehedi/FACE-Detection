# FACE-Detection
Face Detection Projects with OpenCV <br>
This repository contains two simple yet powerful AI face detection projects using Python and OpenCV.

📸 1. Face Detection in Static Images <br>
This script loads a static image (Human.jpg), converts it to grayscale, and uses OpenCV’s pretrained Haar Cascade classifier to detect human faces. <br>
It then draws colorful rectangles around each detected face and displays the result in a window.

Main features: <br>
✅ Uses haarcascade_frontalface_default.xml <br>
✅ Random-color rectangles for each detected face <br>
✅ Simple image display with OpenCV’s imshow() 

🎥 2. Real-time Face Detection from Webcam or Video <br>
This script activates your webcam (or can be modified to load a video file) and performs real-time face detection on each video frame. <br>
It draws bounding boxes around faces in live video and displays the processed frames continuously until you press Q (q or Q key) to stop.

Main features: <br> 
✅ Works with webcam or pre-recorded videos <br>
✅ Live face detection on video frames <br>
✅ Random-color rectangles for fun visual feedback <br>
✅ Graceful shutdown when key pressed

Author - Mehedi Hasan Shawon <br>
Email : shawonmehedi.c@gmail.com
