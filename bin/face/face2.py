#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Class to do face verification with opencv.
import os

import cv2

import numpy

# self.path = os.path.join(self.fn_dir, self.fn_name)
# if not os.path.isdir(self.path):
#     os.mkdir(self.path)
#  hay que volver a entrena rel modelo si lo apago?
path = os.path.abspath("cam.jpg")
path = os.path.realpath( "./../../public/video/cam.jpg") 
print(path)

class RecognizedVideo:
    def __init__(self, file_haar, dir_img, size=4,
                 img_width=92, img_height=112):
        self.__size = size
        self.__file_haar = file_haar
        self.__dir_img = dir_img
        # sino crerar el direcctorio k puse
        self.__img_width = img_width
        self.__img_height = img_height
        self.__img = None
        (self.__names, images, lables) = self.__list_of_peoble()
        self.__model = self.__train_model(images, lables)

    # Public
    def video_on(self):
        self.__access_to_the_video()
        while True:
            self.__img = self.__take_picture_video()
            self.__recognizer_img(self.__img)

            cv2.imshow("Video", img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

    def video_off(self):
        self.__cap.release()

    def save_video(self, img):
        # path = os.path.abspath("../public/video/cam.jpg")
        # path = os.path.abspath("./public/video/cam.jpg")
        path = os.path.realpath( "./../../public/video/cam.jpg") 
        # print("ddddd . " + path)
        cv2.imwrite(path, img)
   
    # Dibujamos un rectangulo en las coordenadas del rostro
    def __paint_rectangle_img(self, x, y, w, h, img, name, prediction):   
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < 500:
             pr = '%s - %.0f' % (name, prediction)
             punto = (x - 10, y - 10)
             font = cv2.FONT_HERSHEY_PLAIN
             font_scale = 1
             font_color = (0, 255, 0)
             line_type = 0
             cv2.putText(img, pr,
                         punto, font,
                         font_scale, font_color,
                         line_type)
             #name_aux = self.names[prediction[0]]
             #reconoce = True
        else:
            cv2.putText(img, 'Desconocido', (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    # Private
    def __recognizer_img(self, img):
        mini = self.__processing_image(img)
        faces = self.__detect_face(mini)
        self.__compare_images(mini, faces, mini)
        reconoce = False
        name_aux = "Desconocido"

    def __compare_images(self, min, faces, gray):
        for i in range(len(faces)):
            face_i = faces[i]
            (x, y, w, h) = [v * self.size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = self.resize(face)
            # Reconociendo
            prediction = self.model.predict(face_resize)
            self.__paint_rectangle_img((x, y, w, h), img,
                                self.names[prediction[0]],
                                prediction[1])
        #(reconoce, name_aux, img)
        return img

    def __access_to_the_video(self):
        try:
            self.__haar_cascade = cv2.CascadeClassifier(self.__file_haar)
            self.__cap = cv2.VideoCapture(0)
            if (self.__cap.isOpened()):
                print('Access to the video device')
            else:
                raise ValueError('The video is not open')
        except Exception as e:
            print('The video sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

    def __list_of_peoble(self):
        (images, lables, names, id) = ([], [], {}, 0)
        for (subdirs, dirs, files) in os.walk(self.__dir_img):
            for subdir in dirs:
                names[id] = subdir
                subjectpath = os.path.join(self.__dir_img, subdir)
                print subjectpath
                for filename in os.listdir(subjectpath):
                    path = subjectpath + '/' + filename
                    lable = id
                    images.append(cv2.imread(path, 0))
                    lables.append(int(lable))
                id += 1
        (images, lables) = [numpy.array(lis) for lis in [images, lables]]
        return (names, images, lables)

    # OpenCV entrena un modelo a partir de las imagenes
    def __train_model(self, images, lables):
        model = cv2.face.createFisherFaceRecognizer()
        model.train(images, lables)
        return model

    def __take_picture_video(self):
        (rval, img) = self.__cap.read()
        return cv2.flip(img, 1, 0)

    def take_picture_file(self, file_name):
        # (rval, img) = self.cap.read()
        # return cv2.flip(img, 1, 0)
        return 0

    def __gray_scale_and_resize(self, img):
        gray = self.__gray_scale(img)
        return self.resize(gray)

    # we convert the image to black and white
    def __gray_scale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # def __resize(self, img):
    #     return cv2.resize(img, (self.im_width, self.im_height))

    def __resize_gray(self, img):
        new_tam = (img.shape[1] / self.__size, img.shape[0] / self.__size)
        return cv2.resize(img, new_tam)

    def __how_many_pictures(self, path):
        sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                if n[0] != '.'] + [0])[-1] + 1

    def resize_and_save(self, img):
        img_resize = cv2.resize(img, (self.__img_width, self.__img_height))
        num = self.howManyPictures(self.path) + 1
        cv2.imwrite('%s/%d.png' % (self.path, int(num)), img_resize)

    def __processing_image(self, img):
        gray = self.__gray_scale(img)
        return self.__resize_gray(gray)

    # coordinates of the faces and we keep poscicion
    def __detect_face(self, img):
        faces = self.__haar_cascade.detectMultiScale(img)
        faces = sorted(faces, key=lambda x: x[3])
        return faces

    def new_capture(self, name):
        self.fn_name = name
        cont = 0
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



file_haar = '/home/a/Escritorio/proy/paginaWeb/bin/face/haarcascade_frontalface_alt.xml'
dir_img = '/home/a/Escritorio/proy/paginaWeb/bin/face/att_faces/orl_faces'
aux = RecognizedVideo(file_haar, dir_img);
aux.video_on()
