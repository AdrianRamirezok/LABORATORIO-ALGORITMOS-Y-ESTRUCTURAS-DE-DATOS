



# precios_cafe = [("capuchino",1.5), ("Expresso",2.5), ("Moka",3.5)]

# def cafe_mas_caro(lista_precios):

#     precio_mayor = 0
#     cafe_mas_caro = ''

#     for cafe,precio in lista_precios:
#         if precio > precio_mayor:
#             precio_mayor = precio_mayor
#             cafe_mas_caro = cafe
#         else:
#             pass
#     return(cafe_mas_caro,precio_mayor)

# cafe, precio = cafe_mas_caro(precios_cafe)
# print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")



# from random import shuffle

# # lista inicial 
# palitos = ['-','--','---','----']
# # mezclar palitos 
# def mezclar(lista):
#     shuffle(lista)
#     return lista

# # pedirle intento
# def probar_suerte():
#     intento = ''
#     while intento not in ['1','2','3','4']:
#         intento = input("Elige un numero del 1 al 4: ")
#     return int(intento)
# # Comprobar intento 
# def chequear_intento(lista, intento):
#     if lista[intento - 1] == '-':
#         print("Te toco el 8")
#     else:
#         print("Te has salvado ")
    
#     print(f"Te ha tocado {lista[intento-1]}")

# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)



# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
numeros=[1,2,3,4,5,6]
from random import choice
def lanzar_dados():
    tiro1 = choice(numeros)
    tiro2 = choice(numeros)
    return tiro1, tiro2  

def suma_dados(tiro1, tiro2):
    return tiro1 + tiro2

def evaluar_jugada(suma):
    if suma<6:
        print(f"La suma de tus dados es {suma}. Lamentable")
    if suma>6 and suma<10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    if suma>=10:
        print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
tiro1, tiro2 = lanzar_dados()
suma = suma_dados(tiro1, tiro2)
evaluar_jugada(suma)


# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

def reducir_lista(lista_numeros):
    lista_sin_duplicados = list(set(lista_numeros))
    if lista_sin_duplicados:
        lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados

def promedio(lista):
    if not lista:
        return 0  
    return sum(lista) / len(lista)
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)
print("Lista reducida:", lista_reducida)
print("Promedio:", resultado_promedio)




# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

from random import choice

def lanzar_moneda():
   return choice(["Cara", "Cruz"])

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []  
    else:  
        print("La lista fue salvada")
        return lista_numeros  

lista_numeros = [1, 2, 3, 4, 5]
resultado = lanzar_moneda()
print("Resultado del lanzamiento:", resultado)

lista_final = probar_suerte(resultado, lista_numeros)
print("Lista final:", lista_final)





def mi_funcion( *args):
    return sum(args)

resultado = mi_funcion(1,2,40,50)
print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

def suma_cuadrados(*args):
    total=0
    for n in args:
     total=n**2+total
    return total
resultado2=suma_cuadrados(1,2,3)
print(resultado2)

# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).



# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    return sum(args)
suma=suma_absolutos(1,2,3,-5,6,7)
print(suma)

# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = sum(args) 
    return f"{nombre}, la suma de tus números es {suma_numeros}"
resultado = numeros_persona("Adrián", 2, 3, 4, 5, 6)
print(resultado)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def suma  (**kwargs):
    total = 0
    for clave,valor  in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total



print(suma(a=1,b=2,c=3))


def test(num1,num2,*args,**kwargs):

    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]


test(20,10,100,200,300,400,a=1,b=2,c=3)


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    return len(kwargs)  

resultado = cantidad_atributos(nombre="Adrián", edad=25, ciudad="Cordoba")
print("Cantidad de atributos:", resultado)

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    return list(kwargs.values())
resultado = lista_atributos(nombre="Adrián", edad=30, ciudad="Madrid", ocupacion="Ingeniero")
print("Lista de atributos:", resultado)


# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items():
        print(f"{atributo}: {valor}")

describir_persona("María", color_ojos="azules", color_pelo="rubio", altura="1.65m")


print("Realizado por Ramirez Adrian")