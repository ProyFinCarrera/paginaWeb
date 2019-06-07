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

print("Save footprint ....")


def main():
    try:
        email = sys.argv[1]
        # email = "nuevo@gmail"
        # print("ESte es mi email: " + email)
        db = myfirebase.MyFirebase()
        aux = footprint.Footprint(timer_power = 30 );
        check , vec_aux = aux.save_footprint();
        print(check)
        print(vec_aux)
        if check:
            db.upload_footprint(vec_aux, email)
    except Exception as e:
        print('Exception message: ' + str(e))

        
if __name__ == "__main__":
    main()

   
            
            


    
    
