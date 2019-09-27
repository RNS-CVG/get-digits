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
      

       day=crop[y:y+h,30:110]
       cv2.imshow('img1',day) 
       
       month=crop[y:y+h,135:210]
       cv2.imshow('img2',month)
       
       year=crop[y:y+h,235:365]
       cv2.imshow('img3',year)
       
       hours=crop[y:y+h,380:460]
       cv2.imshow('img4',hours)
       
       mins=crop[y:y+h,480:560]
       cv2.imshow('img5',mins)
       
       secs=crop[y:y+h,580:660]
       cv2.imshow('img6',secs)
       
       ampm=crop[y:y+h,680:760]
       cv2.imshow('img7',ampm)
       
       cv2.waitKey(0)
