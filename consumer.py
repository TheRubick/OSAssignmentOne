import time
import zmq
import random
import sys
import cv2
import pickle
import numpy as np
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
                recvPacket = pickle.loads(consumer_receiver.recv())
                #print(type(recvPacket['image']))
                #print(recvPacket['image'])
                #otsu function
                ret2,outputImag = cv2.threshold(recvPacket['image'],0,255,cv2.THRESH_OTSU) # image , threshold value , assign max value for values >= threshold
                #print(outputImag)
                #print(outputImag.dtype)
                print("consumer , frame#"+str(recvPacket['frame#']))
                #cv2.imshow('imagessss',outputImag)
                #cv2.waitKey()
                send_Packet = {'frame#' : recvPacket['frame#'] , 'image' : outputImag}
                consumer_sender.send(pickle.dumps(send_Packet))
                #time.sleep(2)

consumer()