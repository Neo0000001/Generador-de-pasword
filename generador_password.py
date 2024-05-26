__autor__ = 'Enrique Manuel Jimenz'

import random  # Importamos la librería random para generar números y caracteres aleatorios
import os  # Importamos la librería os para ejecutar comandos del sistema operativo

# Función que genera un password aleatorio de una longitud específica


def generador_password(longitud):
    # Definimos los caracteres que se pueden usar en el password
    letras = 'abcdefghijklmnopqrstuvwz'
    letras_mayusculas = letras.upper()  # Convertimos las letras a mayúsculas
    numeros = '1234567890'
    caracteres = '#$&*.'

    # Convertimos las cadenas de caracteres en listas
    letras_lista = list(letras)
    letras_mayusculas_lista = list(letras_mayusculas)
    numeros_lista = list(numeros)
    caracteres_lista = list(caracteres)

    # Combinamos todas las listas en una sola
    lista_completa = letras_lista + letras_mayusculas_lista + \
        numeros_lista + caracteres_lista

    passw = []  # Inicializamos la lista que contendrá los caracteres del password

    # Generamos el password de longitud especificada
    for i in range(longitud):
        # Elegimos un carácter aleatorio de la lista completa
        aleatorio = random.choice(lista_completa)
        passw.append(aleatorio)  # Añadimos el carácter a la lista del password

    passw = ''.join(passw)  # Convertimos la lista de caracteres en una cadena

    return passw  # Devolvemos el password generado

# Función principal


def main():
    os.system('clear')  # Limpiamos la pantalla (en sistemas Unix)

    # Mostramos un banner artístico
    print("""
          
  ▄▀  ▄███▄      ▄   ▄███▄   █▄▄▄▄ ██   ██▄   ████▄ █▄▄▄▄     ██▄   ▄███▄       █ ▄▄  ██      ▄▄▄▄▄    ▄▄▄▄▄    ▄ ▄   ████▄ █▄▄▄▄ ██▄   
▄▀    █▀   ▀      █  █▀   ▀  █  ▄▀ █ █  █  █  █   █ █  ▄▀     █  █  █▀   ▀      █   █ █ █    █     ▀▄ █     ▀▄ █   █  █   █ █  ▄▀ █  █  
█ ▀▄  ██▄▄    ██   █ ██▄▄    █▀▀▌  █▄▄█ █   █ █   █ █▀▀▌      █   █ ██▄▄        █▀▀▀  █▄▄█ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄  █ ▄   █ █   █ █▀▀▌  █   █ 
█   █ █▄   ▄▀ █ █  █ █▄   ▄▀ █  █  █  █ █  █  ▀████ █  █      █  █  █▄   ▄▀     █     █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀   █  █  █ ▀████ █  █  █  █  
 ███  ▀███▀   █  █ █ ▀███▀     █      █ ███▀          █       ███▀  ▀███▀        █       █                     █ █ █          █   ███▀  
              █   ██          ▀      █               ▀                            ▀     █                       ▀ ▀          ▀          
                                    ▀                                                  ▀                                               
          """)

    try:
        # Solicitamos al usuario que introduzca la longitud del password
        longitud = int(
            input('\nIntroduce la longitud del password (8 a 15): '))

        # Verificamos que la longitud esté dentro del rango permitido
        if longitud < 8 or longitud > 15:
            print('\nOpción no válida, debe introducir un número del 8 al 15')
            input('\nPulse ENTER para regresar... ')
            main()  # Reiniciamos el proceso si la longitud no es válida
        else:
            # Generamos y mostramos el password si la longitud es válida
            print(f'\nSe ha generado un password aleatorio de {
                  longitud} caracteres --> {generador_password(longitud)}')
    except ValueError:
        # Manejo de errores si el usuario no introduce un número válido
        print('\nHa introducido un valor inválido.')
        input('\nPulse ENTER para regresar... ')
        main()  # Reiniciamos el proceso si el valor introducido no es válido


# Punto de entrada del script
if __name__ == '__main__':
    main()
