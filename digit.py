import numpy as np
import cv2
import sys

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" #make sure to install tesseract 4.0.0
def getTimeStamp(image):
    x = 1024 + 30
    xh = 1024 +760
    date = crop(image, x,xh)

    cv2.imshow("test", date)
    cv2.waitKey(0)
    return date

def crop(image, lvalue, rvalue = None):
    if rvalue is None:
        return image[10:90, lvalue: ]
    return image[40:90, lvalue: rvalue]

def convertToString(image):
    blur = cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
    cv2.imshow("Blurred", blur)
    cv2.waitKey(0)
    text = pytesseract.image_to_string(blur)
    return text
