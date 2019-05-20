#!/usr/bin/python
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
import cv2

cap = cv2.VideoCapture(0);
while True:

	(rval, frame) = cap.read()
	frame = cv2.flip(frame,1,0)
	cv2.imwrite("cam1.jpg", frame)  # save frame as JPEG file
	#cv2.imwrite("cam1.webp", frame)
	cv2.imshow("Ventana",frame) # ver image
	# salir con Esc
	if cv2.waitKey(10) == 27:
		break
cap.release()