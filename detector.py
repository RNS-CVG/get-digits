import numpy as np
import cv2
class Timestamp:
   def __init__(self, image):
       self.image=image
   def getTime(self):
       y=0
       x=1024
       h=100
       w=2200

       crop = self.image[y:y+h, x:]
      

       day=crop[y:y+h,50:110]

       cv2.imwrite('day.png', day)
       
       month=crop[y:y+h,135:210]

       cv2.imwrite('month.png', month)

       year=crop[y:y+h,235:365]

       cv2.imwrite('year.png', year)

       hours=crop[y:y+h,390:445]

       cv2.imwrite('hours.png', hours)

       mins=crop[y:y+h,490:560]

       cv2.imwrite('mins.png', mins)

       secs=crop[y:y+h,590:660]

       cv2.imwrite('secs.png', secs)

       ampm=crop[y:y+h,680:760]

       cv2.imwrite('ampm.png', ampm)
       
       cv2.waitKey(0)

