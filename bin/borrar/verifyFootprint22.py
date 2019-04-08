#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

PyFingerprint. Search for a finger
"""
from pyfingerprint.pyfingerprint import PyFingerprint

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)
## Tries to search the finger and calculate hash
try:
    ## print('Waiting for finger...')
    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass
    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)
    ## Searchs template
    result = f.searchTemplate()
    positionNumber = result[0]
    accuracyScore = result[1]
    if ( positionNumber == -1 ):
        print('No match found!')
        exit(2)
    else:
        print('Found template at position #' + str(positionNumber))
        print('The accuracy score is: ' + str(accuracyScore))
	
    print("Intengo buscar la imagen y la gustro en un archivo") 
    ####################### Search Imagen en firebase.

    ## Loads the found template to charbuffer 1
    f.loadTemplate(positionNumber, 0x01)

    ## Downloads the characteristics of template loaded in charbuffer 1
   ## Downloads the characteristics of template loaded in charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
    
    # Paso genro shas
    messageSha = takeSha(characterics)
    print(messageSha)
    
    # Tranformo con el algoritmo Aeas.
    messageAES = takeAES(messageSha)
    print(messageAES)##EStoy es lo que hay k mandar.
    ####################busco la imagen messageAes.png en firebase###########################################
    

    ################################################################
    # takeShas y desigrado son iguales
    
    descifrado = desAES(messageAES)
    print(descifrado)

    # Nota si el shas que se genrea l huella Tengo k encriptar sha
except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

