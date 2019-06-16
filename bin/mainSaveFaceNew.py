# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# MainSaveFaceNew: Program that does the following:
#               1. Check if it was already running.
#               2. Mostrar imágenes.
#               3. Detect if there is a face in the image.
#               4. Save images and faces.
import threading
import cv2
import os
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from recognizerVideo.faceDetector import faceDetector
from recognizerVideo.saveSystem import saveSystem

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")

try:
    if os.path.isfile(PID_FILE):
        print("%s the file exist" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.hflip = True
        camera.framerate = 32 # 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)
        det_face = faceDetector.FaceDetector(save_face=True)
        
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image,
            # then initialize the timestamp bgr and occupied/unoccupied text
            image = frame.array
            det_face.detect(image)
            # save video
            t2 = threading.Thread(target=saveSystem.save_img, args=(image,))
            t2.start()
            #saveSystem.save_img(image)
            # show the frame
            cv2.imshow("Frame", image)
            rawCapture.truncate(0)
            if cv2.waitKey(10) == 27:
                break
            # clear the stream in preparation for the next frame
        cv2.destroyAllWindows()
except Exception as e:
    print('Exception message: ' + str(e))