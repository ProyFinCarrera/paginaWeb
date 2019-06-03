# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa principara que lleva al gestion de
# funcionemineto del siemta reconocerdor:
#           1. Clase RecognonizerVideo reconozcera a una persona en una imagen,si la reconoce 20 veces seguir
#                la persona quires registarse.
#            2. llaamara al reconocerdor de huella para ver si estas en el siemta.path
#            3. se bajara lso datos del firebase.path
#            4. Se comparara y verificara los datos y si concuerda todo se registar en firebase la entrada.
import subprocess
import threading
import sys
import cv2
import os
import signal
from recognizerVideo import recognizerVideo
from myfirebase import myfirebase
from footprint import footprint

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = PATH_DIR + "/tmp/mydaemon.PID"
pid = 1

try:
    if os.path.isfile(PID_FILE):
        print("%s el archivo ya existe, cerrando el proceso" % PID_FILE)
        pid = open(PID_FILE, "w").read()
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        cap = cv2.VideoCapture(0)
        det_video = recognizerVideo.RecognizerVideo(
             maxiR=20, maxiF=20, selRecon=1,rec_op=False)
  
        while cap.isOpened():
            rval, frame = cap.read()
            if rval:
                frame = cv2.flip(frame, 1, 0)
                aux, name_img = det_video.video_img(frame)
            # cv2.imshow("face", frame)

            if cv2.waitKey(10) == 27:
                break
        cap.release()

except Exception as e:
    print('Exception message: ' + str(e))
finally:
    if(pid!=1):
        pirnt("Me carge el proceso:"+str(pid))
        os.kill(pid, signal.SIGTERM)
    
    os.unlink(PID_FILE)