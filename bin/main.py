# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa principara que lleva al gestion de
# funcionemineto del siemta reconocerdor:
#           1. Clase RecognonizerVideo reconozcera a una persona en una imagen,si la reconoce 20 veces seguir
#                la persona quires registarse.
#            2. llaamara al reconocerdor de huella para ver si estas en el siemta.path
#            3. se bajara lso datos del firebase.path
#            4. Se comparara y verificara los datos y si concuerda todo se registar en firebase la entrada.
import subprocess
import threading
import sys
import cv2
import os
import signal
from recognizerVideo import recognizerVideo
from myfirebase import myfirebase
from footprint import footprint

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = PATH_DIR + "/tmp/mydaemon.PID"
pid = 1

try:
    if os.path.isfile(PID_FILE):
        print("%s el archivo ya existe, cerrando el proceso" % PID_FILE)
        pid = open(PID_FILE, "w").read()
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        cap = cv2.VideoCapture(0)
        det_video = recognizerVideo.RecognizerVideo(
             maxiR=20, maxiF=20, selRecon=1)
        # det_footprint = footprint.Footprint()
        # db = myfirebase.MyFirebase()
        cont=1
        while cap.isOpened():
            rval, frame = cap.read()
            if rval:
                frame = cv2.flip(frame, 1, 0)

                aux, name_img = det_video.video_img(frame)
               
                if aux:
                    cont+=1
                    name_img ="nuevo_yo"
                    print (name_img)
                    cmd = 'python fingers.py '+ name_img

                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if(p.poll()):
                        (stdout, stderr) = p.communicate()
                        print(stdout)
                        print(stderr)
                        print(p.poll())
                    #thread = threading.Thread(target=os.system, args=(todo))
                    #thread.start()
                    # a = os.system('python fingers.py '+ name_img)
                    # print(a)

                    print("Encendia lector de huellas")
                    det_video.set_cont_cero()
            # cv2.imshow("face", frame)

            if cv2.waitKey(10) == 27:
                break
        cap.release()

except Exception as e:
    print('Exception message: ' + str(e))
finally:
    if(pid!=1):
        pirnt("Me carge el proceso:"+str(pid))
        os.kill(pid, signal.SIGTERM)
    
    os.unlink(PID_FILE)
    # eliminar la carpete de las fotos.


# # showing stat information of file "foo.txt"
# statinfo = os.stat('foo.txt')
# PATH_DIR = os.path.abspath(os.path.realpath(__file__))
# pathAntes = os.path.dirname(sys.argv[0])
# path = PATH_DIR  + '/fingers.py'

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
