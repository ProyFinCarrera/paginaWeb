from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

input_file = open("input.jpg")
input_data = input_file.read()
input_file.close()

cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
enc_data = cfb_cipher.encrypt(input_data)

enc_file = open("encrypted.enc", "w")
enc_file.write(enc_data)
enc_file.close()


enc_file2 = open("encrypted.enc")
enc_data2 = enc_file2.read()
enc_file2.close()

cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
plain_data = cfb_decipher.decrypt(enc_data2)

output_file = open("output.jpg", "w")
output_file.write(plain_data)
output_file.close()