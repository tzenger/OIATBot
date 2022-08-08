import time
import cv2 as cv
from PIL import Image

import capture
import compare
import ult


counter = 0
limit = 1000

time.sleep(1)
screenshot = capture.windowCapture()

while True:

    screenshotOld = screenshot
    screenshot = capture.windowCapture()
    
    frame = compare.compare(screenshot, screenshotOld)[0]
    coordList = compare.compare(screenshot, screenshotOld)[1]
    cv.imshow('Eggs', frame)

    # Click Box
    for i in coordList:
        ult.clickHere(i[0] * (1440/500), i[1] * (1440/500))

    ult.randomPath(20)
    if counter >= limit:
        ult.closeNewEgg()
        counter = 0
    else:
        counter += 1

    compare.ifGemFull(screenshot, True)
    if compare.ifGemFull(screenshot, True) == 1:
        print('starting gem pop')
        time.sleep(3)
        ult.menuButton()
        ult.gemPopButton()
        ult.gemPopStart()
        time.sleep(5) # arbutrary time
        if compare.gemPopCloseButton(screenshot):
            ult.closeGemPop()
            time.sleep(3)


    # if frame is read correctly ret is True
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# When everything done, release the capture
cv.destroyAllWindows()