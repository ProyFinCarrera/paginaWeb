# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa cierra el siestema.
import os
import signal
import shutil
import time

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
DIR_FACES = os.path.join(os.path.join(
    PATH_DIR, "recognizerVideo"), "recognizer")
DIR_FACES = os.path.join(os.path.join(DIR_FACES, "att_faces"), "tmp_faces")
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")
PID_FILE2 = os.path.join(os.path.join(PATH_DIR, "tmp"), "pass.PID")
PID_FILE3 = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")
PATH_VIDEO = os.path.join(PATH_DIR, "..")
PATH_VIDEO = os.path.join(PATH_VIDEO, "public")
PATH_VIDEO = os.path.join(PATH_VIDEO, "video")
DIR_IMAGES = os.path.join(PATH_VIDEO, "images")
PATH_IMG = os.path.join(PATH_VIDEO, "img_begin")
PATH_IMG = os.path.join(PATH_IMG, "video.jpg")
PATH_VIDEO = os.path.join(PATH_VIDEO, "video.jpg")
pid = 1

try:
    if os.path.isfile(PID_FILE):
        pid = open(PID_FILE, "r").read()
        os.kill(int(pid), signal.SIGTERM)
        time.sleep(1)
        os.unlink(PID_FILE)
    shutil.rmtree(DIR_IMAGES)
    os.makedirs(DIR_IMAGES)
    shutil.rmtree(DIR_FACES)
    os.makedirs(DIR_FACES)
    shutil.copy(PATH_IMG, PATH_VIDEO)       
    if os.path.isfile(PID_FILE2):
        os.unlink(PID_FILE2)
    if os.path.isfile(PID_FILE3):
        os.unlink(PID_FILE3)
    print("Llego al final")
except Exception as e:
    raise e
