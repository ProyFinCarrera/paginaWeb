#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File face.py:
#   1. Class to do face verification with opencv.
#   Finguer. Search for a finger
import time
from time import clock

if __name__ == "__main__":
  import pyfingerprint
  from codify import codify
else:
  from footprint import pyfingerprint
  from footprint.codify import codify


class Footprint:
        """ Class that will manage the operation of
             fingerpirnt detectro, we will help with the
             pyfingerprint class.
             Attributes:
                 __fingerprint (:obj:PyFingerprint()): Obj that
                 connects with the detector divice
                 __timer_power (float): Time waiting for the
                 recognizer by the finger in seconds. The defaul
                 value is 0.1
          """
        def __init__(self, timer_power = 15):        
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
               raise e
        
        def verify_footprint(self, json_v_caracteristic):
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
              aux = self._read_footprint_buffer(0x01)
              if aux:
                  aux = self._read_footprint_buffer(0x02)
                  if self.is_footprint_equal():
                      (check, pos) = self._check_if_inside()
                      if check:
                          vect = self.id_footprint(pos, buffer=0x01).decode("ASCII")  # poxicondonde esta en do
                          vect_aux = codify.des_aes(vect).decode("ASCII")
                          #print(vect_aux)
                          #print()
                          for aux_v in json_v_caracteristic:
                              vect_aux2 = codify.des_aes(json_v_caracteristic[aux_v]).decode("ASCII")
                              # print(vect_aux2)
                              if vect_aux2 == vect_aux:
                                print("Vector Equals")
                                return True
                      else:
                          # print("Estoy fuera")
                          return False
                  else:
                      return False
              else:
                  return False
            except Exception as e:
              print('Exception message: ' + str(e))
              raise e
            
        def save_footprint(self):
            """ Tries to enroll new finger. Befor saving ,
                 the finger is checked twice. Steps to follow
                             1. Catch finger
                             2. Check if it is inside.
                             3. Catch finger again.
                             4. If it is verified that you have
                             taken the same finger, you enter the system.
                Returns:
                  if you save your finger, it returns it charactgeristic
                  vector. False in otherwise.
            """
            try:
              aux = self._read_footprint_buffer(0x01)
              if aux:
                  aux = self._read_footprint_buffer(0x02)
                  if self.is_footprint_equal():
                      (check, pos) = self._check_if_inside()
                      if check == False:
                          position_number = self._save_footprint_inside()
                          vect = self.id_footprint(position_number, buffer=0x01)
                          return (True, vect.decode("ASCII"))
                      else:
                         return (False, 3) # is inside
                  else:
                    return (False, 2) # footprin no equal
              else:
                  return (False, 2) # footprin no equal
            except Exception as e:
              print('Operation failed!')
              print('Exception message: ' + str(e))
              raise e
          
              
        
        def clear_all_footprint(self):
            """ Remove all fingers from the divece"""
            self.__fingerprint.clearDatabase()

        def del_footprint(self, json_v_caracteristic):
              # print(json_v_caracteristic)
            size = self.__fingerprint.getTemplateCount()
            for pos in range(0, size):
              vect = self.id_footprint(pos, buffer=0x02)
              for aux_v in json_v_caracteristic:
                if aux_v == vect:
                  # print("Delete foorprint: " + str(pos))
                  self.__fingerprint.deleteTemplate(pos)

        def _read_and_not_be_inside(self):
            (check, pos) = self._read_and_be_inside()
            if(check):
              return False
            else:
              return True

        def _read_footprint_buffer(self, buffer):
           # Wait that finger is read
            wait = False
            read = False
            time_a = 0
            while (wait == False):
              wait = self.__fingerprint.readImage()
              if(wait):
                read = True
              if time_a >= self.__timer_power:
                 wait = True
              time_a+=1
            # Converts read image to characteristics and stores it in charbuffer 1
            if (read):
              self.__fingerprint.convertImage(buffer)
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
            characterics = self.__fingerprint.downloadCharacteristics(buffer)
            return codify.take_aes(codify.tranfor_vector_int(characterics))

        def _save_footprint_inside(self):
            # Creates a template
            self.__fingerprint.createTemplate()
            # Saves template at new position number
            position_number = self.__fingerprint.storeTemplate()
            # print('Finger enrolled successfully!')
            # print('New template position #' + str(position_number))
            return position_number


if __name__ == "__main__":
  aux = Footprint()
  aux.clear_all_footprint();
  #check , vec_aux = aux.save_footprint()
  #print (vec_aux)
  # aux.del_footprint({vec_aux:vec_aux})
  # introducto huella.
  # Saco vector caracteristico.
  # check , vec_aux = aux.save_footprint()
  # print(vec_aux)
  # mto nuevo dedo y verifico el vecto caracteritico.
  # con el vector carateristico veo si esta dentro
  # time.sleep(3)
  # vec_aux = {"41436bec58e9c5381d9e8f8e23a38f4bf988f98e57febe10f7e208ab87734708"}
  # print(aux.verify_footprint(vec_aux))
