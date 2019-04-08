#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File encode.py:
#           1. Unctions that help to encode.
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os


def take_sha_hex(characterics):
    hash = SHA256.new(characterics)
    text = hash.hexdigest()
    return str(text).encode('utf-8')

def read_clave(name_archive):
    archive = open(name_archive, 'r')
    text = archive.read()
    archive.close()
    return text

def take_aes(characterics):
    path = os.path.abspath("encode/clave.txt")
    clave = read_clave(path)
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    # print (obj)
    aux = obj.encrypt(characterics)
    print(aux.encode('hex'))
    return aux


def des_aes(characterics):
    path = os.path.abspath("encode/clave.txt")
    clave = read_clave(path)
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    return obj.decrypt(characterics)