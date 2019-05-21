# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: Recognizer
import os
import cv2
import numpy
path_dir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


class Recognizer:
	"""class that recognizes the image of the face."""
	def __init__(self):	
		try:
			self.__path_faces= os.path.join(path_dir,os.path.join("att_faces","orl_faces"))
			self.__create_list_img_names()
			# OpenCV entrena un modelo a partir de las imagenes
			# self.__model = cv2.face.LBPHFaceRecognizer_create()
			self.__model = cv2.face.FisherFaceRecognizer_create()
			# self.__model =  cv2.face.EigenFaceRecognizer_create()
			self.__model.train( self.__images,self.__lables)
		except:
			print('Error loaded FaceDetector: ')
			exit(1)
	"""Method that gives a percentage of recognition and also says if it is recognized or not."""
	def recognize(self,img,face,x,y):
		reconoce = True
		prediction = self.__model.predict(face)
		print(prediction[1])
		if prediction[1] < 500:
			pr = '%s - %.0f' % (self.__names[prediction[0]], prediction[1])
			punto = (x - 10, y - 10)
			font = cv2.FONT_HERSHEY_PLAIN
			font_scale = 1
			font_color = (0, 255, 0)
			line_type = 0
			cv2.putText(img, pr,punto, font,
                            font_scale, font_color,
                            line_type)
			name_aux = self.__names[prediction[0]]
			reconoce = True
		else:
			cv2.putText(img, 'Desconocido', (x - 10, y - 10),
				cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
		return reconoce
	"""Method to create a list of images and a list of corresponding names"""
	def __create_list_img_names(self):
		(self.__images,  self.__lables,self.__names, id) = ([], [], {},0)
		for (subdirs, dirs, files) in os.walk(self.__path_faces):
			for subdir in dirs:
				self.__names[id] = subdir
				subjectpath = os.path.join(self.__path_faces, subdir)
				print(subjectpath)
				for filename in os.listdir(subjectpath):
					path = os.path.join(subjectpath ,filename)
					lable = id
					self.__images.append(cv2.imread(path, 0))
					self.__lables.append(int(lable))
				id += 1
		(self.__images, self.__lables) = [numpy.array(lis) for lis in [self.__images,  self.__lables]]

if __name__ == "__main__":
    print("Exmple processs")
    aux = Recognizer()