import time
import zmq
import random
import sys
import cv2
from skimage.measure import find_contours
import numpy as np
import pickle

def contouring(img):
        contours = find_contours(img,0.8)
        bounding_boxes = []
        for contour in contours:
                contour=contour.astype(int)
                Xmin = np.min(contour[:,0])
                Xmax = np.max(contour[:,0])
                Ymin = np.min(contour[:,1])
                Ymax = np.max(contour[:,1])
                bounding_boxes.append([Xmin, Xmax, Ymin, Ymax])
        return bounding_boxes


def consumer():

        #pullPort = str(sys.argv[2])
        pullPort = str(sys.argv[1])  #will use this
        context = zmq.Context()
        # recieve work
        consumer_receiver = context.socket(zmq.PULL)
        consumer_receiver.connect("tcp://127.0.0.1:%s" % pullPort)
        
        # send work
        consumer_sender = context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:5558")
        
        
        while True:
                
                recv_packet = pickle.loads(consumer_receiver.recv())
                print("consumer2 has recieved a value")
                bounding_boxes = contouring(recv_packet['image'])
                send_packet = {'frame#' : recv_packet['frame#'] , 'bboxes' : bounding_boxes}
                consumer_sender.send(pickle.dumps(send_packet))
                print("consumer2 has sent a value with frame#"+str(send_packet['frame#']))
                #consumer_sender.send_pyobj("whaaaaaaaaaat")
                #time.sleep(2)

consumer()