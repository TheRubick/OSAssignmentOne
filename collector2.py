import time
import zmq
import random
import sys
import cv2
def collector():

    #pullPort = str(sys.argv[1])
    #print(type(pullPort))
    #print(pullPort)
    context = zmq.Context()
    # recieve work
    collector_receiver = context.socket(zmq.PULL)
    collector_receiver.bind("tcp://127.0.0.1:5558")
    # send work
    #collector_sender = context.socket(zmq.PUSH)
    # ip address and port of this socket would be assigned on connecting the 2 machines
    #collector_sender.connect("tcp://127.0.0.1:9888") 

    
    while True:
        file1 = open("file.txt","a")
        recvImag = collector_receiver.recv_pyobj()

        #file1.write(recvImag)
        file1.writelines(recvImag)
        file1.close()  # will not excute

collector()