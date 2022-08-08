from asyncio.windows_events import NULL
import cv2
import imutils
from PIL import Image
import ult
import numpy as np

def compare(current, previous):

    # #get the images you want to compare.
    # original = cv2.imread("./images/bfr1.jpg")
    # new = cv2.imread("./images/aft1.jpg")
    # #resize the images to make them small in size. A bigger size image may take a significant time
    # #more computing power and time
    original = imutils.resize(previous, height = 500)
    new = imutils.resize(current, height = 500)


    #create a copy of original image so that we can store the
    #difference of 2 images in the same on
    diff = original.copy()
    
    cv2.absdiff(original, new, diff)

    #converting the difference into grayscale images
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Differences', gray)

    #increasing the size of differences after that we can capture them all
    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), None, iterations= i+ 1)


    #threshold the gray image to binary it. Anything pixel that has
    #value higher than 3 we are converting to white
    #(remember 0 is black and 255 is exact white)
    #the image is called binarised as any value lower than 3 will be 0 and
    # all of the values equal to and higher than 3 (NOW 100) will be 255
    (T, thresh) = cv2.threshold(dilated, 85, 255, cv2.THRESH_BINARY)

    # now we have to find contours in the binarized image
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)


    # egg area within 600 x 377 is 47 x 55

    buffer = 15 # pixel buffer for egg detection
    cntsValid = [] # initialize list of valid contours
    boxCoords = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c) # establishes coordinate and length values for bounding rectangle around contour c
        if ((w <= 40 + buffer) and (w >= 40 - buffer)) and ((h <= 50 + buffer) and (h >= 50 - buffer)): # if within egg dimensions with buffer
            cntsValid.append(c) # add to list of valid contours
            boxCoords.append((x + (w/2), y + (h/2))) # midpoints of boxes
        


    for c in cntsValid:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2) # draw valid contours to image as box

    return (new, boxCoords)

def ifGemFull(current, blue):
    bGemPos = 906
    rGemPos = 1055
    if blue:
        left = bGemPos - 5
        top = 82
        right = bGemPos + 5
        bottom = 83
    if not blue:
        left = rGemPos - 5
        top = 82
        right = rGemPos + 5
        bottom = 83
    crop = current[top:bottom, left:right]
    #cv2.imwrite("croppedred.jpg", crop)

    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    h, w, c = hsv.shape
    for i in range(h):
        for j in range(w):
            if hsv[i, j][0] <= 80 and hsv[i, j][0] >= 25:
                print('yellow')
                return 0 # yellow
            if hsv[i, j][0] == 0 and hsv[i, j][1] == 0 and hsv[i, j][2] >= 80:
                print('white')
                return 1 # white
    print("possible egg hunt")
    return False # neither yellow or white

def gemPopCloseButton(current):
    collectButtX = 1280
    collectButtY = 1393

    left = collectButtX - 3
    top = collectButtY
    right = collectButtX + 3
    bottom = collectButtY + 1
    crop = current[top:bottom, left:right]
    
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    h, w, c = hsv.shape
    for i in range(h):
        for j in range(w):
            if hsv[i, j][0] == 264:
                print('purple')
                return True # button exists
    return False # button does not exist