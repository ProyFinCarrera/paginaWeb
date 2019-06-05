# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Main program that manages the operation of the system:
#            1. Check if it was already running.
#            2. Using the RecognizerVideo class
#            3. Create a subporocesos with the file "mainSaveFingers.py"
#            4. Save the camera image.
import subprocess
import threading
import cv2
import os
import time
from recognizerVideo import recognizerVideo
from recognizerVideo.saveSystem import saveSystem
from picamera.array import PiRGBArray
from picamera import PiCamera

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")

CMD = os.path.join(PATH_DIR, "mainSaveFingers.py ")

try:
    if os.path.isfile(PID_FILE):
        print("%s the file already exists" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32  # 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)
        det_video = recognizerVideo.RecognizerVideo(
            maxiR=20, maxiF=20, selRecon=1)
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image,
            # then initialize the timestamp bgr and occupied/unoccupied text
            image = frame.array
            # image = cv2.flip(image,1)
            image = cv2.flip(image, 1, 0)
            aux, name_img = det_video.video_img(image)
            if aux:
                print(name_img)
                #cmd = 'python mainSaveFingers.py ' + name_img
                cmd = ['python', 'mainSaveFingers.py', name_img]
                p = subprocess.Popen(
                    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if(p.poll()):
                    (stdout, stderr) = p.communicate()
                    print(stdout)
                    print(stderr)
                    print(p.poll())
                    print("Encendia lector de huellas")
                    det_video.set_cont_cero()
            # save video
            t1 = threading.Thread(target=saveSystem.save_img, args=(frame,))
            t1.start()
            # cv2.imshow("Frame", frame)
            if cv2.waitKey(10) == 27:
                break
except Exception as e:
    print('Exception message: ' + str(e))
