# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# File: SaveSystem: File where the functions that save the
# necessary files for the operation of the recognizing seitema are saved.
import os
from PIL import Image
import cv2
import numpy as np
import threading
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PATH_DIR = os.path.join(PATH_DIR, "..")

SAVE_IMG = os.path.join(os.path.join(PATH_DIR, ".."), "..")
SAVE_IMG = os.path.join(SAVE_IMG, "public")
SAVE_IMG = os.path.join(os.path.join(SAVE_IMG, "video"), "video.jpg")
# print(SAVE_IMG)

DIR_SAVE_FACE = os.path.join(PATH_DIR, "recognizer")
DIR_SAVE_FACE = os.path.join(os.path.join(
    DIR_SAVE_FACE, "att_faces"), "tmp_faces")
# print(DIR_SAVE_FACE)
MAX_F = 20
EXT = "jpg"
cont_img = 1
pid = 1


def save_face(face):
    global cont_img
    save = os.path.join(DIR_SAVE_FACE, "%d.%s" %
                        (cont_img, EXT))
    # im = Image.Image(face)
    # img = Image.fromarray(face[0], 'RGB')
    # im.save(save)
    #cv2.imwrite(save, face)
    t1 = threading.Thread(target=cv2.imwrite, args=(save, face,))
    t1.start()
    if(cont_img < MAX_F):
        cont_img += 1
    else:
        cont_img = 1

def save_img2(images):
    # print(images)
    # images = cv2.resize(images,(40,30))
    # images = cv2.resize(images,(80,60))
    images = cv2.resize(images,(160,120))
    #images = cv2.resize(images,(320,240))
    #images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    #np.save(SAVE_IMG, images)
    im = Image.fromarray(images,mode='RGB')
    
    #im.save(SAVE_IMG)
    t1 = threading.Thread(target=im.save, args=(SAVE_IMG,))
    t1.start()
    
def save_img(images):
    # print(images)
    # images = cv2.resize(images,(40,30))
    # images = cv2.resize(images,(80,60))
    images = cv2.resize(images,(160,120))
    #images = cv2.resize(images,(320,240))
    images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    #np.save(SAVE_IMG, images)
    im = Image.fromarray(images)
    
    #im.save(SAVE_IMG)
    t1 = threading.Thread(target=im.save, args=(SAVE_IMG,))
    t1.start()
    #t1.join()
   
    #pass_webp(SAVE_IMG)
    # images = cv2.resize(images,(400,400))
    #cv2.imwrite(SAVE_IMG, images)

def pass_webp(dir_image):
    try:
        for infile in glob.glob(dir_image):
            file =  os.path.join(os.path.dirname(dir_image),"video.webp")
            im = Image.open(infile)
            im.save(file, "WEBP")
    except:
            print("fuera")
# # Direccion actual
# path_dir_tmp = os.path.dirname(__file__)
# path_dir_tmp = os.path.join(path_dir_tmp, "..")
# path_dir_tmp = os.path.join(path_dir_tmp, "..")
# path_dir_tmp = os.path.join(path_dir_tmp, "..")
# path_dir_tmp = os.path.join(path_dir_tmp, "public")
# path_dir_tmp = os.path.join(path_dir_tmp, "video")
# path_dir_tmp = os.path.join(path_dir_tmp, "images")
# # print(os.path.isdir(path_dir_tmp))
# path_dir_save = os.path.dirname(__file__)
# path_dir_save = os.path.join(path_dir_save, "..")
# path_dir_save = os.path.join(path_dir_save, "recognizer")
# path_dir_save = os.path.join(path_dir_save, "att_faces")
# path_dir_save = os.path.join(path_dir_save, "orl_faces")
# # path_pfm= os.path.join(path_save,name)
# # print(os.path.isdir(path_dir_save))
# path_file_face = os.path.dirname(__file__)
# path_file_face = os.path.join(path_file_face, "..")
# path_file_face = os.path.join(path_file_face, "recognizer")
# path_file_facee = os.path.join(path_file_face, "att_faces")
# path_file_face = os.path.join(path_file_face, "tem_face")
# path_file_face = os.path.join(path_file_face, "1.jpg")

# ext = "pmg"


# class SaveSystem:
#     def __init__(self):
#         try:
#             self.__num_photo = 20
#             self.__path_file_face = path_file_face
#             self.__path_dir_save = path_dir_save
#             self.__path_dir_tmp = path_dir_tmp
#         except:
#             print("mall")


#     def save_tmp(self):
#         try:
#             cont = self.__rename_all("poner par eliminar")
#             num = self.__num_photo  - cont
#             if os.path.isdir(path_save)== False:
#                 os.mkdir(path_save)

#             for num in range(self.__num_photo):
#                 path_save=os.path.join(path_save, "%d.%s" % (num,ext))
#                 shutil.copy(self.__temp_face, path_save )
#         except:
#             print("No copy face")

#     """metodo que elimina todo lo k esta en tmpo la lipia"""
#     def delete_tmp_all(self):
#         pass
#     """metodo que elimina el archivo o archivo con los nombre tal se le pasa un json con los nombre y los elimina """
#     def delete_tmp(self,name):
#         pass

#     def save_confirme(self,name):
#         pass

#     def save_face(self,name):
#         try:
#             path_save = os.path.join(self.__save_face,name)
#             if os.path.isdir(path_save):
#                 self.__rename_all(path_save)
#                 num = len(os.listdir(path_save)) +1
#                 path_save=os.path.join(path_save, "%d.%s" % (num,ext))
#                 # img =cv2.imread(self.__temp_face)
#                 # cv2.imwrite(path_save,img)

#                 shutil.copy(self.__temp_face, path_save )
#             else:
#                 os.mkdir(path_save)
#                 path_save=os.path.join(path_save,"%d.%s" % (1,ext))
#                 # img =cv2.imread(self.__temp_face)
#                 # cv2.imwrite(path_save,img)
#                 shutil.copy(self.__temp_face,path_save )
#         except:
#             print("No copy face")

#     def __rename_all(self,path):
#         onlyfiles =os.listdir(path)
#         onlyfiles = sorted(onlyfiles, key=lambda s: int(s.split('.')[0]))
#         num=0
#         for f in onlyfiles:
#             num+=1
#             os.rename(os.path.join(path,f),os.path.join(path,"%d.%s" % (num,ext)))
#         return num

#     def save_faces(self,n_face,name):
#         for x in range(1, n_face):
#             self.save_face(name)

#     def delete_face(self,n_face,name):
#         try:
#             path_save = os.path.join(self.__save_face,name)
#             os.remove(path_save)
#             self.__rename_all(os.path.dirname(path_save))
#         except:
#             print("No delete")

#     def delete_all(self,name):
#         try:
#             path_save = os.path.join(self.__save_face,name)
#             shutil.rmtree(path_save)
#         except:
#             print("No delete all")

# if __name__ == "__main__":
#     aux= SaveSystem()
#     aux.save_faces(20,'pedro')
