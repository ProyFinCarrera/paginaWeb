#!/usr/bin/python2
import cv2, sys, numpy, os
import StringIO
from PIL import Image
img = None

while True:
	r = open('./../video/cam.jpg','rb').read()
	img_array = numpy.asarray(bytearray(r), dtype=numpy.uint8)
	flags = cv2.CV_LOAD_IMAGE_COLOR
	img = cv2.imdecode(img_array,0)
	cv2.imshow(img)