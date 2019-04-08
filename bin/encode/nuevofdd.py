from Crypto.Cipher import AES
from Crypto import Random


class Encode:
	def __init__(self):
		self.__key = Random.new().read(AES.block_size)
		self.__iv = Random.new().read(AES.block_size)
		self.__cipher = AES.new(key, AES.MODE_CFB, iv)

	def decrypt_imagen(self, enc_file, dec_file):
		enc_data = self.__read_file(enc_file)
    	dec_data = self.__cipher.decrypt(enc_data)
    	self.__save_imagen(dec_file, dec_data)

    def encrypt_imagen(self, filename, enc_file):
    	data_img = self.__read_file(filename)
    	enc_data = self.__cipher.encrypt(data_img)
    	self.__save_data(enc_file, enc_data)  

    def __read_file(self, filename):
    	input_file = open(filename)
    	data_img = input_file.read()
        input_file.close()
        return data_img

    def __save_imagen(self, filename,data):
    	enc_file = open(filename, "w")
        enc_file.write(data)
        enc_file.close()



nuevo = Encode()
nuevo.encrypt_imagen("input.jpg","dale.ecr")