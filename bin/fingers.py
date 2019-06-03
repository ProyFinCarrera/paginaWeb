#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File fingers.py:
# 1. Execution of the fingerprint recognition system.
# 2. Downloading data from firebase to find similarity with other data.
# 3. Registration of date in firebase
# 4. The double identification is verified

import sys
import json
import os
from myfirebase import myfirebase
#from footprint import footprint
PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID_FILE = PATH_DIR + "/tmp/pass.PID"


#finguer = footprint.Footprint()
#name_f = sys.argv[1]
name_img = "nuevo_yo"
db = myfirebase.MyFirebase()

def __main__():
    print("estoy aki"  + name_img)
    my_json = db.vect_charasteristics_doc(name_img)
    if my_json:
        for n in my_json:
            print(n)
            #aux = det_footprint.verify_footprint(vector)
          # if  det_footprint.verify_footprint(vector):
    json_uno = {u'emailId': u"user1@gmail.com", u'firstName': u'user1'}
    
    # si tal escribo y creo
    open(PID_FILE, "w").write(name_img)
    #db.upload_date(json_uno)
    #exit(150)
    #(result, characterics) = finguer.verify_footprint()


__main__()
