# get-digits
Extracts digits from timestamped images.

## Project Structure
```
-detector.py
-test.png
-main.py
```

* Crop the pixels of the timestamp data from the right corner of the image. 
    To do so, read the image with [cv2.imread()](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html), crop appropriate area with array slicing. An image can be treated like a 2D matrix of RGB tuples of (R, G, B) values. An example can be found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html).
* Create an object oriented design to access the digits hereafter with variables for each digit.
  ```
  class Timestamp(image):
     def __init__(self, image):
        #Open image in a variable with self./<variable>
     def getTime(self):
        #create variables like below to store the 
        #bounding boxes of each of the appropriate areas. 
        #self.date
        #self.time
        . . .
   ```
* When .getTime() is invoked on a Timestamp object which is already initialised to a frame, it should return the appropriate bounding boxes of the content. 
