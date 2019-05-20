#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
PyFingerprint
Copyright (C) 2019 Jairo Gonzalez Lemus alu0100813272@ull.edu.com
All rights reserved.

"""
import time
from Crypto.Cipher import AES
from io import open 
import hashlib
from Crypto.Hash import SHA256
from pyfingerprint.pyfingerprint import PyFingerprint

print("Estoy en saveFootprint.py")
## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

def takeSha(characterics):
    hash = SHA256.new(characterics)
    text = hash.hexdigest()
    return str(text).encode('utf-8')

## leo la clave desde un archivo.txt
def readClave(nameArchive):
    archive = open(nameArchive, "r") 
    text = archive.read()
    archive.close()
    return text

def takeAES(characterics):
    #clave = readClave("clave.txt")
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    return obj.encrypt(characterics)

def desAES(characterics):
    #clave = readClave("clave.txt")
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    return obj.decrypt(characterics)
## Tries to enroll new finger
try:
    print('Waiting for finger...')
    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass
    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)
    ## Checks if finger is already enrolled
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        print('Template already exists at position #' + str(positionNumber))
        exit(2)

    time.sleep(2)

    ## Wait that finger is read again
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 2
    f.convertImage(0x02)

    ## Compares the charbuffers
    if ( f.compareCharacteristics() == 0 ):
    	print('Fingers do not match')
    	exit(2)
       

    ## Creates a template
    f.createTemplate()
    ## Saves template at new position number
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully!')
    print('New template position #' + str(positionNumber))
    
    ## Loads the found template to charbuffer 1
    f.loadTemplate(positionNumber, 0x01)
    ## Downloads the characteristics of template loaded in charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
    print characterics;
    # Genero shas
    messageSha = takeSha(characterics)
    print(messageSha)
    # Tranformo con el algoritmo Aeas.
    messageAES = takeAES(messageSha)
    print(messageAES)

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)