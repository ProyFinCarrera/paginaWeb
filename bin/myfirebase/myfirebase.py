#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File myfirebase.py:
#           1. Class for upload and download of data in the firebase account.
import json
import time
import os
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import firestore
from uuid import getnode as get_mac


def my_mac():
    mac = get_mac()
    mac_aux = ':'.join(('%012X' % mac)[i:i + 2]for i in range(0, 12, 2))
    return mac_aux


class MyFirebase:
    def __init__(self):
        # path = os.path.abspath('serviceAccountKey.json')

        path = os.path.abspath('myfirebase/serviceAccountKey.json')
        # print(path)
        file = open(path, 'r')
        with file as f:
            self.conf = json.load(f)

        self.cred = credentials.Certificate(self.conf)
        self.db_admin = admin.initialize_app(self.cred, {
            "storageBucket": "tfg-findegrado.appspot.com",
            "databaseURL": "https://tfg-findegrado.firebaseio.com"
        })
        self.db_fire = firestore.client()
    # Search data with nameF equals NameF and datoC equals val.

    # def search_data(self, name_f, val):
    #     users_collection = self.db_fire.collection(u'users')
    #     snapshot = users_collection.where(u"nameF", u"==", name_f.decode(
    #         "utf-8")).where(u"dataC", u"==", val).get()
    #     for n in snapshot:
    #         s = n.to_dict()
    #         return s
    #     return -1

    # Search data with nameF equals NameF and datoC equals val.
    def search_data_in_users(self, data, val):
        print "Antes"
        users_collection = self.db_fire.collection(u'passVerification')
        print "Antes"
        snapshot = users_collection.where(data, u"==", val).get()
        for n in snapshot:
            s = n.to_dict()
            print s
        return -1

    # Search data with nameF equals NameF and datoC equals val.
    def search_dates(self, data, val):
        print "Antes"
        users_collection = self.db_fire.collection(u'passVerification')
        print "Antes"
        snapshot = users_collection.where(data, u"==", val).get()
        for n in snapshot:
            s = n.to_dict()
            print s
        return -1

    def upload_footprint(self, id_footprint, email):
        mac = my_mac().decode('utf-8')
        #mac = my_mac().encode('hex')

        doc = self.search_id_user(email)
        # Update
        camp = id_footprint + "." + mac
        up_data = {camp: True}

        if(doc == -1):
            print("No se ha encontrado usuario")
        else:
            print("Usuario encontrado")
            print(doc)
            users_collection = self.db_fire.collection(u'users').document(doc)
            users_collection.update(up_data)

    def search_id_user(self, email):
        user = self.db_fire.collection("users").where(
            u"emailId", u"==", email.decode("utf-8")).get()
        # id
        for doc in user:
            return (doc.id)
        return -1
        # print(u'{} => {}'.format(doc.id, doc.to_dict()))

    def upload_date(self, json_d):
        up_data = {
            u'timeStamps': time.time(),
            u'day': int(time.strftime('%d')),
            u'month': int(time.strftime('%m')),
            u'nameMonth': time.strftime('%B').decode('utf-8'),
            u'nameDay': time.strftime('%A').decode('utf-8'),
            u'year': int(time.strftime('%Y')),
            u'hour': int(time.strftime('%H')),
            u'minute': int(time.strftime('%M')),
            u'mac': my_mac().decode('utf-8')
        }
        # time.time()
        up = json.dumps(json_d)
        up = json.loads(up)
        print
        up_data[u'emailId'] = up[u'emailId']
        up_data[u'firstName'] = up[u'firstName']
        upload = self.db_fire.collection(u'passVerification').document()
        upload.set(up_data)
        return up_data

    def upload_date_test(self, json_d, day, month, year, hour, minute):
        up_data = {
            u'timeStamps': time.time(),
            u'day': day,
            u'month': month,
            u'nameMonth': time.strftime('%B').decode('utf-8'),
            u'nameDay': time.strftime('%A').decode('utf-8'),
            u'year': int(time.strftime('%Y')),
            u'hour': int(time.strftime('%H')),
            u'minute': int(time.strftime('%M')),
            u'mac': my_mac().decode('utf-8')
        }
        up = json.dumps(json_d)
        up = json.loads(up)
        print
        up_data[u'emailId'] = up[u'emailId']
        up_data[u'firstName'] = up[u'firstName']
        upload = self.db_fire.collection(u'passVerification').document()
        upload.set(up_data)
        return up_data


# aux = MyFirebase()
# aux.upload_footprint(u'id_footprint', u'soy_yo000@hotmail.com')

# json_uno = {u'emailId': u"user1@gmail.com",
#             u'firstName': u'user1'}
# json_dos = {u'emailId': u"user2@gmail.com",
#             u'firstName': u'user2'}
# json_tres = {u'emailId': u"user3@gmail.com",
#              u'firstName': u'user3'}
# json_cuatro = {u'emailId': u"user4@gmail.com",
#                u'firstName': u'user4'}
# json_cinco = {u'emailId': u"user5@gmail.com",
#               u'firstName': u'user5'}

# for i in range(10):
#     aux.upload_date(json_uno)
#     aux.upload_date(json_dos)
#     aux.upload_date(json_tres)
#     aux.upload_date(json_cuatro)
#     aux.upload_date(json_cinco)
