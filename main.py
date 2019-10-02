import numpy
import cv2
from detector import Timestamp as T
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread('test.png',0)
x=T(image)
x.getTime()

#Using Gaussian Blur to smoothen the images
day = cv2.imread('day.png', cv2.IMREAD_UNCHANGED)
blurDay= cv2.GaussianBlur(day, (3,3), cv2.BORDER_DEFAULT)
dayText=pytesseract.image_to_string(blurDay)


mins = cv2.imread('mins.png', cv2.IMREAD_UNCHANGED)
blurMins= cv2.GaussianBlur(mins, (5,5), cv2.BORDER_DEFAULT)
minsText=pytesseract.image_to_string(blurMins)


month = cv2.imread('month.png', cv2.IMREAD_UNCHANGED)
blurMonth= cv2.GaussianBlur(month, (7,7), cv2.BORDER_DEFAULT)
monthText=pytesseract.image_to_string(blurMonth)



secs = cv2.imread('secs.png', cv2.IMREAD_UNCHANGED)
blurSecs = cv2.GaussianBlur(secs, (5,5), cv2.BORDER_DEFAULT)
secsText=pytesseract.image_to_string(blurSecs)


year = cv2.imread('year.png', cv2.IMREAD_UNCHANGED)
blurYear = cv2.GaussianBlur(year, (5,5), cv2.BORDER_DEFAULT)
yearText=pytesseract.image_to_string(blurYear)

print(dayText)
print(monthText)
print(yearText)

print(minsText)
print(secsText)


