# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

# Recuerda importar Path del módulo pathlib, y utilizar el método home()
from pathlib import Path
ruta_base= Path.home()
print(ruta_base)

# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path
from pathlib import Path
ruta=Path("curso python","dia 6","practicas_path.py")
print(ruta)

# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario

from pathlib import Path
ruta_base=Path.home()
ruta_absoluta = ruta_base / "Curso Python" / "Día 6" / "practicas_path.py"
print (ruta_absoluta)



# from os import system

# nombre = input("Dime tu numbre : ")

# edad = input("Dime tu edad : ")

# system('cls')

# print(nombre)
# print(edad)


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).
def abrir_leer():
    archivo=open("archivo.txt","r")
    return archivo
abrir=abrir_leer()
contenido=abrir.read()
print (contenido)
abrir.close()

# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
def sobrescribir():
    archivo = open("archivo.txt", "w")  
    archivo.write("contenido eliminado")  
    archivo.close()
    return archivo




# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error():
    archivo3=open("archivo.txt")
    archivo3.write("se ha registrado un error de ejecucon")
    archivo3.closed
    return archivo3





# sexta_parte_2.py
# Mostrando sexta_parte_2.py
# Actividad Clase 6 Parte 2
# luciano lugani
# •
# 24 oct (Editado: 24 oct)
# 100 puntos
# Fecha límite: 31 oct

# path.py
# Texto

# Europa.zip
# Archivo comprimido

# sexta_parte_2.py
# Texto
# Comentarios de la clase
