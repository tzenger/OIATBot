from asyncio import create_subprocess_exec
from asyncio.windows_events import NULL
from multiprocessing.connection import wait
import pyautogui
import threading
import keyboard
import time
import random
import cv2
pyautogui.PAUSE = 0.000000001 # sets delay between pyautogui actions


xLower = 915
xUpper = 1615
yLower = 200
yUpper = 1224

def printPosition():
    print(pyautogui.position())


# click function - left-clicks mouse
def click():
    pyautogui.click()

# move function - moves cursor to location using coordinates
def move(x, y):
    pyautogui.moveTo(x, y)

def typ(char):
    pyautogui.typewrite(char)
    time.sleep(0.1)

def clickHere(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def randomPath(i):
    random.seed(random.seed(43))
    for i in range(i):
        move(random.randint(xLower, xUpper), random.randint(yLower, yUpper))
        pyautogui.click()
        print("help")

def newFind(screenshot):
    newFindImg = cv2.imread('./images/newfind.png', cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(newFindImg, screenshot, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if(max_val >= 0.99):
        clickHere(1280, 1350)


# Close (1280, 1290 or 1348)


