import time
import zmq
import random
import sys
import cv2
from skimage.measure import find_contours

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


def consumer2():

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
                
                recvImag = consumer_receiver.recv_pyobj()
                bounding_boxes = contouring(recvImag)
                
                consumer_sender.send_pyobj(bounding_boxes)
                #consumer_sender.send_pyobj("whaaaaaaaaaat")
                time.sleep(2)

consumer()