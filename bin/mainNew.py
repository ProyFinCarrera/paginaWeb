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
from footprint import footprint
from recognizerVideo import recognizerVideo
from recognizerVideo.saveSystem import saveSystem
from picamera.array import PiRGBArray
from picamera import PiCamera

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")
PID_PROCESS = os.path.join(os.path.join(PATH_DIR, "tmp"), "process.PID")
PID_FILE2 = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")
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
        camera.framerate = 30  # 15 32
        camera.hflip = True
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)
        det_video = recognizerVideo.RecognizerVideo(
            maxiR=3, selRecon=1)
        flag = False
        #time.sleep(0.1)
        # aux_F = footprint.Footprint(timer_power = 15 );
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image,
            # then initialize the timestamp bgr and occupied/unoccupied text
            image = frame.array
            #aux, name_img = det_video.video_img(image)
            rt_v, name_img = det_video.only_video_img(image)
            #time.sleep(0.1)
            #cv2.imshow("Frame",image )
            if rt_v == True:
                aux  = os.path.join(PATH_DIR ,'mainVerifyFootprint.py')
                cmd = ['python', aux , name_img]
                p = subprocess.Popen(cmd)
                open(PID_PROCESS, "w").write(str(p.pid))
                flag = True
                print("Activo suproceso")
                det_video.cancel_cont()
            if flag:
                if os.path.isfile(PID_PROCESS)== False:
                    flag = False
                    det_video.active_cont()
                    det_video.set_cont_cero()
            
            # save video
            t1 = threading.Thread(target=saveSystem.save_img, args=(image,))
            t1.start()
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
            if cv2.waitKey(10) == 27:
                break
         
        cv2.destroyAllWindows()
except Exception as e:
    print('Exception message: ' + str(e))
         
