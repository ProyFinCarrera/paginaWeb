from PIL import Image
 
foto = Image.open('dedo.jpg')
 
datos = list(foto.getdata())
print datos
 
'''la linea anterior tambien podria escribirse como:
 
datos = list(Image.Image.getdata(foto))'''
 
#al finalizar cerramos el objeto instanciado
 