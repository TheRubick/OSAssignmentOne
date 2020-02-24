import time
import zmq
import cv2 
import pickle
import skimage.io as io
# Used as counter variable 
import numpy as np
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # checks whether frames were extracted 
    success = 1

    frameCount = 0
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        if(not success):
                break
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.jpg" % frameCount, image) 
        #img_message = cv2.imread('frame0.jpg',0)
        frameCount += 1

    return frameCount
# Calling the function 
frameCount = FrameCapture("test2.webm") 

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    #loop would be modified on the number of frames
    for i in range(0,frameCount):
        #should be modified to send image frame object
        #each file in python would take argument which is the number of port
        print('Producer : frame#'+str(i))
        img_message = cv2.imread('frame'+str(i)+'.jpg',0)
        msg_packet = {'frame#' : i , 'image' : img_message}
        zmq_socket.send(pickle.dumps(msg_packet))
        #print(img_message.dtype)
        
        #time.sleep(10)
        
producer()