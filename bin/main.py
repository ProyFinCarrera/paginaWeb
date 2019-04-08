#!/usr/bin/python
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
from face import face
import subprocess
import sys
import threading
import cv2

print("Entreeeeeee")
recognizer = face.Face()


pathAntes = os.path.dirname(sys.argv[0])
path = pathAntes  + '/fingers.py'

def __main__():
    recognizer.create_fisher_recognizer()
    cont_name = 0
    name_aux = ""
    while True:
        if(opcion == "1"):
            print("opcion dentro")
            recognizer.new_capture("opcion")
        else:
            # print("opcion" + opcion)
            (reco, name, img) = recognizer.recognizer()
            if(name_aux == name) & (name != "Desconocido"):
                cont_name += 1
                if(cont_name >= 10):
                    cont_name = -10
                    # num_1 = 100
                    # datos = ['sudo', 'python', 'fingers.py', name]
                    datos = ['python', path, path, name]
                    # datos = ['./fingers.py', name]
                    p = subprocess.Popen(datos)
                   
                  
                    # stdout, stderr = p.communicate()
                    # print p
                    # print name
            else:
                name_aux = name
                cont_name = 0
            # mira para gaursa
            # recognizer.saveVideo("./face/",img)
            cv2.imshow("fas",img)
            recognizer.save_video(img)
         



__main__()



