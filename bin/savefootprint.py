#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Save footprin in the sistem.
# 2. Code footprint
# 3. Take mac from the device
# 4. Upload the information to firebase.
from encode import encode
from myfirebase import myfirebase
from footprint import footprint
import hashlib
import sys

if ( sys.argv[0]):
 email = sys.argv[0]
else:
	email =""

print("Estoy aki dentro")

new_footprint = footprint.Footprint()
characterics = new_footprint.save_footprint()

caract_shas = encode.take_sha_hex(characterics)

# caract_shas ="533b6ef334f4ae34bc336e7695f84fad7a282e10b0f6208c881e6e7b7fdcabdf"
print(type(caract_shas))
# print('SHA-2 hash of template: ' + hashlib.sha256(caract_shas).hexdigest())
caract_aes = encode.take_aes(caract_shas) ##estas en hexadecimal

myBd = myfirebase.MyFirebase()
a = u"soy_yo000@hotmail.com" 
myBd.upload_footprint(caract_shas, email)

print("Footprint save with successful")
# messageAES = encode.des_aes(caract_aes)
# print(messageAES)

# print(aux)
