# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: recognizerVideo
import os
import cv2
import threading

if __name__ == "__main__":
    from faceDetector import faceDetector
    from recognizer import recognizer
else:
    from recognizerVideo.faceDetector import faceDetector
    from recognizerVideo.recognizer import recognizer
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PATH_VID = os.path.join(os.path.join(os.path.join(os.path.join(
    os.path.dirname(os.path.dirname(PATH_DIR)), "public"), "video")))
EXT = "jpg"


class RecognizerVideo:
    """ Class that counts the number followed by images in whic
        the same face appears.
        Attributes:
            __temp_face (str): Folder where the faces are saved
            __save_img (str): File where the image are save.
            __det (:obj:`FaceDetector()`): Detects the face in the image.
            __rec (:obj:`Recognizer()`, optional): Recognize the face.
            __cont_face (int): Times the same face has been detected.
            __cont_img (int): Number of photos of face that has been save.
            __maxiR (int): Maximum recognition value to know that we are
            facing that person.
            __maxiF (int): Maximum number of files saved in the
            __temp_face folder
            selRecon(int): Option for the type of recognition.
    """

    def __init__(self, maxiR=20, maxiF=20, selRecon=1):
        try:
            self.__temp_face = os.path.join(PATH_DIR, os.path.join(
                "recognizer", os.path.join("att_faces", "tmp_face")))
            file = "%s.%s" % ("video", EXT)
            self.__save_img = os.path.join(PATH_VID, file)
            self.__det = faceDetector.FaceDetector()
            self.__rec = recognizer.Recognizer(selRecon=selRecon)
            self.__cont_face = 0
            self.__cont_img = 1
            self.__maxiR = maxiR
            self.__maxiF = maxiF
            # print("Loaded RecognizerVideo")
        except Exception as e:
            print('Error loaded FaceDetector: ')
            exit(1)

    def video_img(self, frame):
        """ Class methods that recognize a person's face in an image
            Args:
                frame: Image where the face will be detected.
            Returns:
                True If you have detected a person self._max
                followed., False otherwise.
        """
        rt, face, point = self.__det.detect(frame)
        if rt:
            self._save_face(face)
            rec = self.__rec.recognize(frame, face, point)
            self._repeated_times_recognized(rec)
            # print(str(self.__cont_face) + " " + str(rec))
        cv2.imwrite(self.__save_img, frame)  # safe imagen
        return self._maximum_recognition()

    def set_cont_cero(self):
        """Class methods what it does is initialize the value of __cont a 0"""
        self.__cont_face = 0

    def _repeated_times_recognized(self, rec):
        if rec:
            self.__cont_face += 1
        else:
            self.set_cont_cero()

    def _maximum_recognition(self):
        if self.__cont_face == self.__maxiR:
            return True
        else:
            return False

    def _save_face(self, face):
        save = os.path.join(self.__temp_face, "%d.%s" %
                            (self.__cont_img, EXT))
        cv2.imwrite(save, face)
        if(self.__cont_img < self.__maxiF):
            self.__cont_img += 1
        else:
            self.__cont_img = 1


if __name__ == "__main__":
    aux = RecognizerVideo()
    # aux.video_on()
