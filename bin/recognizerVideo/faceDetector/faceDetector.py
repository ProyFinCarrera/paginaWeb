# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: FaceDetector.
import os
import cv2
import threading   
if __name__ == "__main__":
    import saveFace
else:
    from recognizerVideo.faceDetector import saveFace

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


class FaceDetector:
    """ Class that detects in an image if there is a face.
        Attributes:
            __tam_face ((int)(int)): Size that the face will have
            after detecting.
            __size (int): Size of the image is reduced to optimize
            the detection algorithm.
            __dir_haarcascade (str): The default configuration file
            for default is haarcascade_fromtalface_default.xml
            __sys_det(:obj:`cv2`): Cv2 detector system,
            configured with the most optimal data.
            __op_contrast(boolean): It is true to prepare images with
            contrast, false is not used contrast.
            __t_contrast(int): Select the type of constarte.
                    value 1 the record of does by histogram.
                    value 2 the constrate is made by adaptive equalization
                    of the histogram.
    """

    def __init__(self, file_haarcascade=os.path.join(
            PATH_DIR, "haarcascade_frontalface_default.xml"),
            size=4, size_face_w=92, size_face_h=112,
            op_contrast=False, t_contrast=1, save_face=False ):
        try:
            self.__tam_face = (size_face_w, size_face_h)
            self.__size = size
            self.__save_face = save_face
            self.__file_haarcascade = file_haarcascade
            self.__sys_det = cv2.CascadeClassifier(self.__file_haarcascade)
            self.__op_contrast = op_contrast
            self.__t_contrast = t_contrast
            if self.__sys_det.empty():
                raise ValueError("No Exist file haarcascade.")
        except Exception as e:
            print('Error loaded FaceDetector: ' + str(e))
            exit(1)

    def detect(self, img):
        """ Class methods that paints a rectangle where there is a face.
        Args:
            img: Image where the face will be detected.
        Returns:
            resul: True if there is a picture, False otherwise.
            pos_face(int,int): if "result" is true, it returns
            the Point where the face is placed in teh image that
            is passed as a parameter, (0,0) otherwise.
         """
        resul = False
        face_resize = False
        pos_face = (0, 0)
        prepared_img = self._prepare_img(img)
        # cv2.imshow("imagen pre",prepared_img)
        faces = self.__sys_det.detectMultiScale(
            prepared_img, scaleFactor=1.05, minNeighbors=5,minSize=(50,50),maxSize=(67,67))#minSize=(50,50),maxSize=(67,67)
        tam = len(faces)
     
        #print(tam)
        if tam > 0:
            (x, y, w, h) = (faces[0][0]+12, faces[0]
                            [1]+9, faces[0][2]-25, faces[0][3]-10)
            face = prepared_img[y:y + h, x:x + w]
            face_resize = self._prepare_face(face)

            # Dibujamos un rectangulo en las coordenadas del rostro
            pos_a = (x * self.__size, y * self.__size)
            pos_b = (x * self.__size + w * self.__size,
                     y * self.__size + h * self.__size)
            img = cv2.rectangle(img, pos_a, pos_b, (0, 255, 0), 3)
            resul = True
            pos_face = (x * self.__size, y * self.__size)
            if self.__save_face:
                t1 = threading.Thread(
                    target=saveFace.save_face, args=(face_resize,))
                t1.start()
            return (resul, face_resize , pos_face)
        return (resul, face_resize, pos_face)

    def _prepare_img(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_min = self._resize_img(gray)
        if(self.__op_contrast):
            gray_c = self._prepare_constrate(gray_min)
            return gray_c
        else:
            return gray_min

    def _prepare_constrate(self, img):
        """Contraste de histograma"""
        if(self.__t_contrast == 1):
            # black puts it more white
            return cv2.equalizeHist(img)
        """Contraste de ecualización adaptable del histograma"""
        if(self.__t_contrast == 2):
            clahe = cv2.createCLAHE(
                clipLimit=2.0, tileGridSize=(8, 8))  # (8,8)
            return clahe.apply(img)

    def _resize_img(self, img):
        resize_a = int(img.shape[1] / self.__size)
        resize_b = int(img.shape[0] / self.__size)
        return cv2.resize(img, (resize_a, resize_b))

    def _prepare_face(self, face):
        return cv2.resize(face, self.__tam_face)


if __name__ == "__main__":
    print("Exmple processs")
    aux = FaceDetector()
    # img = cv2.imread("example2.jpg")
    img = cv2.imread("example1.jpg")
    rt, (x, y) = aux.detect(img)
    cv2.imshow('image', img)
    #if rt:
    #    cv2.imshow("Face", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
