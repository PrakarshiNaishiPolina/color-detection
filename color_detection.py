import cv2 as cv
import numpy as np
from PIL import Image

def get_limits(color):
    # convert the BGR to HSV
    c=np.uint8([[color]])

    # cvtColor works for 2D arrays or 3D arrays

    hsvC=cv.cvtColor(c,cv.COLOR_BGR2HSV)

    # to detect colors in an image HSV is better

    # aftering converting into HSV color: [120,255,255]

    # calculate the HSV range

    # for hue we do +10,-10 to account for shades and variations and lightning conditions. ranges from 0 to 179.

    # saturation ranges from 0 to 255 but we take it from 100 (lower bound) it ensures that we ugnore very desaturated colors which look grayish or white. 255 (upper bound) captures the most intense version of the color.

    # value ranges from 0 to 255 but we take it from 100 to ensure very dark shaes (nearly black) are ignored, as they might not be visually identifiable. 255 (upper bound) captures the brightest possible appearances of the color.


    lower_limit1 = np.array([hsvC[0][0][0]-10,100,100],dtype= np.uint8)
    upper_limit1=np.array([hsvC[0][0][0]+10,255,255],dtype=np.uint8)

    lower_limit2 = np.array([hsvC[0][0][0] - 10 + 180, 100, 100], dtype=np.uint8)
    upper_limit2 = np.array([180, 255, 255], dtype=np.uint8)


    return (lower_limit1, upper_limit1), (lower_limit2, upper_limit2)



 



# Define the target color in BGR format (blue)

blue= [255,0,0] # BGR is OpenCV's default color format

# Open the default webcam

cap=cv.VideoCapture(0)

# Check if the webcam is opened successfully

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # read a frame from the webcam

    ret,frame=cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # convert the frame from BGR to HSV color space

    # HSV is better for Color Detection.


    hsvimage=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # get the range limits for the color blue

    (lower_limit1,upper_limit1), (lower_limit2,upper_limit2) = get_limits(color=blue)


    #  we need a way to identify only the pixels that match the target color.

    # the mask isolates those pixels by turning:

    # pixels matching the color -> white (255)

    # all other pixels -> black (0)

    # mask makes it easy to highlight the parts of the image where the target color exists.


    # create mask1


    mask1=cv.inRange(hsvimage,lower_limit1,upper_limit1)

    # create mask2
    mask2= cv.inRange(hsvimage,lower_limit2,upper_limit2)

    # combine the 2 masks

    mask =cv.bitwise_or(mask1,mask2)

    #convert the mask to a PIL image to calc the bounding box

    mask_=Image.fromarray(mask) # create a image from an array

    # getbbox() is a function from PIL Image that returns the smallest rectangle enclosing all non-zero(white) pixels in the image.
    bbox = mask_.getbbox()

    # if bounding box exists then,draw it on the original frame

    if bbox is not None:
        x1,y1,x2,y2 =bbox
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)

    
    # display the frame with detected blue areas

    cv.imshow('Detected Color',frame)

    # break the loop when 'd' is pressed
    if cv.waitKey(1) & 0xFF == ord('d'):
        break


# Release the webcam and close all OpenCV windows
cap.release()
cv.destroyAllWindows()


