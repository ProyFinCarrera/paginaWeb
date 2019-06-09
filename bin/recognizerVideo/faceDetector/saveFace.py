# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# File: saveFace: File where the functions that save the image of face.
import os
from PIL import Image
import cv2
import numpy as np
import threading
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PATH_DIR = os.path.join(PATH_DIR, "..")
DIR_SAVE_FACE = os.path.join(PATH_DIR, "recognizer")
DIR_SAVE_FACE = os.path.join(os.path.join(
    DIR_SAVE_FACE, "att_faces"), "tmp_faces")
# print(DIR_SAVE_FACE)
MAX_F = 20
EXT = "jpg"
cont_img = 1

def save_face(face):
    global cont_img
    save = os.path.join(DIR_SAVE_FACE, "%d.%s" %
                        (cont_img, EXT))
    # im = Image.Image(face)
    # img = Image.fromarray(face[0], 'RGB')
    # im.save(save)
    #cv2.imwrite(save, face)
    t1 = threading.Thread(target=cv2.imwrite, args=(save, face,))
    t1.start()
    if(cont_img < MAX_F):
        cont_img += 1
    else:
        cont_img = 1