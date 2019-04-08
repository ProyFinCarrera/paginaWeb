# esto es una mierda.
# -*- coding: ascii -*-
from secrets import choice

from string import ascii_letters, ascii_uppercase, digits

caracteres = ascii_letters + ascii_uppercase + digits

#longitud = 8# La longitud que queremos
#cadena_aleatoria = ''.join(choice(caracteres) for caracter in range(longitud))
#print("La cadena es: "+ cadena_aleatoria)
"""
Eso también significa que no puede reutilizar un objeto para cifrar o descifrar otros datos con la misma clave.

Esta función no realiza ningún relleno.

Para MODE_ECB , MODE_CBC y MODE_OFB , la longitud del texto sin formato (en bytes) debe ser un múltiplo de block_size .
Para MODE_CFB , la longitud del texto sin formato (en bytes) debe ser un múltiplo de segment_size / 8.
Para MODE_CTR , el texto plano puede ser de cualquier longitud.
Para MODE_OPENPGP , el texto sin formato debe ser un múltiplo de block_size , a menos que sea la última parte del mensaje.
Parámetros:
plaintext (cadena de bytes): el dato a cifrar.
Devoluciones:
Los datos encriptados, como una cadena de bytes. Es tan largo como el texto sin formato con una excepción: al cifrar el primer fragmento de mensaje con MODE_OPENPGP , el IV cifrado se añade al texto cifrado devuelto."""