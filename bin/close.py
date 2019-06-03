# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa cierra el siestema.
import os
import signal
import shutil



PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID_FILE = PATH_DIR + "/tmp/mydaemon.PID"

PATH_VIDEO = os.path.join( PATH_DIR, "..")
PATH_VIDEO = os.path.join(PATH_VIDEO , "public")
PATH_VIDEO = os.path.join(PATH_VIDEO , "video")
DIR_IMAGES = os.path.join(PATH_VIDEO , "images")
PATH_IMG =  os.path.join(PATH_VIDEO , "img_begin")
PATH_IMG =os.path.join(PATH_IMG ,"video.jpg")
PATH_VIDEO = os.path.join(PATH_VIDEO ,"video.jpg")


pid = 1

try:
    if os.path.isfile(PID_FILE):
        # print("%s el archivo ya existe, cerrando el proceso" % PID_FILE)
        pid = open(PID_FILE, "r").read()
        os.kill(int(pid), signal.SIGTERM)
        os.unlink(PID_FILE)
        shutil.rmtree(DIR_IMAGES)
        os.makedirs(DIR_IMAGES)
        shutil.copy(PATH_IMG,PATH_VIDEO)
except Exception as e:
    raise e
