import time
import cv2 as cv
from PIL import Image

import capture
import compare
import ult


counter = 0
limit = 40
isGemFullReturn = 0
prevReturn = 0

time.sleep(1)
screenshot = capture.windowCapture()

while True:

    screenshotOld = screenshot
    screenshot = capture.windowCapture()
    
    frame = compare.compare(screenshot, screenshotOld)[0]
    coordList = compare.compare(screenshot, screenshotOld)[1]
    cv.imshow('Eggs', frame)
    cv.waitKey(1)
    # Click Box
    for i in coordList:
        ult.clickHere(i[0] * (1440/500), i[1] * (1440/500))

    ult.randomPath(20)
    if counter >= limit:
        ult.closeNewEgg()
        counter = 0
    else:
        counter += 1
    
    # # Gem Pop Algorithm
    # prevReturn = isGemFullReturn
    # isGemFullReturn = compare.ifGemFull(screenshot, True)
    # if prevReturn == 2 and isGemFullReturn == 1: # prevent unwanted gem pop after egg hunt
    #     time.sleep(0.1)
    #     prevReturn = 0
    #     isGemFullReturn = compare.ifGemFull(screenshot, True)
    # elif isGemFullReturn == 1 and prevReturn != 2:
    #     print('starting gem pop')
    #     time.sleep(1)
    #     ult.menuButton()
    #     ult.gemPopButton()
    #     ult.gemPopStart()
    #     time.sleep(2) # arbitrary value
    #     ult.closeGemPopMenu()
    #     while not compare.gemPopCloseButton(screenshot):
    #         screenshot = capture.windowCapture()
    #         time.sleep(0.1)
    #     ult.closeGemPop()
    #     time.sleep(2) # arbitrary value
    #     ult.closeGemPopMenu() # in case of accidental click
    #     time.sleep(0.5)
    #     isGemFullReturn = 0
    #     prevReturn = 0
    # if isGemFullReturn == 2:
    #         ult.eggHuntPath()

    # Tap Blasts Algorithm
    start_time = time.time()
    secondsLimit = 30

    prevReturn = isGemFullReturn
    isGemFullReturn = compare.ifGemFull(screenshot, True)
    if isGemFullReturn == 1 and prevReturn == 1:
        print('starting tap blasts')
        cv.destroyAllWindows()
        time.sleep(1)
        ult.menuButton()
        ult.tapBlastsButton()
        ult.tapBlasts10Gems()
        ult.tapBlastsWild()
        time.sleep(2) # arbitrary value
        while (not compare.tapBlastsCloseButton(screenshot)) or (not time.time() - start_time > secondsLimit):
            print(time.time() - start_time)
            screenshotOld = screenshot
            screenshot = capture.windowCapture()
    
            frame = compare.compare(screenshot, screenshotOld)[0]
            coordList = compare.compare(screenshot, screenshotOld)[1]
            cv.imshow('Eggs', frame)
            cv.waitKey(1)
            # Click Box
            for i in coordList:
                ult.clickHere(i[0] * (1440/500), i[1] * (1440/500))
        ult.closeTapBlastsButton()
        cv.destroyAllWindows()


        


    # if frame is read correctly ret is True
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# When everything done, release the capture
cv.destroyAllWindows()