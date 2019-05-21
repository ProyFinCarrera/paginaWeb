#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Class to do face verification with opencv.
import os

import cv2

import numpy
import sys

#print(os.path.abspath(os.path.realpath(sys.argv[0]))) 
#print os.path.abspath(os.path.realpath(__file__))
#pathAntes = os.path( "/face/" + os.path.dirname(sys.argv[0]))
#print(pathAntes)

class Face:
    def __init__(self):
        # Tries to initialize the sensor
        try:
            self.size = 4
            #self.fn_haar = os.path.abspath('face/haarcascade_frontalface_alt.xml')
            #self.fn_dir = os.path.abspath('face/att_faces/orl_faces')
            #self.fn_haar = os.path.abspath('bin/face/haarcascade_frontalface_alt.xml')
            # self.fn_dir = os.path.abspath('bin/face/att_faces/orl_faces') 
            # print(os.getcwd())# no sirve
           
            self.fn_haar =pathAntes  + './haarcascade_frontalface_alt.xml'
            self.fn_dir = pathAntes  + '/att_faces/orl_faces'


            self.fn_name = ""
            (self.im_width, self.im_height) = (92, 112)
            self.haar_cascade = cv2.CascadeClassifier(self.fn_haar)
            self.path = os.path.join(self.fn_dir, self.fn_name)
            if not os.path.isdir(self.path):
                os.mkdir(self.path)
            self.cap = cv2.VideoCapture(0)
            if (self.cap.isOpened()):
                print('Access to the video device')
            else:
                raise ValueError('The video is not open')

        except Exception as e:
            print('The video sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

    def new_capture(self, name):
        self.fn_name = name
        cont = 0
        #path = os.path.abspath("../../public/video/cam.jpg")
        path = os.path.abspath("../../public/video/cam.jpg")
        while cont < 30:
            photo = self.photo()
            cv2.imwrite(path, photo)

            cv2.imshow('OpenCV', photo)
            

            # self.photo()
            cont += 1
            key = cv2.waitKey(10)
            if key == 27:
                break
    
    def take_picture(self):
        (rval, im) = self.cap.read()
        return cv2.flip(im, 1, 0)

    def gray_scale_and_resize(self, img):
        gray = self.grayScale(img)
        return self.resize(gray)

    def gray_scale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def resize_gray(self, img):
        new_tam = (img.shape[1] / self.size, img.shape[0] / self.size)
        return cv2.resize(img, new_tam)

    def resize(self, img):
        return cv2.resize(img, (self.im_width, self.im_height))

    # cara preparadas
    def detect(self, img):
        faces = self.haar_cascade.detectMultiScale(img)
        faces = sorted(faces, key=lambda x: x[3])
        return faces

    # cantida de fotos en la direccion path
    def how_many_pictures(self, path):
        sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                if n[0] != '.'] + [0])[-1] + 1

    def resize_and_save(self, img):
        img_resize = cv2.resize(img, (self.im_width, self.im_height))
        num = self.howManyPictures(self.path) + 1
        cv2.imwrite('%s/%d.png' % (self.path, int(num)), img_resize)

    def photo(self):
        img = self.takePicture()
        # convertimos la imagen a blanco y negro
        gray = self.grayScale(img)
        # redimensionar la imagen
        mini = self.resizeGray(gray)
        # buscamos las coordenadas de los rostros(si hay) y guardamos poscicion
        faces = self.detect(mini)
        if faces:
            face_i = faces[0]
            (x, y, w, h) = [v * self.size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = self.resize(face)
            # Dibujamos un rectangulo en las coordenadas del rostro
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            # Ponemos el nombre en el rectagulo
            cv2.putText(img, self.fn_name, (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            cont = self.howManyPictures(self.path)
            # Metemos la foto en el directorio
            cv2.imwrite('%s/%s.pgm' % (self.path, cont), face_resize)
        return img

    def recognizer(self):
        img = self.take_picture()
        # convertimos la imagen a blanco y negro
        gray = self.gray_scale(img)
        # redimensionar la image
        mini = self.resize_gray(gray)
        # guadamos cordenadas de rotros (si las hay)
        faces = self.detect(mini)
        reconoce = False
        name_aux = "Desconocido"
        for i in range(len(faces)):
            face_i = faces[i]
            (x, y, w, h) = [v * self.size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = self.resize(face)
            # Reconociendo
            prediction = self.model.predict(face_resize)
            # Dibujamos un rectangulo en las coordenadas del rostro
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if prediction[1] < 500:
                pr = '%s - %.0f' % (self.names[prediction[0]], prediction[1])
                punto = (x - 10, y - 10)
                font = cv2.FONT_HERSHEY_PLAIN
                font_scale = 1
                font_color = (0, 255, 0)
                line_type = 0
                cv2.putText(img, pr,
                            punto, font,
                            font_scale, font_color,
                            line_type)
                name_aux = self.names[prediction[0]]
                reconoce = True
                break
            else:
                cv2.putText(img, 'Desconocido', (x - 10, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        return (reconoce, name_aux, img)

    def save_video(self, img):
        # path = os.path.abspath("../public/video/cam.jpg")
        path = os.path.abspath("./public/video/cam.jpg")
        # print("ddddd . " + path)
        cv2.imwrite(path, img)

    # Crear una lista de imagenes y una lista de nombres correspondientes
    def create_fisher_recognizer(self):
        (images, lables, names, id) = ([], [], {}, 0)
        for (subdirs, dirs, files) in os.walk(self.fn_dir):
            for subdir in dirs:
                names[id] = subdir
                subjectpath = os.path.join(self.fn_dir, subdir)
                print( subjectpath)
                for filename in os.listdir(subjectpath):
                    path = subjectpath + '/' + filename
                    lable = id
                    images.append(cv2.imread(path, 0))
                    lables.append(int(lable))
                id += 1
        (images, lables) = [numpy.array(lis) for lis in [images, lables]]
        self.names = names
        # OpenCV entrena un modelo a partir de las imagenes
        self.model = cv2.face.createFisherFaceRecognizer()
        self.model.train(images, lables)

aux = Face();
aux.newCapture("fdsa")
# aux.otro()
