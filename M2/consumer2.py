import time
import zmq
import random
import numpy as np
import sys
import cv2
from skimage.measure import find_contours
import skimage.io as io
from skimage.color import rgb2gray

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

        #pullPort = str(sys.argv[1])
        context = zmq.Context()
        consumer_sender = context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:5558")

        ################# just for test ###################3
        img =io.imread("test.jpg")
        grayImg=rgb2gray(img)
        grayImg[grayImg>=0.5]=1
        grayImg[grayImg<0.5]=0
        ####################################################
        
        bounding_boxes = contouring(grayImg)

        while True:
                l = ["ss", "ds", "fs"]
                consumer_sender.send_pyobj(bounding_boxes)
                time.sleep(2)




consumer2()