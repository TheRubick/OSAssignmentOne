import time
import zmq
import random
import sys
import cv2

def consumer():

        pushPort = str(sys.argv[1])
        #print(type(pushPort))
        context = zmq.Context()
        # recieve work
        consumer_receiver = context.socket(zmq.PULL)
        consumer_receiver.connect("tcp://127.0.0.1:5557")
        # send work
        consumer_sender = context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:%s" % pushPort)
        
        #consumer can push more than one frame
        while True:
                #print("tcp://127.0.0.1:%s" % pushPort)
                recvImag = consumer_receiver.recv_pyobj()
                #print(type(recvImag))
                #cv2.imshow('imagessss',recvImag)
                #cv2.waitKey()
                #otsu function
                ret2,outputImag = cv2.threshold(recvImag,0,255,cv2.THRESH_OTSU)
                
                consumer_sender.send_pyobj(outputImag)
                time.sleep(2)

consumer()