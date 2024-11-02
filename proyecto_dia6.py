import os

def mostrar_categorias():
    recetas=os.listdir("Recetas")
    return recetas


def abrir_categorias():
    categorias = mostrar_categorias()
    categoria = input(f"Seleccione una categoría de las siguientes: {categorias}: ")
    ruta_categoria = os.path.join("Recetas", categoria)

    if os.path.exists(ruta_categoria) and os.path.isdir(ruta_categoria):
        recetas = os.listdir(ruta_categoria)
        if recetas:
            print(f"Recetas en la categoría '{categoria}': {recetas}")
            receta = input("Elija la receta que desea leer: ")
            ruta_receta = os.path.join(ruta_categoria, receta)

            if os.path.exists(ruta_receta) and receta.endswith('.txt'):
                with open(ruta_receta, 'r') as archivo:
                    print(archivo.read())
            else:
                print("La receta no existe o no es un archivo .txt.")
        else:
            print(f"No hay recetas en la categoría '{categoria}'.")
    else:
        print(f"La categoría '{categoria}' no existe.")
 

def crear_categoria():
    nueva_categoria = input("Introduce el nombre de la nueva categoría: ")
    ruta_categoria = os.path.join("Recetas", nueva_categoria)

    try:
        os.makedirs(ruta_categoria)
        print(f"Categoría '{nueva_categoria}' creada exitosamente.")
    except FileExistsError:
        print(f"La categoría '{nueva_categoria}' ya existe.")


def crear_receta():
    categorias = mostrar_categorias()
    categoria = input(f"Seleccione una categoría de las siguientes: {categorias}: ")
    ruta_categoria = os.path.join("Recetas", categoria)

    if os.path.exists(ruta_categoria) and os.path.isdir(ruta_categoria):
        nombre_receta = input("Introduce el nombre de la receta (incluyendo .txt): ")
        contenido_receta = input("Agrega el contenido de la receta: ")
        ruta_receta = os.path.join(ruta_categoria, nombre_receta)

        with open(ruta_receta, 'w') as archivo:
            archivo.write(contenido_receta)
        print(f"Receta '{nombre_receta}' creada exitosamente en la categoría '{categoria}'.")
    else:
        print(f"La categoría '{categoria}' no existe.")


def eliminar_categoria():
    categoria = input("Introduce la categoría que desea eliminar: ")
    ruta_categoria = os.path.join("Recetas", categoria)

    if os.path.exists(ruta_categoria) and os.path.isdir(ruta_categoria):
       
        for receta in os.listdir(ruta_categoria):
            os.remove(os.path.join(ruta_categoria, receta))
        os.rmdir(ruta_categoria)
        print(f"Categoría '{categoria}' eliminada exitosamente.")
    else:
        print(f"La categoría '{categoria}' no existe.")

def eliminar_receta():
    categorias = mostrar_categorias()
    categoria = input(f"Seleccione una categoría de las siguientes: {categorias}: ")
    ruta_categoria = os.path.join("Recetas", categoria)

    if os.path.exists(ruta_categoria) and os.path.isdir(ruta_categoria):
        recetas = os.listdir(ruta_categoria)
        if recetas:
            print(f"Recetas en la categoría '{categoria}': {recetas}")
            receta = input("Elija la receta que desea eliminar (incluyendo .txt): ")
            ruta_receta = os.path.join(ruta_categoria, receta)

            if os.path.exists(ruta_receta) and receta.endswith('.txt'):
                os.remove(ruta_receta)
                print(f"Receta '{receta}' eliminada exitosamente.")
            else:
                print("La receta no existe o no es un archivo .txt.")
        else:
            print(f"No hay recetas en la categoría '{categoria}'.")
    else:
        print(f"La categoría '{categoria}' no existe.")

def menu():
 while True:   
    print("bienvenido elija que desea hacer: ")
    print("1.ver categorias y recetas")
    print("2.crear categoria")
    print("3.crear receta")
    print("4.eliminar categoria")
    print("5.eliminar receta")
    print("6.salir")

    opcion=input("Seleccione la opcion deseada: ")
   
    if opcion=="1":
      categorias=mostrar_categorias()
      print(f"las categorias disponibles son:{categorias}")
      recetas=abrir_categorias()
      print(f" {recetas}")
    
    elif opcion=="2":
        crear_cat_rec=crear_categoria()
        print(f"{crear_cat_rec}")

    elif opcion=="3":
        crear_rec=crear_receta()
        print(f"{crear_rec}")
    
    elif opcion == "4":
         eliminar_cat=eliminar_categoria()
         print(f"{eliminar_cat}")
   
    elif opcion == "5":
         eliminar_rec=eliminar_receta()
         print(f"{eliminar_rec}")
           
   
    elif opcion == "6":
            print("Saliendo del programa...")
            break
    
    else:
            print("Opción no válida. Intente nuevamente.")

   
       
menu()

print("Ramirez Adrian")