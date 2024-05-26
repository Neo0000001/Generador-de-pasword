# Generador de Passwords Aleatorios

Este proyecto es un script en Python que genera passwords aleatorios de una longitud especificada por el usuario. El objetivo es proporcionar una herramienta sencilla para crear contraseñas seguras y difíciles de adivinar.

## Autor
__Autor__: Enrique Manuel Jiménez

## Descripción

El script permite al usuario generar una contraseña aleatoria con una longitud especificada entre 8 y 15 caracteres. Utiliza una combinación de letras minúsculas, mayúsculas, números y caracteres especiales para garantizar la seguridad del password generado.

## Funcionalidades

- Generación de passwords aleatorios.
- Validación de la longitud del password (entre 8 y 15 caracteres).
- Limpieza de pantalla para una mejor visualización.
- Manejo de errores para entradas no válidas.

## Uso

Para ejecutar el script, simplemente abre una terminal y corre el archivo `generador_password.py`. Sigue las instrucciones en pantalla para introducir la longitud deseada del password.

### Ejecución del script

```bash
python generador_password.py
```

### Requisitos

* Python 3.x

### Notas

Este script limpia la pantalla usando el comando clear, que funciona en sistemas Unix. Si estás usando Windows, puedes cambiar os.system('clear') por os.system('cls').
¡Esperamos que este generador de passwords sea de utilidad para mantener tus cuentas seguras!
