import numpy as np
import cv2
from digit import getTimeStamp,convertToString
import sys

if __name__ == "__main__":
    image = cv2.imread(sys.argv[1], 0)
    value = getTimeStamp(image)
    print(convertToString(value))

    
