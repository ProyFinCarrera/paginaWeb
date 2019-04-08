from Crypto.Cipher import AES

key = '0123456789abcdef'
IV = 16 * '\x00'           # Initialization vector: discussed later
print IV
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'j' * 64 + 'i' * 128
print text
ciphertext = encryptor.encrypt(text)
print ciphertext

import hashlib

password = 'kitty'
key = hashlib.sha256(password).digest()
print key

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)
print plain


from Crypto.Util import Counter
pt = b''*1000000
ctr = Counter.new(128)
print ctr
cipheraa = AES.new(b'dsf'*16, AES.MODE_CTR, counter=ctr)
ct = cipheraa.encrypt(pt)