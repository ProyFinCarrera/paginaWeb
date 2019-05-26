# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es.
# Class: SaveSystem
import os
# Direccion actual
path_dir_tmp= os.path.dirname(__file__)
path_dir_tmp= os.path.join(path_dir_tmp,"..")
path_dir_tmp= os.path.join(path_dir_tmp,"..")
path_dir_tmp= os.path.join(path_dir_tmp,"..")
path_dir_tmp= os.path.join(path_dir_tmp,"public")
path_dir_tmp= os.path.join(path_dir_tmp,"video")
path_dir_tmp= os.path.join(path_dir_tmp,"images")
#print(os.path.isdir(path_dir_tmp))
path_dir_save= os.path.dirname(__file__)
path_dir_save= os.path.join(path_dir_save,"..")
path_dir_save= os.path.join(path_dir_save,"recognizer")
path_dir_save= os.path.join(path_dir_save,"att_faces")
path_dir_save= os.path.join(path_dir_save,"orl_faces")
#path_pfm= os.path.join(path_save,name)
#print(os.path.isdir(path_dir_save))
path_file_face= os.path.dirname(__file__)
path_file_face= os.path.join(path_file_face,"..")
path_file_face= os.path.join(path_file_face,"recognizer")
path_file_facee= os.path.join(path_file_face,"att_faces")
path_file_face= os.path.join(path_file_face,"tem_face.jpg")

ext = "pmg"
class SaveSystem:
    """Class that detects in an image if there is a face.
    the default configuration file is haarcascade_fromtalface_default.xml
    size = porcentra that we will make the image smaller for algorithm optimization."""
    def __init__(self):
        try:
            self.__num_photo = 20
            self.__path_file_face = path_file_face
            self.__path_dir_save=path_dir_save
            self.__path_dir_tmp =path_dir_tmp

     """Metodo que guarda temporar mente numeor x de fotos esto estara numeradas desde 1 al 20si falta x voyver a terminar con tal
     siempre compuerga cantidad de carpetas dentro del temporar.20-ese numoe y keda perfet"""
    def save_tmp(self):
        
         try:
            cont = self.__rename_all("poner par eliminar")
            num = self.__num_photo  - cont
            if os.path.isdir(path_save)== False:
                os.mkdir(path_save)
            
            for num in range(self.__num_photo)
                path_save=os.path.join(path_save, "%d.%s" % (num,ext))
                shutil.copy(self.__temp_face, path_save )
        except:
            print("No copy face")

    """metodo que elimina todo lo k esta en tmpo la lipia"""
    def delete_tmp_all(self):
        pass
    """metodo que elimina el archivo o archivo con los nombre tal se le pasa un json con los nombre y los elimina """
    def delete_tmp(self,name):
        pass
     """Metodo que guarda en la bbdd para el entrenmiento las 20 fotos que estan dentro de ahi con el nombre del archvo juan para que no sean igna el nom
     va haces el nombre00 numero de carpeta que hay guradadas"""
    def save_confirme(self,name):
        pass
    
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
        return num

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
    path_dir = os.path.dirname(__file__)
    path_dir= os.path.join(path_dir,"..")
    path_dir= os.path.join(path_dir,"..")
    path_dir= os.path.join(path_dir,"..")
    path_dir= os.path.join(path_dir,"public")
    path_dir= os.path.join(path_dir,"video")
    path_dir= os.path.join(path_dir,"images")
    print(os.path.isdir(path_dir))
    path_save = os.path.dirname(__file__)
    path_save= os.path.join(path_save,"..")
    path_save= os.path.join(path_save,"recognizer")
    path_save= os.path.join(path_save,"att_faces")
    path_save= os.path.join(path_save,"orl_faces")
    #path_pfm= os.path.join(path_save,name)
    print(os.path.isdir(path_save))