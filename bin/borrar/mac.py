#!/usr/bin/python
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Media Access Control es un identificador de 48 bits
# (6 bloques de dos caracteres hexadecimales (4 bits))

from uuid import getnode as get_mac
mac = get_mac()
# Number macc hexa


def my_mac_hexa():
	return hex(mac)


def my_mac():
	mac_aux = ':'.join(('%012X' % mac)[i:i + 2]for i in range(0, 12, 2))
	return mac_aux

print my_mac_hexa()
print my_mac()