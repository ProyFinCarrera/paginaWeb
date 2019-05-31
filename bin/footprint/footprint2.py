
# esto es una mierda.
# -*- coding: ascii -*-
"""Class Footprint
  Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
  File face.py :
  1. Class to do face verification with opencv.
  Finguer. Search for a fingerv
"""
from  footprint.pyfingerprint import PyFingerprint
import hashlib
from time import clock


class Footprint:
    def __init__(self, timer_power=0.05):
        """Example function with PEP 484 type annotations.
        Args:
            timer_power: Configurate tieme wait for finger.
'/dev/ttyUSB0'
         """
        try:
            self.__fingerprint = PyFingerprint(
               'COM3' , 57600, 0xFFFFFFFF, 0x00000000)
            if (self.__fingerprint.verifyPassword):
                self.__timer_power = timer_power
                print('Access to the device correct')
            else:
                raise ValueError(
                    'The given fingerprint sensor password is wrong!')
        except Exception as e:
            print('The Footprint sensor could not be initialized!')
            print('E__catch_footprint_img(xception message: ' + str(e))
            exit(1)

    def dowload(self):
        #imageDestination =  tempfile.gettempdir() + '/fingerprint.bmp'
        imageDestination =  '/fingerprint.bmp'
        self.__fingerprint.downloadImage("./dedo.jpg")
        print('The image was saved to "' + imageDestination + '".')
    
    def on(self):
        """ On cath de fingher and the vector carasteristic.
            Return a vector caracteristic.
        """
        characterics = self.__catch_vect_characterics()
        # return characterics
        if(characterics):
            # borro lo k hay dentro y listo. se hiso en catthc_:ve
            # return hashlib.sha256(characterics).hexdigest()
            return characterics
        else:
            return -1

    def recognize(self, vect):
        finger = self.on()

        print(finger)
        aux = hashlib.sha256(finger).hexdigest()
        print(aux)
        # Saves template at new position number
        pos = self.__fingerprint.storeTemplate()
        
        ## Downloads the characteristics of template loaded in charbuffer 1
        print(pos)
        characterics = self.__fingerprint.downloadCharacteristics(0x01)

        # finger_old = vect +
        date = self.__compare(vect)
        # borrar el dedo del sistema
        return date

    def __compare(self, vect1):
        # self.__fingerprint.uploadCharacteristics(0x01, vect1) # esta el dedo en pa posicion1
        self.__fingerprint.uploadCharacteristics(0x02, vect1)
        aux = self.__fingerprint.compareCharacteristics()
        print(aux)

    def clear_all_footprint(self):
        self.__fingerprint.clearDatabase()

    def __catch_vect_characterics(self):
        # Converts read image to characteristics and stores it in charbuffer 1
        try:
            if self.__catch_footprint_img():
                self.__fingerprint.convertImage(0x01)

                # Creates a template
                print(self.__fingerprint.createTemplate())
                # Saves template at new position number
                # pos = self.__fingerprint.storeTemplate()
                # print pos

                characterics = self.__fingerprint.downloadCharacteristics(0x01)
                # print len(characterics)
                # self.__fingerprint.loadTemplate(pos, 0x01) # estoy hay k hacerlo ?
                subs = characterics[256:512]
                sub = characterics[0:255]

                # print str(sub)
                ## return characterics
                return str(sub).encode('utf-8')
            else:
                return 0
        except Exception as e:
            print('E__catch_vec_characterics(xception message: ' + str(e))
            exit(1)

    def __catch_footprint_img(self):
        wait = True
        while (wait):
            b = clock()
            # print b
            if self.__timer_power - b <= 0:
                wait = False
            if self.__fingerprint.readImage():
                wait = False
        return self.__fingerprint.readImage()
    
    def testTres(self):
        print(self.__fingerprint.generateRandomNumber())
    
    def test(self):
        self.__fingerprint.loadTemplate(5, 0x01)
        self.__fingerprint.loadTemplate(22, 0x02)
        aux = self.__fingerprint.compareCharacteristics()
        print(aux)

    def testdos(self, vect):
        self.__fingerprint.uploadCharacteristics(0x01, vect)
        # self.__fingerprint.loadTemplate(5, 0x01)
        self.__fingerprint.loadTemplate(22, 0x02)
        aux = self.__fingerprint.compareCharacteristics()
        print(aux)


nuevo = Footprint()
#catch= nuevo.on()
# print catch

#vect = [3, 1, 94, 33, 123, 0, 224, 62, 128, 30, 0, 30, 0, 30, 0, 30, 0, 14, 0, 14, 0, 6, 0, 6, 0, 6, 0, 6, 128, 6, 128, 6, 128, 6, 128, 6, 128, 14, 192, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 135, 38, 30, 66, 9, 231, 94, 54, 146, 39, 62, 48, 33, 80, 222, 77, 43, 140, 254, 80, 49, 200, 190, 46, 187, 203, 30, 44, 66, 202, 182, 74, 141, 232, 31, 27, 17, 167, 223, 55, 150, 145, 127, 19, 155, 233, 63, 33, 28, 17, 255, 33, 32, 103, 223, 85, 32, 80, 63, 15, 39, 144, 191, 60, 169, 142, 95, 48, 171, 206, 255, 74, 184, 135, 159, 96, 185, 69, 215, 58, 186, 201, 127, 38, 60, 204, 223, 66, 185, 72, 92, 81, 61, 157, 218, 88, 48, 72, 59, 102, 50, 93, 59, 84, 188, 6, 59, 97, 168, 139, 184, 99, 170, 138, 56, 92, 157, 233, 185, 94, 176, 133, 23, 97, 47, 225, 212, 96, 36, 205, 245, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 #       0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 98, 24, 126, 0, 255, 254, 255, 254, 224, 62, 128, 30, 0, 30, 0, 14, 0, 14, 0, 14, 0, 6, 0, 6, 0, 6, 128, 6, 128, 2, 128, 6, 192, 6, 192, 6, 192, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 69, 142, 167, 126, 12, 149, 16, 54, 57, 150, 103, 94, 27, 161, 168, 30, 53, 165, 144, 30, 22, 175, 143, 254, 107, 176, 207, 94, 56, 50, 13, 254, 83, 50, 12, 126, 27, 67, 77, 150, 77, 19, 40, 223, 30, 150, 103, 95, 59, 26, 145, 31, 66, 47, 13, 159, 101, 183, 6, 119, 66, 193, 202, 87, 53, 194, 75, 55, 92, 66, 197, 247, 84, 63, 74, 188, 75, 64, 73, 28, 37, 36, 167, 26, 87, 184, 72, 218, 37, 162, 16, 216, 92, 183, 71, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# nuevo.test()
#nuevo.testdos(vect)
print( "fin")
# nuevo.testTres()
#nuevo.recognize(vect)
# nuevo.dowload()
#nuevo.clear_all_footprint()

# nuevo.clear_buffer()
