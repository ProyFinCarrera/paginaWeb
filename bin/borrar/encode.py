#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
PyFingerprint
Copyright (C) 2019 Jairo Gonzalez Lemus alu0100813272@ull.edu.com
All rights reserved.
"""
from Crypto.Cipher import AES
from io import open 
import hashlib
from Crypto.Hash import SHA256
import os

def tell_me_about(s):
	return (type(s), s)
	
## solo da un numero al raiz de undato
def takeSha(characterics):
    hash = SHA256.new(characterics)
    text = hash.hexdigest()
    return str(text).encode('utf-8')

## leo la clave desde un archivo.txt
def readClave(nameArchive):
    path = 'bin/encode/'+nameArchive
    pathArchive = os.path.abspath(path)
    archive = open(pathArchive, "r") 
    text = archive.read()
    archive.close()
    return text

def takeAES(characterics):
    clave = readClave("clave.txt")
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    return obj.encrypt(characterics)

def desAES(characterics):
    clave = readClave("clave.txt")
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    return obj.decrypt(characterics)

# Genero shas
# messageSha = takeSha("fdasfadsfadsf fa dsfdasfdasfdsafdsf")
# print("Con sha: " + messageSha)
# print len(messageSha)
# # Tranformo con el algoritmo Aeas.
# messageAES = takeAES(messageSha)
# print("Con AES: " + messageAES) 

# print("Desencriptar")

# mdesAES = desAES(messageAES)
# print("Con Des: " + mdesAES) 
# message = desSha(mdesAES)
# print("Mensaje: " + message.decode('utf-8'))



# print "////////////////////////////////////////////"
## v ="esto es  una mierda"
## uv = v.decode("iso-8859-1")
## print v.decode("utf-8")

## if isinstance( s, str ): # BAD: Not true for Unicode strings!
## if isinstance( s, basestring ): # True for both Unicode and byte strings