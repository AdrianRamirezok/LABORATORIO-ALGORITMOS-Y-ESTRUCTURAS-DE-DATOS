
#ejercicio 1
def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    intermedio = num1 + num2 + num3 - mayor - menor  
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else: 
        return intermedio

resultado = devolver_distintos(4, 7, 1)
print("Resultado:", resultado)

#-----------------------------------------------------------------------------------------------
#Ejercicio 2

def letras_unicas(palabra):

    letras = set(palabra) 
    letras_ordenadas = sorted(letras) 
    return letras_ordenadas
resultado = letras_unicas("entretenido")
print(resultado)
 
 #--------------------------------------------------------------------------------------------------
 #ejercicio 3

def verificar_ceros_consecutivos(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i - 1] == 0:
            return True
    return False

resultado1 = verificar_ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5)
resultado2 = verificar_ceros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1)

print("Resultado 1:", resultado1) 
print("Resultado 2:", resultado2)  

#----------------------------------------------------------------------------------------------------
#ejercicio 4

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(n):
    cantidad_primos = 0
    print("Números primos en el rango de 0 a", n, ":")
    
    for num in range(2, n + 1):  # Empezamos desde 2, ya que 0 y 1 no son primos
        if es_primo(num):
            print(num)
            cantidad_primos =cantidad_primos+1
            
    return cantidad_primos


resultado = contar_primos(20)
print("Cantidad de números primos encontrados:", resultado)
