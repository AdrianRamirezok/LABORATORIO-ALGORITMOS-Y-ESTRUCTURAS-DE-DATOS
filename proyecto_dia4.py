nombre=input("Bienvenido, ¿cual es su nombre?: ")
print("Bueno",nombre,"he pensado un numero del 1 al 100 y solo tendras 8 intentos para adivinarlo, comencemos")
contador=0
repeticiones=8
from random import randint
numero_correcto=randint(1,100)

while contador<repeticiones:
    numero_usuario=int(input("Escribe el numero que pensaste: "))
    if numero_usuario < 1 or numero_usuario > 100:
        print("El numero en el que he pesado esta entre el 1 y el 100, ingresa un valor que este entre ellos")
    if numero_usuario != numero_correcto:
        print("Ese numero no es el correcto")
    if numero_usuario ==numero_correcto:
        print("felicitaciones, acertaste es el numero que habia pensado") 
        print("Te ha tomado ",contador,"intentos")
        break
    if numero_usuario < numero_correcto:
        print("Una pista, el numero que he pesado es mayor al que ingresaste")
    if numero_usuario > numero_correcto:
        print("Una pista, el numero que he pesado es menor al que ingresaste")    
    contador=contador+1
else: 
    print("Lo siento, perdiste todas las oportunidades, el numero que habiaoensado es: ", numero_correcto)

print("Trabajo realizado por Ramirez Adrian")