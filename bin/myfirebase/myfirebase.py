#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File myfirebase.py:
#           1. Class for upload and download of data in the firebase account.
import json
import time
import os
import firebase_admin
import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import firestore
from uuid import getnode as get_mac

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
# Function that returns the mac of the device where it is running.


def my_mac():
    mac = get_mac()
    mac_aux = ''.join(('%012X' % mac)[i:i + 2]for i in range(0, 12, 2))
    return mac_aux


class Users(object):
    """ Class that manages the users of the database.
        The attributes of the parameter database are passed.
    """

    def __init__(self, emailId, firstName, lastName, nameFile, m_div):
        self.emailId = emailId
        self.firstName = firstName
        self.lastName = lastName
        self.nameFile = nameFile
        self.m_div = m_div

    def get_cout_footprint(self):
        mac = my_mac()
        count = len(self.m_div[mac])
        return count

    def get_email(self):
        return self.emailId

    def vect_characteristics(self):
        """
            Class method that consults the carecteristic vectors
            Returns:
                A document with all the characteristic vector of the user.
        """
        mac = my_mac()
        return self.m_div[mac]

    @staticmethod
    def from_dict(source):
        for doc in source:
            data = doc.to_dict()
            return Users(data['emailId'], data['firstName'],
                         data['lastName'], data['nameFile'], data['m_div'])

    def to_dict(self):
        pass

    def __repr__(self):
        return u'Users( emailId={}, firstName={}, lastName={}, nameFile={})'.format(
            self.emailId, self.firstName, self.lastName, self.nameFile)


class MyFirebase:
    """
        Class that manages the connection to the
        database. I make consultation and store data necessary
        for the system.
    """

    def __init__(self):
        path = os.path.join(PATH_DIR, 'serviceAccountKey.json')
        #path = os.path.join(PATH_DIR, 'doskey.json')
        file = open(path, 'r')
        try:
            self.app = firebase_admin.get_app()
            self.db_fire = firestore.client()
        except ValueError as e:
            with file as f:
                self.conf = json.load(f)

            self.cred = credentials.Certificate(self.conf)
            self.db_admin = admin.initialize_app(self.cred, {
                "storageBucket": "tfg-findegrado.appspot.com",
                "databaseURL": "https://tfg-findegrado.firebaseio.com"
            })
            #self.db_admin = admin.initialize_app(self.cred, {
            #    "storageBucket": "dosjoder-46c0a.appspot.com",
            #    "databaseURL": "https://dosjoder-46c0a.firebaseio.com"
            #})
            self.db_fire = firestore.client()

    def vect_charasteristics_doc(self, nameFile):
        """
            Class method that is responsible for downloading the
            document with all the characteristic vectors of the
            user's footprint.
            Args:
                dir_img: Name of the directory where the user's
                image is saved for recognition.
            Returns:
               A document, False otherwise.
        """
        try:
            user = self.db_fire.collection("users").where(
                u'nameFile', u'==', nameFile).limit(1).stream()
            doc = Users.from_dict(user)
            # print(doc)
            return doc.vect_characteristics()
        except ValueError as e:
            # print("Vectors characteristic not foud")
            return e

    def upload_testUser(self, json):
        try:
            users_collection = self.db_fire.collection(u'users').document()
            users_collection.set(json)
        except Exception as e:
            print('Exception message: ' + str(e))
            return e

    def upload_testMac(self, json):
        try:
            users_collection = self.db_fire.collection(u'device').document()
            users_collection.set(json)
        except Exception as e:
            print('Exception message: ' + str(e))
            return e

    def upload_footprint(self, vect_characteristic, email):
        """ Class method that loads the characteristic vector of
            the footprint in firebase.
            Args:
                verct_characteristic(str): Value of the characteristic
                vector of the footprint previously calculated.
                email(str): Email to search the user.
            Return:
                True if you find a user, false otherwise.
        """
        try:
            mac = my_mac()
            # Reference to the document.
            doc, size = self._search_id_user(email)
            # Update
            # + vect_characteristic.decode("ASCII")
            camp = "m_div." + mac + ".finger" + str(size)
            up_data = {camp: vect_characteristic}

            if(doc == -1):
                # print("User not foud")
                return False
            else:
                # print(up_data)
                # print("Foud user")
                users_collection = self.db_fire.collection(
                    u'users').document(doc)
                users_collection.update(up_data)
                return True
        except Exception as e:
            print('Exception message: ' + str(e))
            return e

    def search_email(self, nameFile):
        try:
            user = self.db_fire.collection("users").where(
                u"nameFile", u"==", nameFile).stream()
            doc = Users.from_dict(user)
            # print(doc)
            return doc.get_email()
        except Exception as e:
            print('Exception message: ' + str(e))
            return (-1)

    def _search_id_user(self, email):
        user = self.db_fire.collection("users").where(
            u"emailId", u"==", email).stream()
        doc_id = -1
        size = 0
        mac = my_mac()
        try:
            for doc in user:
                doc_id = doc.id
                data = doc.to_dict()
                size = len(data['m_div'][mac])
            return (doc_id, size)
        except Exception as e:
            print('Exception message: ' + str(e))
            return (doc_id, size)

    def upload_date(self, json_d):
        """ Method that loads the dates and other values ​​to
           the passVerification collection.
           Args:
                json_d(doc) :  Document with the values ​​of
                emailId and firstname.
            Returns:
                True If it has been loaded in the collection,
                False otherwise.
        """
        up_data = {
            u'timeStamps': time.time(),
            u'day': int(time.strftime('%d')),
            u'month': int(time.strftime('%m')),
            u'nameMonth': time.strftime('%B'),
            u'nameDay': time.strftime('%A'),
            u'year': int(time.strftime('%Y')),
            u'hour': int(time.strftime('%H')),
            u'minute': int(time.strftime('%M')),
            u'mac': my_mac()
        }
        # time.time()
        up = json.dumps(json_d)
        up = json.loads(up)
        # print()
        up_data[u'emailId'] = up[u'emailId']
        up_data[u'firstName'] = up[u'firstName']
        upload = self.db_fire.collection(u'passVerification').document()
        upload.set(up_data)
        return up_data

    def upload_date_test(self, up_data):
        """Method to perform a loading test in the database."""
        upload = self.db_fire.collection(u'passVerification').document()
        upload.set(up_data)


if __name__ == "__main__":
    aux = MyFirebase()
    val = aux.upload_footprint(u'vectordd_cjj', u'dios@gmail.com')
    v = aux.search_email('Ejemplo_ejmpl')
    # print(v)
    # print(val)
    nameFile = "luis_dios"
    my_json = aux.vect_charasteristics_doc(nameFile)
    # print(my_json)
    if my_json:
        for n in my_json:
            print(n)
