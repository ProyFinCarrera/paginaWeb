# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
# import subprocess
import sys
import threading
# import cv2
# import os
# from recognizerVideo.saveSystem import saveSystem
from myfirebase import myfirebase
from footprint import footprint

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
DIR_FACES = os.path.join(os.path.join(
    PATH_DIR, "recognizerVideo"), "recognizer")
DIR_FACES = os.path.join(os.path.join(DIR_FACES, "att_faces"), "tmp_faces")

print("Save footprint ....")
try:
    shutil.rmtree(DIR_IMAGES)
    
if os.path.isfile(PID_FILE):
        os.unlink(PID_FILE)
