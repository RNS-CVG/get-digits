import cv2
import pytesseract


def getTimestamp(image):
    image = image[0:100, 1000:1800]
    ret, thresh = cv2.threshold(image, 10, 255, cv2.THRESH_OTSU)
    timestamp = pytesseract.image_to_string(thresh)
    # print(timestamp)
    return timestamp


if __name__ == '__main__':
    image = cv2.imread("test.png", 0)
    print(getTimestamp(image))
