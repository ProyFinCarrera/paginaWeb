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
from recognizerVideo import recognizerVideo
from recognizerVideo.saveSystem import saveSystem

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")
PID_FILE2 = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")

try:
    if os.path.isfile(PID_FILE):
        print("%s the file already exists" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        cap = cv2.VideoCapture(0)
        det_video = recognizerVideo.RecognizerVideo(
            maxiR=20, selRecon=1)
        while cap.isOpened():
            rval, frame = cap.read()
            if rval:
                frame = cv2.flip(frame, 1, 0)
                aux, name_img = det_video.video_img(frame)
                if aux:
                    #name_img = "sdfadfsd" #este fuera
                    # print(name_img)
                    #cmd = 'python mainSaveFingers.py ' + name_img
                    aux  = os.path.join(PATH_DIR ,'mainVerifyFootprint.py')
                    #aux = 'mainSaveFingers.py'
                    print(aux)
                    cmd = ['python', aux , name_img]
                    p = subprocess.Popen(cmd)

            if os.path.isfile(PID_FILE2):
                os.unlink(PID_FILE2)
                det_video.set_cont_cero()
            # save video
            t1 = threading.Thread(target=saveSystem.save_img, args=(frame,))
            t1.start()
            #cv2.imshow("Frame", frame)
            if cv2.waitKey(10) == 27:
                break
        cap.release()
except Exception as e:
    print('Exception message: ' + str(e))
