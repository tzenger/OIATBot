from asyncio import create_subprocess_exec
from asyncio.windows_events import NULL
from multiprocessing.connection import wait
from tkinter import W
import pyautogui
import threading
import keyboard
import time
import random
import cv2
import compare
pyautogui.PAUSE = 0.000000001 # sets delay between pyautogui actions


xLower = 915
xUpper = 1615
yLower = 180
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

def closeNewEgg():
    clickHere(1280, 1350)

def menuButton():
    clickHere(1635, 1389)
    time.sleep(0.5)

def gemPopButton():
    clickHere(1635, 1043)
    time.sleep(0.5)

def gemPopStart():
    clickHere(1278, 787)
    time.sleep(0.5)

def closeGemPop():
    clickHere(1280, 1393)
    time.sleep(0.5)

def closeGemPopMenu():
    clickHere(1280, 908)
    time.sleep(0.5)

def randomPath(i):
    random.seed(random.seed(43))
    for i in range(i):
        move(random.randint(xLower, xUpper), random.randint(yLower, yUpper))
        pyautogui.click()

#  def eggHuntPath(curr, past):
#     w = 1674 - 877
#     h = 1280 - 170
#     xOffset = 877
#     yOffset = 170
#     stepX = 16
#     stepY = 30
#     alternate = False
    
#     huntEnd = False
#     for i in range(stepY):
#         compare.compare(curr, past)
#         if compare.ifGemFull(curr, True) == 0:
#             time.sleep(0.05)
#             print("WE OUT AND DONE BBABYA")
#             break
#         for j in range(stepX):
#             if alternate:
#                 clickHere(xOffset + j * (w/stepX), yOffset + i * (h / stepY))
#                 time.sleep(0.001)
#                 alternate = True
                
#             else:
#                clickHere(xOffset + (j + 1) * (w/stepX), yOffset + i * (h / stepY))
#                time.sleep(0.001)
#                alternate = False
            
#     print("egg hunt has snaked")



# size x - 877 -> 1674
# size y - 170 -> 1280


