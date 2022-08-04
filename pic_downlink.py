import cv2
from PIL import Image
import os
#Camera settings
camera_id = 0
cap = cv2.VideoCapture(camera_id)
image_id = 0
image_path = "C:\\Users\\sasha\\Documents\\Flight Software"
width = 320 #As per SSDV standards, height must be a multiple of 16
height = 320 #As per SSDV standards, width must be a multiple of 16

#Various downlink settings
jpg_quality = 100
callsign = "ZEKE800" #Yea change that to your callsign
ssdv_path = "C:\\Users\\sasha\\Documents\\Flight Software\\ssdv"
binary_path = "C:\\Users\\sasha\\Documents\\Flight Software\\ssdv\\packets"
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
    im = Image.open(img)
    im = im.resize((width,height),Image.ANTIALIAS)
    im.save(img)
    return img

def convert2jpg(img):
    im = Image.open(img)
    im.save(img[0:len(img)-3]+"jpg",quality=jpg_quality) #Magic to convert to jpg :)
    #Removes the last three characters (png) and replaces with jpg

def convert2ssdv(img):
    print("Convert picture into SSDV [ID=" + str(image_id) + "]")
    os.system(ssdv_path+'/ssdv -e -t ' + str(jpg_quality) + ' -c ' + callsign + ' -i ' + str(image_id) + str(img)+ binary_path+'/image.ssdv')
    print("Done encoding SSDV [ID="+ str(image_id) +"]")
