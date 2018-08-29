import hashlib

#######
contrasena = 'gatito'
clave = hashlib.sha256(contrasena)
print(clave)
claveSha = clave.hexdigest()
print(claveSha);
################################

declave = clave.update("datoooooo")
print(declave)