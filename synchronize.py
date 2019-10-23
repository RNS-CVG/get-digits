import timestamp as T
import numpy as np
import cv2
import sys

FACTOR = 0.2

def openVideo(path): #Return capture object of video if opened successfully.
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("Error opening file: {}".format(path.split('/')[-1]))
        return 0
    else:
        print("Successfully opened: {}".format(path.split('/')[-1]))
    return cap

def stereoContainer(video1, video2, show_video=True): #Takes in Capture object of two videos.
    while(video1.isOpened() and video2.isOpened()):
        _, frame1 = video1.read()
        _, frame2 = video2.read()
    
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        print("left: {} \t\t\tright: {}".format(T.getTimestamp(gray1), T.getTimestamp(gray2)))
        
        if(show_video):
            s_left = cv2.resize(gray1, None, fx=FACTOR, fy=FACTOR)
            s_right = cv2.resize(gray2, None, fx=FACTOR, fy=FACTOR)
            
            stereo = np.concatenate((s_left, s_right), axis=1)

            cv2.imshow("Stereo", stereo)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video1.release(), video2.release()
                break
        


if __name__ == "__main__":
    left = openVideo(sys.argv[1])
    right = openVideo(sys.argv[2])
    stereoContainer(left, right)