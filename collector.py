import time
import zmq
import random
import sys
import cv2
def collector():

    pullPort = str(sys.argv[1])
    #print(type(pullPort))
    #print(pullPort)
    context = zmq.Context()
    # recieve work
    collector_receiver = context.socket(zmq.PULL)
    collector_receiver.bind("tcp://127.0.0.1:%s" % pullPort)
    # send work
    #collector_sender = context.socket(zmq.PUSH)
    # ip address and port of this socket would be assigned on connecting the 2 machines
    #collector_sender.connect("tcp://127.0.0.1:9888") 
    
    while True:
        #print("collector is accessed")
        recvImag = collector_receiver.recv_pyobj()
        print(pullPort)
        print(type(recvImag))
        #cv2.imshow('imageColl',recvImag)
        #cv2.waitKey()
        #collector_sender.send_json(result)

collector()