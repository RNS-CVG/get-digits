# get-digits
Extracts digits from timestamped images.

## Project Structure
```
.
├── media
│   ├── left.mp4
│   ├── README.md
│   ├── right.mp4
│   └── test_data
│       ├── README.md
│       ├── test1.png
│       └── test.png
├── print_timestamps.py
├── README.md
├── requirements.txt
├── synchronize.py
├── test.png
└── timestamp.py
```

* Crop the pixels of the timestamp data from the right corner of the image. 
    To do so, read the image with [cv2.imread()](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html), crop appropriate area with array slicing. An image can be treated like a 2D matrix of RGB tuples of (R, G, B) values. An example can be found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html).
* The pytesseract API is then used to read the digits.
* Invoke the following to view timestamps.
  ```sh
   python print_timestamps.py
   # Format: left: <Left Timestamp> \t\t\tright: <Right Timestamp>
  ``` 
* The readings are extremely nosisy.
# TODO

* Create a script called *accuracy.py* which prints the correctly read values against the incorrect values.
* Use a linux pipeline to feed in data or any other tool you can use.
* The final file should print currently correctly detect:
  ```right / (right + wrong) ```
  and the same in % values.