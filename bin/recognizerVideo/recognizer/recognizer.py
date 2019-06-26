# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: Recognizer
import os
import cv2
import numpy
import threading
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
MODEL = {1: cv2.face.LBPHFaceRecognizer_create,
         2: cv2.face.FisherFaceRecognizer_create,
         3: cv2.face.EigenFaceRecognizer_create}
OP_PREDICTION = {1: 200, 2: 500, 3: 500}
# 80

class Recognizer:
    """ Class that recognizes the image of the face.
        Attributes:
                __path_faces(str): Address where the faces are for comparison
                __model(obj: 'cv2'): Model for the realization and comparison
                in face recognition.
                __prediction(int): Percentage that fits each model.
                __images(img): Images of faces.
                __lables(str): Label that corresponds to the images.
                __names(str): Name the image.
                selRecon(int): Recognition option.
                        value 1: Local Binary Patterns Histograms(LBPH)(1996).
                        value 2: Fisherfaces (1997).
                        value 3: Eigenfaces (1991).

    """

    def __init__(self, selRecon=1):
        try:
            self.__path_faces = os.path.join(
                PATH_DIR, os.path.join("att_faces", "orl_faces"))
            t1 = threading.Thread(target=self._create_list_img_names)
            t1.start()
            t1.join()
            #self._create_list_img_names()
            # OpenCV entrena un modelo a partir de las imagenes
            self.__model = MODEL[selRecon]()
            self.__prediction = OP_PREDICTION[selRecon]
            hilo = threading.Thread(target=self.__model.train, args=(
                self.__images, self.__lables,),)
            hilo.start()
            hilo.join()

        except Exception as e:
            print('Error loaded Recognizer: ' + str(e))
            exit(1)
    def only_recognize(self, face):
        reconoce = False
        name = -1
        prediction = self.__model.predict(face)
        if prediction[1] < self.__prediction:
            name = self.__names[prediction[0]]
            reconoce = True
        return reconoce, name
            
    def recognize(self, img,face, point):
        """ Method that gives a percentage of recognition
            and also says if it is recognized or not.
            Note: The image "img" will be painted the name
            of who has recognized.
             Args:
                img(img): Imagen base
                face(img): Image of the face to recognize
                point(int,int): Point where the image is
                located.
             Returns:
                True If you have detected a person and name the person
                , False otherwise and -1.
         """
        reconoce = False
        name = -1
        prediction = self.__model.predict(face)
        point_a = (point[0] - 10, point[1] - 10)
        # print(prediction[1])
        if prediction[1] < self.__prediction:
            pr = '%s - %.0f' % (self.__names[prediction[0]], prediction[1])
            pr = self.__names[prediction[0]]
            font = cv2.FONT_HERSHEY_PLAIN
            font_scale = 2
            font_color = (0, 255, 0)
            line_type = 3
            cv2.putText(img, pr, point_a, font,
                        font_scale, font_color,
                        line_type)
            name = self.__names[prediction[0]]
            reconoce = True
        else:
            pr = '%s - %.0f' % ("Stranger", prediction[1])
            #pr = "Stranger"
            cv2.putText(img, pr, point_a,
                       cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        return reconoce, name

    def _create_list_img_names(self):
        """ Method to create a list of images and a
            list of corresponding names
        """
        (self.__images, self.__lables, self.__names, id) = ([], [], {}, 0)
        for (subdirs, dirs, files) in os.walk(self.__path_faces):
            for subdir in dirs:
                self.__names[id] = subdir
                subjectpath = os.path.join(self.__path_faces, subdir)
                # print(subjectpath)
                for filename in os.listdir(subjectpath):
                    path = os.path.join(subjectpath, filename)
                    lable = id
                    self.__images.append(cv2.imread(path, 0))
                    self.__lables.append(int(lable))
                id += 1
        (self.__images, self.__lables) = [numpy.array(
            lis) for lis in [self.__images, self.__lables]]


if __name__ == "__main__":
    print("Exmple processs")
    aux = Recognizer()
