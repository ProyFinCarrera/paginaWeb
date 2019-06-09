#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File encode.py:
#           1. Unctions that help to encode.
from Crypto.Cipher import AES
from Crypto import Random
import base64
from Crypto.Hash import SHA256
import os

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


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
    characterics = pad(characterics)
    path = os.path.join(PATH_DIR, "clave.txt")
    clave = read_clave(path)
    iv = Random.new().read( AES.block_size )
    #ivThis is an IV456
    obj = AES.new(clave, AES.MODE_CBC, iv)
    aux = obj.encrypt(characterics)
    return base64.b64encode( iv + aux)


def des_aes(characterics):
    path = os.path.join(PATH_DIR, "clave.txt")
    characterics = base64.b64decode(characterics)
    clave = read_clave(path)
    iv = characterics[:16]
    obj = AES.new(clave, AES.MODE_CBC, iv)
    return unpad(obj.decrypt(characterics[16:]))


def tranfor_vector_int(vector_int):
    rt_str = "".join(map(str, vector_int))
    return rt_str


if __name__ == "__main__":
    vect = [3, 1, 79, 47, 127, 0, 255, 254]
    print(tranfor_vector_int(vect))
    cadena = tranfor_vector_int(vect)
    v_Aes = take_aes(cadena)
    print(v_Aes)
    n = des_aes(v_Aes)
    print(n.decode("ASCII"))
    if n.decode("ASCII") == cadena:
        print("Equals")
    else:
        print("No Equals")
