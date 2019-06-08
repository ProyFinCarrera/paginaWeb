#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File encode.py:
#           1. Unctions that help to encode.
from Crypto.Cipher import AES
import base64
from Crypto.Hash import SHA256
import os

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
BS = 16
pad = lambda s:s+(BS-len(s) % BS)* chr(BS- len(s) % BS)
unpad = lambda s:s[:-ord(s[len(s)-1:])]

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
    characterics=pad(characterics)
    path = os.path.join(PATH_DIR,"clave.txt")
    clave = read_clave(path)
    
    print(clave)
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    #print (obj)
    aux = obj.encrypt(characterics)
    return base64.b64encode(aux)


def des_aes(characterics):
    path = os.path.join(PATH_DIR,"clave.txt")
    characterics=  base64.b64decode(characterics)
    clave = read_clave(path)
    obj = AES.new(clave, AES.MODE_CBC, 'This is an IV456')
    return unpad(obj.decrypt(characterics)).decode("ASCII")



def tranfor_vector_int(vector_int):
    rt_str = "".join(map(str,vector_int))
    return rt_str



if __name__ == "__main__":
    vect = [3, 1, 79, 47, 127, 0, 255, 254, 252, 126, 248, 62, 240, 62, 224, 62, 192, 6, 192, 6, 192, 6, 192, 2, 192, 2, 192, 2, 192, 2, 192, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 34, 108, 254, 82, 170, 19, 126, 82, 178, 170, 94, 64, 191, 65, 190, 8, 64, 95, 254, 25, 65, 147, 30, 17, 195, 195, 30, 62, 31, 168, 223, 26, 169, 193, 215, 22, 56, 194, 119, 104, 64, 24, 247, 58, 151, 229, 252, 65, 174, 235, 92, 83, 183, 192, 60, 41, 63, 2, 124, 88, 64, 67, 29, 83, 66, 4, 61, 58, 14, 99, 90, 61, 178, 44, 250, 104, 58, 67, 250, 57, 148, 164, 219, 78, 22, 11, 59, 101, 54, 235, 59, 95, 56, 44, 91, 90, 186, 66, 123, 63, 9, 163, 120, 73, 153, 144, 152, 73, 156, 100, 216, 58, 186, 193, 152, 89, 27, 103, 121, 61, 182, 1, 121, 45, 15, 164, 118, 50, 146, 35, 182, 82, 156, 101, 118, 81, 162, 146, 240, 76, 36, 41, 112, 41, 153, 151, 215, 75, 162, 148, 87, 85, 35, 168, 119, 59, 56, 151, 183, 47, 61, 24, 183, 42, 149, 164, 117, 33, 160, 153, 111, 38, 44, 130, 21, 43, 174, 129, 21, 69, 138, 143, 50, 41, 176, 25, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 84, 50, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 138, 97, 222, 97, 15, 34, 190, 31, 144, 95, 62, 40, 146, 158, 222, 107, 150, 227, 158, 96, 48, 82, 126, 52, 144, 159, 95, 48, 168, 42, 63, 38, 45, 192, 223, 51, 50, 23, 223, 112, 50, 167, 95, 85, 194, 84, 95, 93, 160, 228, 190, 39, 156, 192, 31, 53, 182, 107, 255, 94, 36, 230, 30, 78, 47, 232, 62, 76, 190, 41, 254, 58, 135, 224, 63, 79, 59, 212, 127, 49, 60, 44, 126, 47, 151, 32, 95, 23, 183, 194, 31, 44, 153, 30, 28, 48, 154, 98, 125, 24, 194, 2, 61, 40, 69, 129, 29, 47, 58, 151, 187, 120, 133, 12, 59, 70, 177, 105, 89, 60, 159, 165, 214, 80, 29, 36, 78, 85, 54, 233, 14, 57, 169, 233, 15, 101, 45, 38, 207, 80, 29, 35, 206, 88, 43, 209, 111, 28, 32, 68, 110, 29, 34, 220, 142, 30, 139, 200, 206, 23, 46, 67, 142, 8, 37, 197, 174, 17, 45, 195, 175, 54, 9, 159, 109, 51, 4, 138, 172, 63, 130, 159, 75, 69, 3, 33, 139, 25, 62, 155, 74, 51, 135, 224, 9, 82, 181, 83, 38]
    print(tranfor_vector_int(vect))
    cadena =tranfor_vector_int(vect)
    v_Aes = take_aes(cadena)
    print()
    n = des_aes(v_Aes)
    print(n)
    if str(n) == cadena:
        print("Si es igual")
    else:
        print("No es igula")