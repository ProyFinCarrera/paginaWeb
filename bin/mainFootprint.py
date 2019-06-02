# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
# import subprocess
import sys
# import threading
# import cv2
# import os
# from recognizerVideo.saveSystem import saveSystem
from myfirebase import myfirebase
# from footprint import footprint

print("Save footprint ....")


def otro():
    try:
        print("fuera")
        # email = "yo@gmaklkljil.cosdmhhsd"
        email = sys.argv[1]
        print(email)
        # email = "yo@gmaklkljil.cosdmhhsd"
        db = myfirebase.MyFirebase()
        # aux = footprint.Footprint();
        # vec_aux = aux.save_footprint();
        vec_aux = "bbbbbb"
        db.upload_footprint(vec_aux, email)

    except Exception as e:
        print('Exception message: ' + str(e))
    finally:
        print("final")


def main():
    email = sys.argv[1]
    # print(email)
    db_dato = myfirebase.MyFirebase()
    # aux = footprint.Footprint();
    # vec_aux = aux.save_footprint();
    vec_aux = "fsdafasdfas"
    db_dato.upload_footprint(vec_aux, email)


main()


if __name__ == "__main__":
    email = "yo@gmaklkljil.cosdmhhsd"
    db = myfirebase.MyFirebase()
    # aux = footprint.Footprint();
    # vec_aux = aux.save_footprint();
    vec_aux = "bbbbbb"
    db.upload_footprint(vec_aux, email)
