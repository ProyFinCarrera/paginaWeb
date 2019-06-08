# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
# import subprocess
import sys
import threading
import shutil
# import cv2
import os
# from recognizerVideo.saveSystem import saveSystem
from myfirebase import myfirebase
from footprint import footprint

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
DIR_FACES = os.path.join(os.path.join(
    PATH_DIR, "recognizerVideo"), "recognizer")
DIR_FACES = os.path.join(os.path.join(DIR_FACES, "att_faces"), "orl_faces")


    
print("Delleted All ...")

def main():
    try:
        # nameFile = sys.argv[1]
        # nameFile = "nuevo_yo"
        deleted_footprint(nameFile)
        deleted_img(nameFile)
    except Exception as e:
        raise e

def deleted_footprint(nameFile):
    aux = footprint.Footprint();
    db = myfirebase.MyFirebase()
    json_vector = aux.vect_charasteristics_doc(nameFile)
    aux.del_footprint(json_vector)
    
def deleted_img(nameFile):
    if(len(nameFile) > 0):
        DIR_FACE = os.path.join(DIR_FACES, nameFile)
        shutil.rmtree(DIR_FACE)

if __name__ == "__main__":
    main()