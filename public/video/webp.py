from PIL import Image
import glob, os
import os.path 

cont =0
while(10000>cont):
	cont+=1 
	
	def pintar():
    try:

        for infile in glob.glob( os.path.join(PATH_DIR,"./../public/video/*.jpg")):
            file =  os.path.join(PATH_DIR,"./../public/video/video.webp")
            #print("fffffff")
            #print(file)
            
            im = Image.open(infile).convert("RGB")
            #print("fffffff")
            #file=os.path.join(file,"video.webp")
            im.save(file, "WEBP")
    except:
            print("fuera")
def pan(fil):