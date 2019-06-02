#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
#   1. Class to do face verification with opencv.
#   Finguer. Search for a finger
import time
import hashlib
from time import clock
if __name__ == "__main__":
  import pyfingerprint
else:
  from footprint.pyfingerprint import PyFingerprint


class Footprint:
      """ Class that will manage the operation of
             fingerpirnt detectro, we will help with the
             pyfingerprint class.
             Attributes:
                 __fingerprint (:obj:PyFingerprint()): Obj that
                 connects with the detector divice
                 __timer_power (float): Time waiting for the
                 recognizer by the finger in seconds. The defaul
                 value is 0.5.
      """

      def __init__( self, timer_power = 5 ):
          try:
            self.__timer_power = timer_power
            self.__fingerprint = pyfingerprint.PyFingerprint(
                '/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if (self.__fingerprint.verifyPassword):
              print('Access to the device correct')
            else:
              raise ValueError(
                  'The given fingerprint sensor password is wrong!')
          except Exception as e:
            print('The Footprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

      def verify_footprint(self, vect_caracteristic):
          """ Tries to enroll new finger. Befor saving ,
             the finger is checked twice. Steps to follow
                       1. Catch finger
                       2. Check if it is inside.
                       3 . si estoy dentro sacar el vecto caracteristico de dentro
                       y compararlo con el k tengo yo
            Returns:
                 True if you are verified by the system. False in otherwise.
          """
          try:
            (rt, pos) = self._read_and_be_inside()  # lo k leo 0x01
            if(rt):
              vect = self.id_footprint(pos, buffer=0x02)  # poxicondonde esta en dos
              print(vect)
              if vect_caracteristic == vect:
                print("Vector Equals")
                return True
              else:
                return False
          except Exception as e:
            print('Exception message: ' + str(e))
            exit(1)

      def save_footprint(self):
        """ Tries to enroll new finger. Befor saving ,
             the finger is checked twice. Steps to follow
                         1. Catch finger
                         2. Check if it is inside.
                         3. Catch finger again.
                         4. If it is verified that you have taken the same finger, you enter the system.
            Returns:
              if you save your finger, it returns it charactgeristic
              vector. False in otherwise.
        """
        try:
          rt = self._read_and_not_be_inside()

          if rt:
            # print("Dedo no dentro")
            time.sleep(2)
            self._read_footprint_pos(0x02)
            if self.is_footprint_equal():
              print("Save footprint")
              position_number = self._save_footprint_inside()
              # Footprin put in position 1 buffer.
              self.id_footprint(position_number)
              return str(self.__fingerprint.downloadCharacteristics(0x01))
            else:
              return False
          else:
            print("Dedos ya dentro")
            return False
        except Exception as e:
          print('Operation failed!')
          print('Exception message: ' + str(e))
          exit(1)

      def clear_all_footprint(self):
        """ Remove all fingers from the divece"""
        self.__fingerprint.clearDatabase()

      def _read_and_be_inside(self):
        read = self._read_footprint_pos(0x01)
        (check, pos) = self._check_if_inside()
        if(read and check):
          return (True, pos)
        else:
          return (False, -1)

      def _read_and_not_be_inside(self):
        if(self._read_footprint_pos(0x01) and
           (self._check_if_inside()[0] == False)):
          return True
        else:
          return False

      def _read_footprint_pos(self, pos):
        # Wait that finger is read
        wait = True
        while (wait and (self.__fingerprint.readImage() == False)):
          b = clock()
          print(b)
          if self.__timer_power - b <= 0:
            wait = False
        # Converts read image to characteristics and stores it in charbuffer 1
        if self.__fingerprint.readImage():
          self.__fingerprint.convertImage(pos)
          return True
        else:
          return False

      def _check_if_inside(self):
        # Checks if finger is already enrolled
        result = self.__fingerprint.searchTemplate()
        position_number = result[0]
        # print('Template already exists at position #' + str(position_number))
        if (position_number >= 0):
          return (True, position_number)
        return (False, -1)

      def is_footprint_equal(self):
        # Compares the charbuffers
        if (self.__fingerprint.compareCharacteristics() == 0):
          print('Fingers do not match')
          return False
        return True

      # Saca el num edintificador de la huella de la pocicion pos.
      def id_footprint(self, pos, buffer=0x01):
        # Loads the found template to charbuffer 1
        self.__fingerprint.loadTemplate(pos, buffer)
        # Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(
            self.__fingerprint.downloadCharacteristics(buffer)).encode('utf-8')
        print(hashlib.sha256(characterics.encode('utf-8')).hexdigest())
        return characterics

      def _save_footprint_inside(self):
        # Creates a template
        self.__fingerprint.createTemplate()
        # Saves template at new position number
        position_number = self.__fingerprint.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(position_number))
        return position_number


if __name__ == "__main__":
  aux = Footprint()
  # aux.clear_all_footprint();
  # introducto huella.
  # Saco vector caracteristico.
  vec_aux = aux.save_footprint()
  print(vec_aux)
  # mto nuevo dedo y verifico el vecto caracteritico.
  # con el vector carateristico veo si esta dentro
  time.sleep(3)
  print(aux.verify_footprint(vec_aux))
