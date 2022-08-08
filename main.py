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
print(compare.ifGemFull(screenshot, True))


while False:

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
        ult.clickHere(1280, 1350)
        counter = 0
    else:
        counter += 1

# if frame is read correctly ret is True
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# When everything done, release the capture
cv.destroyAllWindows()