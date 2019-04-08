from pyfingerprint.pyfingerprint import PyFingerprint

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)
## Tries to delete the template of the finger
try:
    for i in range(100):
   		print f.deleteTemplate(i)

    print str(f.getTemplateCount())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)


        # Gets some sensor information
        # print('Currently used templates: ' + str(self.__fingerprint.getTemplateCount()
        #                                          ) + '/' + str(self.__fingerprint.getStorageCapacity()))

        # # Tries to show a template index table page
        # try:
        #     for page in range(4):
        #         tableIndex = self.__fingerprint.getTemplateIndex(page)
        #         print ('Page:' + str(page))
        #         for i in range(0, len(tableIndex)):

        #             if(tableIndex[i]):
        #                 self.__fingerprint.deleteTemplate(i)
        #                 print('Template at position #' + str(i) +
        #                       ' is used: ' + str(tableIndex[i]) + "Delete Templete")

        # except Exception as e:
        #     print('Operation failed!')
        #     print('Exception message: ' + str(e))
        #     exit(1)