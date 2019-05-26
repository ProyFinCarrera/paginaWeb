# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: recognizerVideo
import os
import cv2
import threading
import shutil # opercion file.
from recognizerVideo.faceDetector import faceDetector
from recognizerVideo.recognizer import recognizer
#from faceDetector import *
#from recognizer import *
#https://becominghuman.ai/face-detection-using-opencv-with-haar-cascade-classifiers-941dbb25177

path_dir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
# self.__temp_face = os.path.join(path_dir, os.path.join("recognizer", os.path.join("att_faces","%s.%s" % ("tmp_face",ext))))
ext ="jpg"
class RecognizerVideo:
    """Class that detects in an image if there is a face.
    the default configuration file is haarcascade_fromtalface_default.xml
    size = porcentra that we will make the image smaller for algorithm optimization."""
    def __init__(self):
        try:
            self.__temp_face = os.path.join(path_dir, os.path.join("recognizer", os.path.join("att_faces","tmp_face")))
            self.__save_face =os.path.join(os.path.dirname( self.__temp_face),"orl_faces")
            self.__save_img =os.path.join( os.path.join( os.path.join(os.path.dirname( os.path.dirname(path_dir)),"public"),"video"),"video.jpg")
            self.__cap=""
            if False:
                self.__cap = cv2.VideoCapture(0)
            else:
                 self.__cap = cv2.VideoCapture()

            self.__det = faceDetector.FaceDetector()
            self.__rec = recognizer.Recognizer()
            self.__cont = 0
            self.__cont_photos = 1
            self.__max = 20
            if self.__cap.isOpened():
                print("VideoCapture loades")
            else:
                print("No loaded Video")
                #raise ValueError("Video not loaded.")
        except Exception as e:
            print('Error loaded FaceDetector: ' + str(e))
            exit(1)
    """Method that paints a rectangle where there is a face.""" 
    # def video_on(self):
    #     while True:
    #         (rval, frame) = self.__cap.read()
    #         frame = cv2.flip(frame,1,0)
    #         rt ,face,x,y = self.__det.detect(frame)
    #         if rt:
    #             cv2.imwrite(self.__temp_face, face)
    #             # cv2.imshow("face",face)
    #             self.__rec.recognize(frame,face,x,y)

    #             # self.save_face("OscuraPadreGray")
    #         cv2.imshow("Ventana",frame) # ver image
    #         # print(self.__save_img)
    #         cv2.imwrite(self.__save_img , frame)
        #     if cv2.waitKey(10) == 27:
        #        break
        # self.__cap.release()
    """Method that paints a rectangle where there is a face.""" 
    def video_img(self,frame):
        frame = cv2.flip(frame,1,0)
        rt ,face,x,y = self.__det.detect(frame)
        if rt:
            #cv2.imwrite(self.__temp_face, face)
            #self.save_face("yoclaro")
            save  =os.path.join( self.__temp_face, "%d.%s" % (self.__cont_photos,ext)  )
            if(self.__cont_photos < self.__max):
                self.__cont_photos+=1
            else:
                self.__cont_photos=1
            
            cv2.imwrite(save , face)
            rec = self.__rec.recognize(frame,face,x,y)
            print(self.__cont)
            if rec:
                self.__cont+=1
            else:
                print("Cerooooooooooo")
                self.set_cont_cero()

        cv2.imwrite(self.__save_img,frame)
        cv2.imshow("Dentto",frame)
        if self.__cont == self.__max:
            return True
        else:
            return False

    def set_cont_cero(self):
        self.__cont=0

    def save_face(self,name):
        try:
            path_save = os.path.join(self.__save_face,name)           
            if os.path.isdir(path_save):
                self.__rename_all(path_save)
                num = len(os.listdir(path_save)) +1
                path_save=os.path.join(path_save, "%d.%s" % (num,ext))
                #img =cv2.imread(self.__temp_face)
                #cv2.imwrite(path_save,img)
                
                shutil.copy(self.__temp_face, path_save )
            else: 
                os.mkdir(path_save)
                path_save=os.path.join(path_save,"%d.%s" % (1,ext))
                #img =cv2.imread(self.__temp_face)
                #cv2.imwrite(path_save,img)
                shutil.copy(self.__temp_face,path_save )
        except:
            print("No copy face")

    def __rename_all(self,path):
        onlyfiles =os.listdir(path)
        onlyfiles = sorted(onlyfiles, key=lambda s: int(s.split('.')[0]))
        num=0
        for f in onlyfiles:
            num+=1
            os.rename(os.path.join(path,f),os.path.join(path,"%d.%s" % (num,ext)))

    def save_faces(self,n_face,name):
        for x in range(1, n_face):
            self.save_face(name)

    def delete_face(self,n_face,name):
        try:
            path_save = os.path.join(self.__save_face,name)   
            os.remove(path_save)
            self.__rename_all(os.path.dirname(path_save))
        except:
            print("No delete")

    def delete_all(self,name):
        try:
            path_save = os.path.join(self.__save_face,name)   
            shutil.rmtree(path_save)
        except:
            print("No delete all")

if __name__ == "__main__":
    aux =RecognizerVideo()
    #aux.video_on()
