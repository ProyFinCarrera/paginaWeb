#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
# 1. Class to do face verification with opencv.
# Finguer. Search for a finger
import time
#from pyfingerprint.pyfingerprint import PyFingerprint
import PyFingerprint

import hashlib

class Footprint:
    def __init__(self):
        # Tries to initialize the sensor
        try:
            self.fingerprint = PyFingerprint(
                '/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if (self.fingerprint.verifyPassword):
                print('Access to the device correct')
            else:
                raise ValueError(
                    'The given fingerprint sensor password is wrong!')
        except Exception as e:
            print('The Footprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

    def read_footprint_pos(self, pos):
        # Wait that finger is read
        while(self.fingerprint.readImage() == False):
            pass
        # Converts read image to characteristics and stores it in charbuffer 1
        self.fingerprint.convertImage(pos)

    def is_footprint(self):
        # Checks if finger is already enrolled
        result = self.fingerprint.searchTemplate()
        position_number = result[0]
        # print('Template already exists at position #' + str(position_number))
        if (position_number >= 0):
            return (True, position_number)
        return (False, -1)

# Saca el num edintificador de la huellade la pocicion pos.
    def is_footprint_equal(self):
            # Compares the charbuffers
        if (self.fingerprint.compareCharacteristics() == 0):
            print('Fingers do not match')
            return False
        return True

    # Saca el num edintificador de la huella de la pocicion pos.
    def id_footprint(self, pos):
        # Loads the found template to charbuffer 1
        self.fingerprint.loadTemplate(pos, 0x01)
        # Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(
            self.fingerprint.downloadCharacteristics(0x01)).encode('utf-8')
        return characterics

    def save_footprint_inside(self):
        # Creates a template
        self.fingerprint.createTemplate()
        # Saves template at new position number
        position_number = self.fingerprint.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(position_number))
        return position_number

    def clear_all(self):
        # Tries to delete the template of the finger
        try:
            for i in range(100):
                print(self.fingerprint.deleteTemplate(i))

            print (str(self.fingerprint.getTemplateCount()))

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)
    # save in divice and return nember hexadecimal
    def save_footprint(self):
        # Tries to enroll new finger
        try:
            self.read_footprint_pos(0x01)
            (to_be, position_number) = self.is_footprint()
            if to_be:
                exit(2)

            time.sleep(2)
            self.read_footprint_pos(0x02)

            if self.is_footprint_equal():
                print("Save footprint")
            else:
                exit(2)

            position_number = self.save_footprint_inside()
            # Footprin put in position 1 buffer.
            self.id_footprint(position_number)
            return str(self.fingerprint.downloadCharacteristics(0x01))
        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)

    def verify_footprint(self):
        try:
            self.read_footprint_pos(0x01)
            (result, pos) = self.is_footprint()
            if(result):
                characterics = str(
                    self.fingerprint.downloadCharacteristics(0x01))
                print( hashlib.sha256(characterics.encode('utf-8')).hexdigest())
                return (result, characterics.encode('utf-8'))

            return (result, -1)
        except Exception as e:
            print('Exception message: ' + str(e))
            exit(1)


aux = Footprint();
# aux.clear_all();
# print aux.save_footprint();
print( aux.verify_footprint())
