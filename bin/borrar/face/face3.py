#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Class to do face verification with opencv.
import os

import cv2

import numpy
import threading
# self.path = os.path.join(self.fn_dir, self.fn_name)
# if not os.path.isdir(self.path):
#     os.mkdir(self.path)
#  hay que volver a entrena rel modelo si lo apago?
path = os.path.abspath("cam.jpg")
path = os.path.realpath("./../../public/video/cam.jpg")
print(path)
print(os.path.abspath(os.path.realpath(__file__)))

class Video:
    def __init__(self, img_width=92, img_height=112):
        try:
            self.__cap = cv2.VideoCapture(0)
            if (self.__cap.isOpened()):
                self.__img = None
                print('Access to the video device')
            else:
                raise ValueError('The video is not open')
        except Exception as e:
            print('The video sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

    def video_on(self):
        while True:
            read_val = self.__take_picture_video()
            if(read_val):
                self.__show()
                # self.__save_video()
            key = cv2.waitKey(10)
            if key == 27:
                break

    def __take_picture_video(self):
        (read_val, img) = self.__cap.read()
        if(read_val):
            self.__img = cv2.flip(img, 1, 0)
        print(read_val)
        return read_val
    # save cam.jpg
    def __save_video(self):
        path = os.path.realpath( "./../../public/video/cam12.jpg") 
        cv2.imwrite(path, self.__img)

    def __show(self):
    	cv2.imshow("", self.__img)





def video():
    video = Video()  # Acedo al videro
    video.video_on()



video()