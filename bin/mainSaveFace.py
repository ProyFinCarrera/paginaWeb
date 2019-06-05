# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# MainSaveFace: Program that does the following:
#               1. Check if it was already running.
#               2. Mostrar imágenes.
#               3. Detect if there is a face in the image.
#               4. Save images and faces.
import threading
import cv2
import os
from recognizerVideo.faceDetector import faceDetector
from recognizerVideo.saveSystem import saveSystem

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")


try:
    if os.path.isfile(PID_FILE):
        print("%s the file exist" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        det_face = faceDetector.FaceDetector()
        # capture frames from the camera
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            rval, frame = cap.read()
            if rval:
                frame = cv2.flip(frame, 1, 0)
                rt, face, (x, y) = det_face.detect(frame)
                if rt:
                    # save face
                    t1 = threading.Thread(
                        target=saveSystem.save_face, args=(face,))
                    t1.start()
            # save video
            t2 = threading.Thread(target=saveSystem.save_img, args=(frame,))
            t2.start()
            # show frame
            # cv2.imshow("Frame", frame)
            if cv2.waitKey(10) == 27:
                break
        cap.release()
except Exception as e:
    print('Exception message: ' + str(e))
