import numpy
import cv2
import win32com.client as comclt
import pyautogui


def draw_found_faces(detected, image, color: tuple):
    for (x, y, width, height) in detected:
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            color,
            thickness=2
        )


# Capturing the Video Stream
video_capture = cv2.VideoCapture(0)

# Creating the cascade objects
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    # Get image
    prv, image = video_capture.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected_face = face_cascade.detectMultiScale(gray)

    for (fx, fy, fw, fh) in detected_face:
        face_color = image[fy:fy + fh, fx:fx + fw]
        face_gray = gray[fy:fy + fh, fx:fx + fw]
        cv2.rectangle(image, (fx, fy), (fx+fw, fy+fh), (0, 0, 255), 2)

    detected_smile = smile_cascade.detectMultiScale(image, scaleFactor=2.2, minNeighbors=30)
    for (sx, sy, sw, sh) in detected_smile:
        cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (255, 0, 0), 5)
        pyautogui.press('space')
    cv2.imshow('Webcam Face Detection', image)
    # Display the updated frame as a video stream


    # Press the ESC key to exit the loop
    # 27 is the code for the ESC key
    if cv2.waitKey(1) == 27:
        break

# Releasing the webcam resource
video_capture.release()

# Destroy the window that was showing the video stream
cv2.destroyAllWindows()
