# FACE-Detection
Face Detection Projects with OpenCV
This repository contains two simple yet powerful AI face detection projects using Python and OpenCV.

📸 1. Face Detection in Static Images
This script loads a static image (Human.jpg), converts it to grayscale, and uses OpenCV’s pretrained Haar Cascade classifier to detect human faces.
It then draws colorful rectangles around each detected face and displays the result in a window.

Main features:
✅ Uses haarcascade_frontalface_default.xml
✅ Random-color rectangles for each detected face
✅ Simple image display with OpenCV’s imshow()

🎥 2. Real-time Face Detection from Webcam or Video
This script activates your webcam (or can be modified to load a video file) and performs real-time face detection on each video frame.
It draws bounding boxes around faces in live video and displays the processed frames continuously until you press Q (q or Q key) to stop.

Main features:
✅ Works with webcam or pre-recorded videos
✅ Live face detection on video frames
✅ Random-color rectangles for fun visual feedback
✅ Graceful shutdown when key pressed
