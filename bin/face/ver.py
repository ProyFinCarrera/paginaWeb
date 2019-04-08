#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Class to do face verification with opencv.
import os

import cv2
import StringIO
import numpy
from PIL import Image
import PIL


path = os.path.abspath('./../../public/video/cam.jpg')
pathv = os.path.abspath('./../../public/video/buffer')

img = None
cont = 0
while cont < 10:
    try:
        with open(path, 'rb') as img_bin:
            buff = StringIO.StringIO()
            buff.write(img_bin.read())
            buff.seek(0)
            temp_img = numpy.array(PIL.Image.open(buff), dtype=numpy.uint8)
            img = cv2.cvtColor(temp_img, cv2.COLOR_RGB2BGR)

        if img is not None:
            print("dentroooo")
            cv2.imshow("uff", img)
            cont += 1
            cv2.imwrite('%s/%s.jpg' % (pathv, cont), img)
            # cv2.waitKey(0)
            cv2.destroyAllWindows()
            
    except Exception as e:
        print("fuerra")
