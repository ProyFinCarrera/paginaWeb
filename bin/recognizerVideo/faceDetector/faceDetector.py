# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: FaceDetector.
import os
import cv2
#https://becominghuman.ai/face-detection-using-opencv-with-haar-cascade-classifiers-941dbb25177

path_dir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

class FaceDetector:
    """Class that detects in an image if there is a face.
    the default configuration file is haarcascade_fromtalface_default.xml
    size = porcentra that we will make the image smaller for algorithm optimization."""
    def __init__(self, dir_haarcascade="haarcascade_frontalface_default.xml", size=4, size_face_w=92, size_face_h=112):
    	try:
            self.__tam_face = (size_face_w,size_face_h)
            self.__size = size
            self.__dir_haarcascade = os.path.join(path_dir,dir_haarcascade)
            print(self.__dir_haarcascade)
            self.__haar_cascade = cv2.CascadeClassifier(self.__dir_haarcascade)
            if self.__haar_cascade.empty():
                raise ValueError("No Exist file haarcascade.")
    	except Exception as e:
    		print('Error loaded FaceDetector: ' + str(e))
    		exit(1)
    """Method that paints a rectangle where there is a face.""" 
    def detect(self,img):
        prepared_img = self.__prepare_img(img)
        faces = self.__haar_cascade.detectMultiScale(prepared_img ,scaleFactor=1.05,minNeighbors=5,minSize = (60, 60))
        tam =len(faces)
        print(tam)
        if tam>0:
            face_i = faces[0]
            (x, y, w, h) =(faces[0][0]+10,faces[0][1]+10,faces[0][2]-20,faces[0][3]-10)
            face = prepared_img[y:y + h, x:x + w]
            face_resize = self.__prepare_face(face)
            # Dibujamos un rectangulo en las coordenadas del rostro
            img=cv2.rectangle(img, (x*self.__size, y*self.__size), (x*self.__size + w*self.__size, y*self.__size + h*self.__size), (0, 255, 0), 3)
            return (True,face)
        return (False,False)
    """Method that creates a new image so that the algorithms of detection are more efficient."""
    def __prepare_img(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_min = self.__resize_img(gray)
        gray_c = self.__prepare_constrate(gray_min)
        return gray_c
    """Contraste de ecualización adaptable del histograma"""
    def __prepare_constrate(self,img):
    	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    	cl1 = clahe.apply(img)
    	return cl1
    """Method that reduces the image self.__size times"""
    def __resize_img(self, img):
        return cv2.resize(img,(int(img.shape[1] / self.__size),int(img.shape[0] / self.__size)))
    """Method that adjusts the image of the face to an optimal value so that it is optimal"""
    def __prepare_face(self,face):
        return cv2.resize(face, self.__tam_face)

if __name__ == "__main__":
    print("Exmple processs")
    aux = FaceDetector()
    #img = cv2.imread("3rostros.jpg")
    img = cv2.imread("1rostro.jpg")
    rt ,face = aux.detect(img)
    cv2.imshow('image',img)
    if rt:
        cv2.imshow("Face",face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
