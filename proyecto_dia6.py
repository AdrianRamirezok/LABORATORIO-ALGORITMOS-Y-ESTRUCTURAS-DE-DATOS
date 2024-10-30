import os


def mostrar_receta():
    recetas=os.listdir("Recetas")
    return recetas
mostrar=mostrar_receta()

print(f"las recetas son{mostrar}")

def crear_receta():
    recetas=open("recetas","w")
    recetas.write()
    return recetas

