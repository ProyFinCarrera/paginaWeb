# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
#from face import face

import subprocess
import sys
import threading
import cv2
import os
import sys
from recognizerVideo import recognizerVideo

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
pathDir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
pid = str(os.getpid())
pidfile = pathDir + "/tmp/mydaemon.pid"

try:
    if os.path.isfile(pidfile):
        print("%s el archivo ya existe, cerrando el proceso" % pidfile)
        raise ValueError('The program is in process')
    else:
        open(pidfile, "w").write(pid)
        video  = recognizerVideo.RecognizerVideo( maxiR=20, maxiF=20, selRecon=1)
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            rval,frame = cap.read()
            if rval:
                frame = cv2.flip(frame,1,0)
                aux = video.video_img(frame)
                # print(aux)
                if aux:
                    print("Encendia lector de huellas")
                    video.set_cont_cero()
            cv2.imshow("face",frame)            
            if cv2.waitKey(10) == 27:
                break
        cap.release()

except Exception as e:
    print('Exception message: ' + str(e))
finally:
    os.unlink(pidfile)
    # eliminar la carpete peptio




# # showing stat information of file "foo.txt"
# statinfo = os.stat('foo.txt')
# pathDir = os.path.abspath(os.path.realpath(__file__))
# pathAntes = os.path.dirname(sys.argv[0])
# path = pathDir  + '/fingers.py'

# def __main__():
#     recognizer.create_fisher_recognizer()
#     cont_name = 0
#     name_aux = ""
#     while True:
#         if(opcion == "1"):
#             print("opcion dentro")
#             recognizer.new_capture("opcion")
#         else:
#             # print("opcion" + opcion)
#             (reco, name, img) = recognizer.recognizer()
#             if(name_aux == name) & (name != "Desconocido"):
#                 cont_name += 1
#                 if(cont_name >= 10):
#                     cont_name = -10
#                     # num_1 = 100
#                     # datos = ['sudo', 'python', 'fingers.py', name]
#                     datos = ['python', path, path, name]
#                     # datos = ['./fingers.py', name]
#                     p = subprocess.Popen(datos)
                   
                  
#                     # stdout, stderr = p.communicate()
#                     # print p
#                     # print name
#             else:
#                 name_aux = name
#                 cont_name = 0
#             # mira para gaursa
#             # recognizer.saveVideo("./face/",img)
#             cv2.imshow("fas",img)
#             recognizer.save_video(img)

