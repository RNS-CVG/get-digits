import numpy as np
import cv2
from detector import Timestamp as T

image = cv2.imread('test.png')
x=T(image)
x.getTime()
