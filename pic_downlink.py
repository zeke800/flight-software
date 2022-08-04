import cv2
from PIL import Image
#Camera settings
camera_id = 0
cap = cv2.VideoCapture(camera_id)
image_id = 0
image_path = "C:\\Users\\sasha\\Documents\\Flight Software"
width = 320 #As per SSDV standards, height must be a multiple of 16
height = 320 #As per SSDV standards, width must be a multiple of 16

def take_pic():
    global image_id
    ret, frame = cap.read()
    grabbed, frame = cap.read()
    image = image_path+"/"+str(image_id)+".png"
    #Avoid saving jpgs until the very last process (ssdv encode) which requires
    #JPEG as a format
    cv2.imwrite(image, frame)
    image_id = image_id + 1
    return image
def release_camera():
    global cap
    cap.release()

def process_image(img):
    global im
    im = Image.open(img)
    im = im.resize((width,height),Image.ANTIALIAS)
    im.save(img)
