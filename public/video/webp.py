from PIL import Image
import glob, os
import os.path 

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
cont =0
while(10000>cont):
    cont+=1
    try:
        for infile in glob.glob( os.path.join(PATH_DIR,"*.jpg")):
            file =  os.path.join(PATH_DIR,"video.webp")
            im = Image.open(infile)
            print("dentro")
            im.save(file, "WEBP")
    except:
            print("fuera")
