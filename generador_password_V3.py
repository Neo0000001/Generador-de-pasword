__autor__ = 'Enrique Manuel Jiménez'

import random  # Importamos la librería random para generar números y símbolos aleatorios
import os  # Importamos la librería os para ejecutar comandos del sistema operativo

# Definimos los símbolos que se pueden usar en el password
letras = 'abcdefghijklmnopqrstuvwz'
letras_mayusculas = letras.upper()  # Convertimos las letras a mayúsculas
numeros = '1234567890'
simbolos = '#$&*.'

# Convertimos las cadenas de símbolos en listas
letras_lista = list(letras)
letras_mayusculas_lista = list(letras_mayusculas)
numeros_lista = list(numeros)
simbolos_lista = list(simbolos)

# Combinamos todas las listas en una sola
lista_completa = letras_lista + letras_mayusculas_lista + \
    numeros_lista + simbolos_lista


def generador_password(longitud):
    """Genera un password aleatorio de una longitud específica que cumpla con los requisitos."""

    while True:
        passw = ''.join(random.choice(lista_completa) for _ in range(longitud))
        if validar_password(passw):
            return passw


def validar_password(passw):
    """Valida que el password contenga al menos una letra mayúscula, un número y un símbolo."""

    tiene_mayusculas = any(
        mayuscula in passw for mayuscula in letras_mayusculas_lista)
    tiene_numeros = any(numero in passw for numero in numeros_lista)
    tiene_simbolos = any(simbolo in passw for simbolo in simbolos_lista)

    return tiene_mayusculas and tiene_numeros and tiene_simbolos


def main():

    os.system('clear')  # Limpiamos la pantalla (en sistemas Unix)

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
        longitud = int(
            input('\nIntroduce la longitud del password (8 a 16): '))

        if 8 <= longitud <= 16:
            password = generador_password(longitud)
            print(f'\nSe ha generado un password aleatorio de {
                  longitud} caracteres, que contiene al menos una letra mayuscula, un digito y un simbolo --> {password}')
        else:
            print('\nOpción no válida, debe introducir un número del 8 al 16')

            input('\nPulse ENTER para regresar... ')
            main()

    except ValueError:
        print('\nHa introducido un valor inválido.')
        input('\nPulse ENTER para regresar... ')


if __name__ == '__main__':
    main()
