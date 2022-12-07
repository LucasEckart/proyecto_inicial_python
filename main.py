import csv
import random
import interfaz 

def leer_palabra_secreta(csvfilename):
    with open ('palabras.csv') as file:
        data = list(csv.DictReader(file))
    palabra_secreta = random.choice(data)
    return palabra_secreta['palabras']
   
def pedir_letra(letras_usadas):
    
    while True:
        letra = str(input(f'Ingresar una nueva letra! ')).lower()
        if letra in letras_usadas:
            print (f'Esa letra ya fue ingresada, elegir otra!\n ')
            continue
        elif len(letra) > 1:
            print(f'Ingresar solo una letra!\n ')
            continue
        elif not letra.isalpha():
            print(f'Solo se permiten letras!\n ')
            continue
        
        letras_usadas.append(letra)
        return letra
        
           

def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False


def validar_palabra(letras_usadas, palabra_secreta):
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i - 1] in letras_usadas:
            return True
        else:
            return False



if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')