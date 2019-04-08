import time
import datetime
print time.time # valor desimal
print time.strftime('%H:%M:%S')
print time.strftime('%I:%M:%S')
print time.strftime('%d/%m/%y')
print time.strftime('%d/%m/%Y')
print time
formato = "%c"
print time.strftime(formato + "este es el mejor \%\c")
formato = "%x"
print time.strftime(formato)
formato = "%X"
print time.strftime(formato)

ahora= datetime.datetime.now()
print(ahora)
print(ahora.minute)
print(ahora.month)
print(ahora.year)
print(datetime.date.today().year)

fecha = "21/01/1991" # string
fecha = datetime.datetime.strptime(fecha,"%d/%m/%Y")

fecha = fecha + datetime.timedelta(days=3)
print(fecha)
fecha = fecha + datetime.timedelta(days=3,weeks=1,hours=1)
print(fecha)

