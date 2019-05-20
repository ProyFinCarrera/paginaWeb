#! /usr/bin/python2
# -*- coding: utf-8 -*-
import cv2, sys, numpy, os
size = 6
fn_haar = 'haarcascade_frontalface_alt.xml'
fn_dir = 'att_faces/orl_faces'
fn_name = sys.argv[1]
path = os.path.join(fn_dir, fn_name)
if not os.path.isdir(path):
    os.mkdir(path)
#(im_width, im_height) = (92, 112)
(im_width, im_height) = (10, 10)
haar_cascade = cv2.CascadeClassifier(fn_haar)

webcam = cv2.VideoCapture(0)

count = 0
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    crop_img = im
    gray = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
    faces = haar_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
               if n[0]!='.' ]+[0])[-1] + 1
        # Metemos fotos dentro de la carpeta
        cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        crop_img = im[y:y+h, x:x+w]
        
        cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
        count += 1
    #Mostramos la imagen
    # cv2.imshow("cropped", crop_img)
    # cv2.imwrite("./../video/cam.jpg", im)
    #cv2.imwrite("./../video/cam1.jpg", crop_img)
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break




    def recognizer(self):
        names = self.createFisherRecognizer()

        contName=0
        nameAux =""
        while True:
            img = self.takePicture()
            #convertimos la imagen a blanco y negro
            gray = self.grayScale(img)
            #redimensionar la image
            mini = self.resizeGray(gray)
            """buscamos las coordenadas de los rostros (si los hay) y guardamos su posicion"""
            faces = self.detect(mini)
            
            for i in range(len(faces)):
                face_i = faces[i]
                (x, y , w , h) = [v * self.size for v in face_i]
                face = gray[y:y+h,x:x+w]
                face_resize = self.resize(face)
                # Reconociendo
                prediction = self.model.predict(face_resize)
                #Dibujamos un rectangulo en las coordenadas del rostro
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if prediction[1] < 100:
                    cv2.putText(img,
                        '%s - %.0f' % (names[prediction[0]],prediction[1]),
                        (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                    
                    if contName >= 10:
                        print( "Estoy con " +str(contName))
                    else:
                        if nameAux == names[prediction[0]]:
                            print("Somo iguales y sumo")
                            contName+=1
                        else:
                            print("Lo pongo a 0 :"+nameAux)
                            nameAux = names[prediction[0]]
                            contName=0
                else :
                    cv2.putText(img,'Desconocido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                    contName=0

            cv2.imwrite("public/video/cam.jpg", img)
            cv2.imshow('OpenCV', img)

            key = cv2.waitKey(10)
            if key == 27:
                break