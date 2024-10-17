


nombre_estudiantes=[]


while True:

    nombre=input("Ingrese el nombre de los estudiantes, FIN para ingresar al menu, REPETIR para ver los nombres ingresados ")
    if nombre.lower()=="fin":
        break
    
    elif nombre.lower()=="repetir":
         print("Nombres ingresados hasta el momento:", nombre_estudiantes)
        
    elif nombre.isdigit():
      print("Solo se permiten nombres alfabeticos ")  
 
    elif nombre.isalpha():
       
      nombre_estudiantes.append(nombre)
    elif nombre.isspace():  
     
      nombre_estudiantes.append(nombre)  
    else:
     print("Solo se permiten nombres alfabeticos ")
    
    
while True:
    print(" Menú de Análisis de Nombres ")
    print("1. Mostrar nombres ingresados")
    print("2. Ordenar los nombres alfabéticamente")
    print("3. Análisis de longitud de los nombres")
    print("4. Contar vocales y consonantes")
    print("5. Contar palabras en cada nombre")
    print("6. Inversión de los nombres")
    print("7. Mostrar nombres que empiezan con una letra que usted elija")
    print("8. Buscar un nombre que usted elija en la lista")
    print("9. Nombres con mas de 5 caracteres")
    print("10. Para convertir todos los nombres en minuscula o mayuscula")
    print("11. Salir")
    opcion=input("elija la opcion que desee: ")
    if opcion=="1":
        print("los nombres ingresados son: ",nombre_estudiantes)
        continue    
    if opcion=="2":
        nombre_estudiantes.sort()
        print(nombre_estudiantes)
        continue    

    if opcion=="3":
        nombre_corto=(min(nombre_estudiantes,key=len))
        nombre_largo=(max(nombre_estudiantes,key=len))
        print("El nombre mas largo es: ",nombre_largo)
        print("El nombre mas corto es: ",nombre_corto)  
        continue    

    if opcion=="4":
       total_vocales=0
       total_consonantes=0
       for nombre in nombre_estudiantes:
        for letra in nombre:
            if letra.lower() in "aeiou":
             total_vocales=total_vocales+1
            else:
             total_consonantes=total_consonantes+1
             
       print("el total de vocales en la lista es: ",total_vocales)  
       print("el total de consonantes es: ",total_consonantes)   
       continue    

    
    if opcion=="5":
        for nombre in nombre_estudiantes:
            cantidad_palabras=len(nombre.split())
            print(nombre,"tiene ",cantidad_palabras,"palabras")
        continue    


    if opcion=="6": 
        nombres_invertidos=nombre_estudiantes[::-1]
        print(nombres_invertidos)
        continue    

    
    if opcion=="7":
        letra=input("ingrese la inicial del nombre que desea buscar: ")
        nombres_iniciales=[]
        for nombre in nombre_estudiantes:
            if nombre.startswith(letra):
                nombres_iniciales.append(nombre)
        if nombres_iniciales:        
            print("los nombres que inician con la letra,",letra,"son: ",nombres_iniciales)
        else:
             print("no se encontraron nombres con esa inicial ")
        continue    

     
    if opcion=="8":
         buscador=input("ingrese el nombre que deseea buscar: ")
         if buscador in nombre_estudiantes:
            print("el nombre ", buscador, "si se encustra entre los estudiantes")
         else:
            print("el nombre", buscador, "no se encustra entre los estudiantes")
         continue    

    if opcion=="9":
        contador=0
        for nombre in nombre_estudiantes:
            if len(nombre)> 5:
             contador = contador+1
        print("La cantidad de nombres con mas de 5 caracteres es: ",contador)
        continue    


    if opcion=="10":
        print("1. minuscula")
        print("2. mayuscula")
        eleccion=input("desea ver los nombres en: ")   
        
        for nombre in nombre_estudiantes:
          if eleccion=="1":
           lista_minuscula=(nombre.lower())
           print(lista_minuscula)
          if eleccion=="2":
            lista_mayuscula=(nombre.upper())
            print(lista_mayuscula)
        continue    

        
    if opcion=="11":
       print("FIN")
    break
print("trabajo realizado por Ramirez Adrian")
        
        

