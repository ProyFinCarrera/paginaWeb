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
from footprint import footprint
from encode import encode

finguer = footprint.Footprint()
#name_f = sys.argv[1]
name_f = "jairo"
myBd = myfirebase.MyFirebase()
# print("Estoy dentro del fingers.py")


def __main__():
    (result, characterics) = finguer.verify_footprint()
    print characterics
    print result
    # result =True
    if(result):
        num_f = take_num_secret(characterics)
        # num_f=take_num_secret("0231456asdf45s64f66sfs5f64s654f")
        # num_f = u"aaaa"
        aux = double_authentication(name_f, num_f)
        print aux
        if(aux != -1):
            update_all(aux)


def take_num_secret(charasterics):
    message_shas = encode.take_shas(charasterics)
    return encode.take_aes(message_shas)

# check if the user is identified.


def double_authentication(name_f, num_f):
    return myBd.search_data(name_f, num_f)


def update_all(data):
    datajson = myBd.upload_date(data)
    path = os.path.abspath('./../public/infoRegistro/infoR.json')
    modifi_document(datajson, path)


def modifi_document(data, file):
    json_file = open(file, "r+")
    data_json = json.load(json_file)
    data_json['Name'] = data['Name']
    data_json['date'] = data['date']
    data_json['code'] = 1
    # Seguridad delete email_id
    newj_son = open(file, "w+")
    newj_son.write(json.dumps(data_json))


__main__()
