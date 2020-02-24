import time
import zmq
import random
import sys
import cv2
import pickle
import numpy as np
def collector():

    pullPort = str(sys.argv[1])
    pushPort = str(sys.argv[2]) # sara
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
    collector_sender = context.socket(zmq.PUSH) # sara
    collector_sender.bind("tcp://127.0.0.1:%s" % pushPort) # sara
    
    #collector_sender.bind("tcp://192.168.43.221:%s" % pushPort) # sara
    
    while True:
        #print("collector is accessed")
        recv_Packet = pickle.loads(collector_receiver.recv())
        print(pullPort)
        print("collector frame # = "+str(recv_Packet['frame#']))
        #cv2.imshow('imageColl',recv_Packet['image'])
        #cv2.waitKey()
        #collector_sender.send_json(result)
        #collector_sender.send_json(packet_dict)
        collector_sender.send(pickle.dumps(recv_Packet))

collector()