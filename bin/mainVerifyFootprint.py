#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File fingers.py:
#   1. Execution of the fingerprint recognition system.
#   2. Downloading data from firebase to find similarity with other data.
#   3. Registration of date in firebase
#   4. The double identification is verified
import os
import sys
import threading
from myfirebase import myfirebase
from footprint import footprint
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
FILE_PASS = os.path.join(os.path.join(PATH_DIR, "tmp"), "pass.PID")
PID_PROCESS = os.path.join(os.path.join(PATH_DIR, "tmp"), "process.PID")
FILE_FIN = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")
PID = str(os.getpid())
# print(PID_FILE)
def main():
    try:
        if os.path.isfile(PID_PROCESS)==False:
            open(PID_PROCESS, "w").write(PID)
        veryfy()
    except Exception as e:
        print("Salir" +str(e))
        raise e
    finally:
        open(FILE_FIN, "w").write("")

def veryfy():
    finguer = footprint.Footprint()
    db = myfirebase.MyFirebase()
    name_img = sys.argv[1]
    #print(name_img)
    # name_img = "jairo_aaaaaa"
    firstName = name_img.split("_")[0]
    email = db.search_email(name_img)
    #print(email)
    my_json = db.vect_charasteristics_doc(name_img)
    # print(my_json)
    check = finguer.verify_footprint(my_json)
    #print(check)
    #check=False
    if(check):
        json_send = {u'emailId': email, u'firstName': firstName}
        val = db.upload_date(json_send)
        #print("pasa")
        if val:
            open(FILE_PASS, "w").write(name_img)
    #open(PID_FILE2, "w").write(name_img)

def prueba():
    db = myfirebase.MyFirebase()
    name_img = "jairo_perez"
    firstName = name_img.split("_")[0]
    email = db.search_email(name_img)
    json_send = {u'emailId': email, u'firstName': firstName}
    val = db.upload_date(json_send)
    if val:
        print("subir")
        
    
    
if __name__ == "__main__":
    main()