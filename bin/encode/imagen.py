
# esto es una mierda.
# -*- coding: ascii -*-
from Crypto.Cipher import AES
from Crypto import Random
import Crypto.Random 
#  modulo mas seguor de rando

class Encode:
    def __init__(self):
    	print AES.key_size
        # self.__key = Random.new().read(AES.block_size)
        key = self.__read_file("key/footprint.key")
        print key
        self.__key = Crypto.Random.new().read(AES.block_size)
        # print str(self.__key )
        self.__key = Crypto.Random.get_random_bytes(AES.block_size)
        print str(self.__key )

        #self.__key = Crypto.Random.getrandbits(AES.block_size)
        print str(self.__key )

        self.__iv = Random.new().read(AES.block_size)
        # print self.__iv
        self.__cipher = AES.new(self.__key, AES.MODE_CFB, self.__iv)
        self.__cipher2 = AES.new(self.__key, AES.MODE_CFB, self.__iv)

    def decrypt_imagen(self, enc_file, dec_file):
        enc_data = self.__read_file(enc_file)
        dec_data = self.__cipher2.decrypt(enc_data)
        self.__save_imagen(dec_file, dec_data)

    def encrypt_imagen(self, filename, enc_file):
        data_img = self.__read_file(filename)
        enc_data = self.__cipher.encrypt(data_img)
        self.__save_imagen(enc_file, enc_data)

    def __read_file(self, filename):
        input_file = open(filename)
        data_img = input_file.read()
        input_file.close()
        return data_img

    def __save_imagen(self, filename, data):
    	enc_file = open(filename, "w")
        enc_file.write(data)
        enc_file.close()



nuevo = Encode()
nuevo.encrypt_imagen("input.jpg","encrypted.enc")
nuevo.decrypt_imagen("encrypted.enc","output.jpg")