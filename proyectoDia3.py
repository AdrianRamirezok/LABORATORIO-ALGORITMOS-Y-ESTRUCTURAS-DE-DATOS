texto=input("ingrese un texto: ")
texto0=texto.lower()
texto1=list(texto0)

letra1=input("ingrese primer letra: ")
letra1.lower()
letra2=input("ingrese segunda letra: ")
letra2.lower()
letra3=input("ingrese tercera letra: ")
letra3.lower()

busqueda1=texto0.count(letra1)
busqueda2=texto0.count(letra2)
busqueda3=texto0.count(letra3)

print("cantidad de veces que se repite la letra: ",letra1,"es",busqueda1)
print("cantidad de veces que se repite la letra: ",letra2,"es",busqueda2)
print("cantidad de veces que se repite la letra: ",letra3,"es",busqueda3)

contador_palabras=len(texto0.split())
print("El texto tiene ",contador_palabras,"palabras")

primera_letra=(texto0[0])
ultima_letra=(texto0[-1])

print ("La primera letra del texto es: ", primera_letra)
print("La ultima letra del texto es: ",ultima_letra)

texto_invertido=(texto0[::-1])
print("EL texto al reves se escribe de esta manera: ",texto_invertido)

buscar_python= ("python"in texto0)
if buscar_python:
 print("la palabra python esta en el texto")
else:
 print("la palabra phyton no esta en el texto")


 print("Trabajo realizado por: Ramirez Adrian")




