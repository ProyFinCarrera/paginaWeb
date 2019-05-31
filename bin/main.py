# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa principara que lleva al gestion de funcionemineto del siemta reconocerdor
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
from PIL import Image
import glob
from recognizerVideo import recognizerVideo

# oscuro padre gray con 200 con sitem 2
# oscuro yo gray con 60 con sistema 1
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = PATH_DIR + "/tmp/mydaemon.PID"
def pintar():
    try:

        for infile in glob.glob( os.path.join(PATH_DIR,"./../public/video/video.jpg")):
            file =  os.path.join(PATH_DIR,"./../public/video/video.webp")
            #print("fffffff")
            #print(file)
            im = Image.open(infile).convert("RGB")
            #print("fffffff")
            #file=os.path.join(file,"video.webp")
            im.save(file, "WEBP")
    except:
            print("fuera")
def pan(fil):
    cv2.imshow("dd",fil)


try:
    if os.path.isfile(PID_FILE):
        print("%s el archivo ya existe, cerrando el proceso" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
        video = recognizerVideo.RecognizerVideo(maxiR=20, maxiF=20, selRecon=1)
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            rval, frame = cap.read()
            if rval:
                frame = cv2.flip(frame, 1, 0)
                aux = video.video_img(frame)
                # print(aux)
                if aux:
                    # Guardar en firebase el dato de mi huella.cd ..video
                    # busco el dadto de la base de datos nombre{herllas , hella hella}
                    # Recibo el diteros todo los datos y lo metodo en verify_pro
                    # verify_footprint() esta es la primerar si todo va bien si estoy dentro y tal busco el dato
                    # k corerponede a mi dedo y lo de posito en 0x02
                    # se guradar de forma permaente en una variable y listo
                    # si lo encuentro caso con el nombre mando datoas a mi servidofr firebase.video
                    # seteo el valor a firebase .
                    print("Encendia lector de huellas")
                    video.set_cont_cero()
            ##hil2 = threading.Thread(target=cv2.imshow,  args=("sdaf",frame),)
            ##hilo.start()
            #hil2.start()
            #cv2.imshow("face", frame)

            if cv2.waitKey(10) == 27:
                break
        cap.release()

except Exception as e:
    print('Exception message: ' + str(e))
finally:
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
