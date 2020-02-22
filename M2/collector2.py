import time
import zmq
import random
import sys
import cv2
def collector():

    context = zmq.Context()
    collector_receiver = context.socket(zmq.PULL)
    collector_receiver.bind("tcp://127.0.0.1:5558")
    file1 = open("file.txt","a")
    while True:
        
        recvImag = collector_receiver.recv_pyobj()
        
        listToStr = ' '.join([str(elem) for elem in recvImag]) 
        file1.writelines(listToStr)
        print(type(listToStr))
        #file1.writelines(recvImag)
    file1.close()  # will not excute

collector()