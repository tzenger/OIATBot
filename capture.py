from asyncio.windows_events import NULL
import numpy as np
import cv2 as cv
import pyautogui
import time
from PIL import ImageGrab
import compare
import ult
from win32 import win32gui
import win32ui
import win32con
pyautogui.PAUSE = 0.000000001 # sets delay between pyautogui actions

def windowCapture():
    w = 2560 # set this
    h = 1440 # set this

    #hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img
