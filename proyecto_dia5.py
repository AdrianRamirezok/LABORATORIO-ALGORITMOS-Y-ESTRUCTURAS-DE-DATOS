import random


palabras = ["python", "programacion", "ahorcado", "desarrollo", "computadora"]

def elegir_palabra():
  
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    
    progreso = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
    return progreso

def pedir_letra():
    
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Entrada inválida. Por favor, ingresa solo una letra.")

def verificar_letra(letra, palabra_secreta):
    
    return letra in palabra_secreta

def juego_ahorcado():

    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    vidas = 6
    
    print("Bienvenido al juego del Ahorcado!")
    
    while vidas > 0:
        print(f"Vidas restantes: {vidas}")
        print("Palabra: ", mostrar_progreso(palabra_secreta, letras_adivinadas))
        
        letra = pedir_letra()
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if verificar_letra(letra, palabra_secreta):
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            vidas -= 1
            print(f"Lo siento, la letra '{letra}' no está en la palabra.")
        
    
        if letra in letras_adivinadas:
          for letra in palabra_secreta:
            print(f"¡Felicidades! Has adivinado la palabra: '{palabra_secreta}'")
            break
    else:
        print(f"¡Perdiste! La palabra era: '{palabra_secreta}'")


juego_ahorcado()


print("Ramirez Adrian")