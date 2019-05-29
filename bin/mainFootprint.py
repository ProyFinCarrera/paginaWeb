# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Ejemplo: cojo archivo
#from face import face

import subprocess
import sys
import threading
import cv2
import os
import sys
from recognizerVideo.saveSystem import saveSystem

# Pasara de tmpface a imagenes alemno 20 fotos


print("Estoy en main footprint")
 
aux= saveSystem.SaveSystem()
aux.save_tmp()