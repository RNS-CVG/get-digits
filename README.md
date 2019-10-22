# get-digits
Extracts digits from timestamped images.

## Project Structure
```
./
├── media
│   ├── left.mp4
│   ├── right.mp4
│   └── test_data
│       ├── test1.png
│       └── test.png
├── README.md
├── requirements.txt
├── synchronize.py
└── timestamp.py
```

### Requirements
```bash
pip install -r requirements.py # in the project directory.
```
## Abstract
* Crop the pixels of the timestamp data from the right corner of the image. 
    To do so, read the image with [cv2.imread()](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html), crop appropriate area with array slicing. An image can be treated like a 2D matrix of RGB tuples of (R, G, B) values. An example can be found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html).
* A function is usedto access the digits hereafter with variables for each digit.
  ```
  def getTimestamp(image):
    .
    .
    return timestamp #string
   ```
* When .getTimeStamp() is invoked on an Image, it returns the content using [Tesseract](https://github.com/tesseract-ocr/tesseract). 

### WIP (Next steps)

