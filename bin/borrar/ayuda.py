##########encode##########################
# # Genero shas
# messageSha = takeSha("fdasfadsfadsf fa dsfdasfdasfdsafdsf")
# print("Con sha: " + messageSha)
# print len(messageSha)
# # Tranformo con el algoritmo Aeas.
# messageAES = takeAES(messageSha)
# print("Con AES: " + messageAES)

# print("Desencriptar")
# mdesAES = desAES(messageAES)
# print("Con Des: " + mdesAES)
# message = desSha(mdesAES)
# print("Mensaje: " + message.decode('utf-8'))
##########encode##########################

cargar = MyFirebase()
# a = cragar.searchData(u"jairo","aaaa")
data = {
    u'email_id': u'uno@gmail.com',
    u'firstName': u'nameUno'
}
cargar.upload_date(data)
# cargar.searchDate(u'hora', 9)
