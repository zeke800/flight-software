import cv2
import imutils
import time

#Camera settings
camera_id = 0
cap = cv2.VideoCapture(camera_id)
image_id = 0
image_path = ""
ret, frame = cap.read()

def take_pic():
    grabbed, frame = cap.read()
    image = image_path+"/"+image_id+".jpg"
    cv2.imwrite(image, frame)
    cap.release()
    return image