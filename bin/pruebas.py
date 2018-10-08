from Crypto.Cipher import AES
from io import open 
import hashlib
from Crypto.Hash import SHA256
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
    clave = readClave("clave.txt")
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    return obj.encrypt(characterics)

def desAES(characterics):
    clave = readClave("clave.txt")
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    return obj.decrypt(characterics)
## Tries to search the finger and calculate hash
try:
    
    ####################### Search Imagen en firebase.

        ## Loads the found template to charbuffer 1
    f.loadTemplate(2, 0x01)

    ## Downloads the characteristics of template loaded in charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
    
    # Paso genro shas
    messageSha = takeSha(characterics)
    print(messageSha)
    
    # Tranformo con el algoritmo Aeas.
    messageAES = takeAES(messageSha)
    print(messageAES)##EStoy es lo que hay k mandar.
    ####################busco la imagen messageAes.png###########################################




    ################################################################
    # takeShas y desigrado son iguales
    descifrado = desAES(messageAES)
    print(descifrado)

    # Nota si el shas que se genrea l huella Tengo k encriptar sha


except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)
