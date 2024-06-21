# Importamos las librerias necesarias
from colorama import init, Fore
import getpass  # Para ocultar la entrada de la contraseña
import hashlib
import json
import os
import random
from cryptography.fernet import Fernet

# Información del proyecto
__autor__: "Enrique Jimenez"
__version__: "1.0"
__description__: "Asesor de Passwords y Generador de Passwords aleatorios."

# Inicializar colorama
init()

# Definición de variables globales
letras = 'abcdefghijklmnopqrstuvwz'
letras_mayusculas = letras.upper()
numeros = '1234567890'
# Caracteres especiales (Podemos añadir o eliminar)
simbolos = r"!#$%&'()*+,-./:;?@[\]_{|}"

# Convertir las cadenas de caracteres a listas
letras_lista = list(letras)
letras_mayusculas_lista = list(letras_mayusculas)
numeros_lista = list(numeros)
simbolos_lista = list(simbolos)
lista_completa = letras_lista + letras_mayusculas_lista + \
    numeros_lista + simbolos_lista


class GeneradorPassword:
    def __init__(self):
        """
        Inicializa el objeto con los atributos necesarios.

        Este método establece los valores iniciales para los atributos del objeto.
        Crea un diccionario vacío llamado `diccionario` con una sola pareja clave-valor
        para la clave `'Urls'` y un diccionario vacío como su valor.

        Luego, llama al método `load_key` para cargar o generar una clave de encriptación.
        La clave generada se almacena en el atributo `key`.

        El atributo `cipher` se inicializa con la clase `Fernet`, pasando la
        `key` como argumento.

        El atributo `file_path` se establece en `'fichero_password.json'`, que es la
        ruta del archivo JSON.

        Finalmente, el atributo `hash_contraseña_correcta` se establece llamando al
        método `load_password_hash`.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            None
        """

        self.diccionario = {'Urls': {}}  # Crear un diccionario vacío
        self.key = self.load_key()  # Cargar o generar clave de encriptación
        self.cipher = Fernet(self.key)  # Instanciar la clase Fernet
        self.file_path = 'fichero_password.json'  # Ruta del archivo JSON
        # Cargar o generar hash de la contraseña
        self.hash_contraseña_correcta = self.load_password_hash()

    def generar_hash_contraseña(self, contraseña):
        """Generar un hash SHA-256 de la contraseña."""

        hash_obj = hashlib.sha256(contraseña.encode())

        return hash_obj.hexdigest()

    def verificar_contraseña(self):
        """
        Verifica la contraseña del usuario solicitando al usuario que ingrese su contraseña y comparandola con la contraseña cifrada correcta.

        Esta función no toma parámetros.

        Intenta verificar la contraseña del usuario solicitando al usuario que ingrese su contraseña utilizando la función `getpass.getpass()`. La contraseña ingresada se cifra utilizando el método `generar_hash_contraseña()` del objeto actual. Si la contraseña cifrada coincide con la contraseña cifrada correcta almacenada en el atributo `hash_contraseña_correcta` del objeto actual, la función imprime un mensaje de éxito y devuelve `True`. Si la contraseña cifrada no coincide, la función imprime un mensaje que indica el número de intentos restantes y continúa el bucle. Si el usuario ingresa la contraseña correcta dentro del número especificado de intentos, la función devuelve `True`. Si el usuario ingresa una contraseña incorrecta el número especificado de intentos, la función imprime un mensaje de error y devuelve `False`.

        Retorna:
            bool: `True` si el usuario ingresa la contraseña correcta, `False` de lo contrario.
        """

        intentos = 3  # Número de intentos permitidos

        for intento in range(intentos):
            # Ocultar la entrada de la contraseña
            contraseña_ingresada = getpass.getpass(
                Fore.YELLOW + "\nIntroduce la contraseña de acceso al programa: " + Fore.RESET)
            hash_contraseña_ingresada = self.generar_hash_contraseña(
                contraseña_ingresada)

            if hash_contraseña_ingresada == self.hash_contraseña_correcta:
                print(Fore.GREEN + '\nContraseña correcta. Bienvenido!!.' + Fore.RESET)
                input(Fore.YELLOW + '\nPulse ENTER para continuar... ' + Fore.RESET)
                return True
            else:
                print(Fore.RED + f"\nContraseña incorrecta. Te quedan {
                      intentos - intento - 1} intentos." + Fore.RESET)

        print(Fore.RED + 'Has superado el número de intentos permitidos. El programa se cerrará.' + Fore.RESET)

        return False

    def load_key(self):
        """Cargar la clave desde un archivo o generar una nueva si no existe."""

        key_file = 'secret.key'

        # Cargar la clave desde un archivo o generar una nueva si no existe
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(key)

        return key

    def load_password_hash(self):
        """Cargar el hash de la contraseña desde un archivo o generar una nueva si no existe."""

        password_hash_file = 'password_hash.txt'

        if os.path.exists(password_hash_file):
            with open(password_hash_file, 'r') as file:
                hash_contraseña = file.read().strip()
        else:
            self.limpiar_consola()
            nueva_contraseña = getpass.getpass(
                Fore.YELLOW + 'Crea una contraseña de acceso, esta contraseña debera ser recordada para la proxima vez que uses el programa: ' + Fore.RESET)
            hash_contraseña = self.generar_hash_contraseña(nueva_contraseña)

            with open(password_hash_file, 'w') as file:
                file.write(hash_contraseña)

        return hash_contraseña

    def limpiar_consola(self):
        """
        Borra la pantalla de la consola.

        Esta función borra la pantalla de la consola utilizando el comando apropiado para el sistema operativo. Primero verifica si el sistema operativo es Windows comprobando el valor del atributo `os.name`. Si es Windows, utiliza el comando `cls` para borrar la pantalla. De lo contrario, utiliza el comando `clear`.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Ninguno
        """

        os.system('cls' if os.name == 'nt' else 'clear')

    def usuario_existe(self, urls, usuario):
        """
        Verifica si un usuario existe en una URL dada.

        Parámetros:
            urls (str): La URL a verificar.
            usuario (str): El nombre de usuario a buscar.

        Retorna:
            bool: True si el usuario existe en la URL, False de lo contrario.
        """

        if urls in self.diccionario['Urls']:
            for elemento in self.diccionario['Urls'][urls]:
                if elemento['Usuario'] == usuario:
                    return True

        return False

    def crear_registro(self):
        """
        Crea un nuevo registro en el diccionario.

        Esta función solicita al usuario que introduzca una URL y un nombre de usuario. Comprueba si la URL ya existe en el diccionario.
        Si la URL no existe, crea una nueva entrada en el diccionario.
        Si la URL existe, comprueba si el nombre de usuario ya existe en la URL.
        Si el nombre de usuario existe, muestra un mensaje indicando que el nombre de usuario ya existe.
        Si el nombre de usuario no existe, genera una contraseña aleatoria de una longitud especificada y agrega una nueva entrada
        al diccionario con la URL, nombre de usuario y contraseña.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            None
        """

        urls = input(Fore.YELLOW + '\nIntroduce la dirección URL o presiona ENTER para cancelar y volver al menú principal: ' +
                     Fore.RESET).lower().strip()

        # Si el usuario presiona ENTER, se cancela la operación y regresa al menú
        if urls == '':
            return

        if not self.comprobar_registro(urls):
            return

        usuario = input(
            Fore.YELLOW + '\nIntroduce el nombre de Usuario o presiona ENTER para cancelar y volver al menú principal: ' + Fore.RESET).lower().strip()

        # Si el usuario presiona ENTER, se cancela la operación y regresa al menú
        if usuario == '':
            return

        if self.usuario_existe(urls, usuario):
            print(
                Fore.GREEN + '\nEl usuario introducido ya existe. No se pueden crear usuarios duplicados en la misma URL.' + Fore.RESET)
            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
            return

        longitud = 16  # Longitud por defecto de la contraseña

        opcion = input(
            '\nAl pulsar' + Fore.GREEN + ' ENTER' + Fore.RESET + ' se generará automáticamente una contraseña aleatoria de 16 caracteres de longitud. Si desea cambiar la longitud de la contraseña, introduzca' + Fore.GREEN + ' "Si" ' + Fore.RESET).lower().strip()

        if opcion == 'si':
            try:
                longitud = int(
                    input(Fore.YELLOW + '\nIntroduce la longitud de la contraseña (8 a 18): ' + Fore.RESET))
                if not (8 <= longitud <= 18):
                    print(
                        Fore.GREEN + '\nOpción no válida, debe introducir un número del 8 al 18' + Fore.RESET)
                    input(
                        Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
                    return
            except ValueError:
                print(Fore.GREEN + '\nHa introducido un valor inválido.')
                input(Fore.YELLOW +
                      '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

                return

        # Genera una contraseña aleatoria de la longitud especificada
        password = self.generador_password(longitud)

        if urls not in self.diccionario['Urls']:
            self.diccionario['Urls'][urls] = []

        self.diccionario['Urls'][urls].append(
            {'Usuario': usuario, 'Password': password})

        print(Fore.GREEN + f'\nSe ha generado una contraseña aleatoria de {longitud} caracteres, para la URL ' + Fore.RED + f'{
              urls}' + Fore.GREEN + ' y el Usuario ' + Fore.RED + f'{usuario}' + Fore.RESET + ' --> ' + Fore.BLUE + f'{password}')

        input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

        self.save_to_file()  # Guarda el diccionario en el archivo

    def crear_registro_manual(self):
        """
        Crea un nuevo registro en el diccionario con una contraseña establecida por el usuario y no aleatoria.

        Esta función solicita al usuario que ingrese una URL y un nombre de usuario. Comprueba si la URL ya existe en el diccionario.
        Si la URL no existe, crea una nueva entrada en el diccionario.
        Si la URL existe, comprueba si el nombre de usuario ya existe en la URL.
        Si el nombre de usuario existe, muestra un mensaje indicando que el nombre de usuario ya existe.
        Si el nombre de usuario no existe, genera una contraseña aleatoria de una longitud especificada y agrega una nueva entrada
        al diccionario con la URL, nombre de usuario y contraseña.

        Parámetros:
            self (objeto): La instancia de la clase.

        Devuelve:
            Ninguno
        """

        urls = input(
            Fore.YELLOW + '\nIntroduce la dirección URL o presiona ENTER para cancelar y regresar al Menu Principal: ' + Fore.RESET).lower().strip()

        # Si el usuario presiona ENTER, se cancela la operación y regresa al menú
        if urls == '':
            return

        if not self.comprobar_registro(urls):
            return

        usuario = input(
            Fore.YELLOW + '\nIntroduce el nombre de Usuario o presiona ENTER para cancelar y regresar al Menu Principal: ' + Fore.RESET).lower().strip()

        # Si el usuario presiona ENTER, se cancela la operación y regresa al menú
        if usuario == '':
            return

        password = input(
            Fore.YELLOW + 'Introduce la Contraseña o presiona ENTER para cancelar y regresar al Menu Principal: ' + Fore.RESET).strip()

        # Si el usuario presiona ENTER, se cancela la operación y regresa al menú
        if password == '':
            return

        # Comprueba si el nombre de usuario ya existe en la URL
        if urls not in self.diccionario['Urls']:
            self.diccionario['Urls'][urls] = []

        # Agrega el nuevo registro al diccionario
        self.diccionario['Urls'][urls].append(
            {'Usuario': usuario, 'Password': password})

        print(Fore.GREEN + '\nSe ha creado el registro correctamente... ')

        input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

        self.save_to_file()  # Guarda el diccionario en el archivo

    def comprobar_registro(self, urls):
        """
        Comprueba si una URL dada ya está registrada en el diccionario.

        Esta función toma una URL como entrada y verifica si existe en el diccionario.
        Si la URL existe, imprime un mensaje indicando que la URL ya está registrada.
        Luego solicita al usuario crear otro usuario para esa URL.
        Si el usuario elige crear otro usuario, devuelve True.
        Si el usuario elige no crear otro usuario, imprime un mensaje para regresar al menú principal y devuelve False.
        Si la URL no existe, devuelve True.

        Parámetros:
            self (objeto): La instancia de la clase.
            urls (str): La URL a verificar.

        Devoluciones:
            bool: True si la URL no existe o si el usuario elige crear otro usuario. False si el usuario elige no crear otro usuario.
        """

        if urls in self.diccionario['Urls']:
            print(
                Fore.GREEN + '\nLa Url introducida ya se encuentra en el registro.' + Fore.RESET)
            opcion = input(
                Fore.YELLOW + '\nQuiere crear otro Usuario para esa Url?' + Fore.GREEN + ' (Si/No) ' + Fore.RESET).lower().strip()
            if opcion == 'si':
                return True
            else:
                input(Fore.YELLOW +
                      '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
                return False

        return True

    def generador_password(self, longitud):
        """
        Genera una contraseña aleatoria de la longitud especificada.

        Parámetros:
            longitud (int): La longitud de la contraseña a generar.

        Retorna:
            str: La contraseña generada.

        Descripción:
            Esta función genera una contraseña aleatoria de la longitud especificada. Utiliza la función `random.choice()`
            para seleccionar caracteres aleatorios de la lista `lista_completa`. La contraseña se genera uniendo los
            caracteres elegidos aleatoriamente utilizando la función `join()`. Se llama al método `validar_password()`
            para validar la contraseña generada. Si la contraseña es válida, se retorna. La función continúa generando
            contraseñas hasta que se encuentre una válida.

        Ejemplo:
            >>> generador_password(10)
            'Kf3gK5j8Yy'
        """

        while True:
            passw = ''.join(random.choice(lista_completa)
                            for _ in range(longitud))

            if self.validar_password(passw):
                return passw

    def validar_password(self, passw):
        """
        Valida una contraseña basada en los criterios dados.

        Parámetros:
            passw (str): La contraseña a validar.

        Retorna:
            bool: True si la contraseña cumple con los criterios, False de lo contrario.

        Criterios:
            - La contraseña debe contener al menos una letra mayúscula.
            - La contraseña debe contener al menos un dígito.
            - La contraseña debe contener al menos un símbolo.

        Ejemplo:
            >>> validar_password("Password123!")
            True
        """

        tiene_mayusculas = any(
            mayuscula in passw for mayuscula in letras_mayusculas_lista)
        tiene_numeros = any(numero in passw for numero in numeros_lista)
        tiene_simbolos = any(simbolo in passw for simbolo in simbolos_lista)

        return tiene_mayusculas and tiene_numeros and tiene_simbolos

    def listar_registros(self):
        """
        Lista todos los registros almacenados en el Archivo de Contraseñas.

        Esta función itera sobre el diccionario de URLs y sus registros correspondientes.
        Imprime la URL y la información de usuario y contraseña para cada registro.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            None

        Ejemplo:
            >>> listar_registros()
            >== Listado de todos los registros almacenados en el Fichero de Passwords ==<

            Url: ejemplo.com
              Usuario: usuario1
              Contraseña: contraseña1
              ---------------------------

              Usuario: usuario2
              Contraseña: contraseña2
              ---------------------------

            Pulse ENTER para regresar al menú...
        """

        # Comprueba si el diccionario de URLs no contiene información
        if not self.diccionario['Urls']:
            print(
                Fore.GREEN + '\nEl fichero todavía no contiene ningún registro.' + Fore.RESET)
            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
            return

        print(Fore.BLUE + '\n>== Listado de todos los registros almacenados en el Fichero de Passwords ==<\n' + Fore.RESET)

        for url, registros in self.diccionario['Urls'].items():
            print(Fore.RED + f'\nUrl: ' + Fore.RESET + f'{url}\n')
            for registro in registros:
                print(Fore.GREEN + '  Usuario: ' +
                      Fore.RESET + f'{registro["Usuario"]}')
                print(Fore.GREEN + '  Password: ' +
                      Fore.RESET + f'{registro["Password"]}')
                print('  ---------------------------')

        input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

    def buscar_password(self):
        """
        Muestra una lista de URLs y sus nombres de usuario y contraseñas asociadas.

        Esta función primero verifica si el diccionario de URLs está vacío. Si lo está, se muestra un mensaje indicando que el archivo
        no contiene ningún registro. La función entonces devuelve.

        Si el diccionario de URLs no está vacío, la función muestra una lista de URLs y sus nombres de usuario y contraseñas asociadas.
        El usuario es solicitado para ingresar el índice de la URL en la que se encuentra el usuario. La función luego muestra una lista
        de nombres de usuario asociados a la URL seleccionada. El usuario es solicitado para ingresar el índice del nombre de
        usuario que desea ver. La función luego muestra el nombre de usuario y la contraseña asociados al nombre de usuario
        seleccionado.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Ninguno

        Ejemplo:
            >>> buscar_password()
            >== Listado de URLS ==<

            1 - ejemplo.com

            Introduce el índice de la URL donde se encuentra el usuario: 1

            >== Lista de usuarios almacenados en la URL ejemplo.com ==<

            1 - usuario1

            Introduce el índice del usuario que deseas mostrar su contraseña: 1

            Usuario: usuario1
            Password: contraseña1

            Pulse ENTER para regresar al menú...
        """

        # Comprueba si el diccionario de URLs no contiene información
        if not self.diccionario['Urls']:
            print(
                Fore.GREEN + '\nEl fichero todavía no contiene ningún registro.' + Fore.RESET)
            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
            return

        print(Fore.BLUE + '\n>== Listado de URLS ==<\n' + Fore.RESET)
        # Obtiene una lista de URLs
        urls = list(self.diccionario['Urls'].keys())
        # Imprime la lista de URLs en forma numerada
        for indice, url in enumerate(urls, start=1):
            print(Fore.YELLOW + f'{indice} - ' + Fore.RESET + f'{url}')

        try:
            url_idx = int(
                input(Fore.YELLOW + '\nIntroduce el índice de la URL donde se encuentra el usuario: ' + Fore.RESET))
            if 1 <= url_idx <= len(urls):
                url = urls[url_idx - 1]

                print(Fore.BLUE +
                      f'\n>== Lista de usuarios almacenados en la URL {url} ==<\n' + Fore.RESET)

                for indice, usuario in enumerate(self.diccionario['Urls'][url], start=1):
                    print(Fore.YELLOW + f'{indice} - ' +
                          Fore.RESET + f'{usuario["Usuario"]}')

                usuario_idx = int(
                    input(Fore.YELLOW + '\nIntroduce el índice del usuario que deseas mostrar su contraseña: ' + Fore.RESET))

                if 1 <= usuario_idx <= len(self.diccionario['Urls'][url]):
                    print(Fore.RED + '\nUsuario: ' + Fore.RESET +
                          f'{self.diccionario["Urls"][url][usuario_idx - 1]["Usuario"]}')
                    print(Fore.RED + 'Password: ' + Fore.RESET +
                          f'{self.diccionario["Urls"][url][usuario_idx - 1]["Password"]}')
                else:
                    print(Fore.GREEN + '\nÍndice no válido.' + Fore.RESET)
            else:
                print(Fore.GREEN + '\nÍndice no válido.' + Fore.RESET)
        except ValueError:
            print(Fore.GREEN + '\nEntrada no válida.' + Fore.RESET)

        input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

    def eliminar_registro(self):
        """
        Una función para eliminar una URL y sus registros asociados o eliminar un usuario específico de una URL específica según la entrada del usuario. 
        La función presenta un menú con opciones para realizar la eliminación. 
        Interactúa con el usuario para confirmar la eliminación y maneja elegantemente las entradas inválidas. 
        Una vez que se realiza la eliminación, guarda los datos actualizados en un archivo.
        """

        # Comprueba si el diccionario de URLs no contiene información
        if not self.diccionario['Urls']:
            print(
                Fore.GREEN + '\nEl fichero todavía no contiene ningún registro.' + Fore.RESET)
            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)
            return

        print(Fore.BLUE + '\n>== Menú para eliminación de registros ==<' + Fore.RESET)
        print(Fore.YELLOW + '\n[1]' + Fore.RESET +
              ' Borrar una URL y todos sus registros.')
        print(Fore.YELLOW + '[2]' + Fore.RESET +
              ' Borrar un Usuario específico de una URL específica.')

        opcion = input(
            Fore.YELLOW + '\nIntroduce una opción o presiona ENTER para cancelar y regresar al Menu Principal: ' + Fore.RESET)

        # Comprueba si se ha presionado ENTER y cancela la operación para regresar al menú
        if opcion == '':
            return

        if opcion == '1':
            print(Fore.BLUE + '\n>== Listado de URLS ==<\n' + Fore.RESET)
            urls = list(self.diccionario['Urls'].keys())
            for indice, url in enumerate(urls, start=1):
                print(Fore.YELLOW + f'{indice} - ' + Fore.RESET + f'{url}')

            try:
                url_idx = int(
                    input(Fore.YELLOW + '\nIntroduce el índice de la URL que deseas eliminar: ' + Fore.RESET))
                confirmar = input(
                    Fore.YELLOW + '\nSe va a proceder a eliminar la URL junto con todos sus usuarios. Esta completamente seguro? ' + Fore.RED + '(Si/No) ' + Fore.RESET).lower().strip()

                if confirmar == 'si':
                    if 1 <= url_idx <= len(urls):
                        url = urls[url_idx - 1]
                        del self.diccionario['Urls'][url]
                        print(
                            Fore.GREEN + '\nLa URL y todos sus registros han sido eliminados correctamente... ' + Fore.RESET)
                    else:
                        print(Fore.GREEN + '\nÍndice no válido.' + Fore.RESET)
                else:
                    print(Fore.GREEN + '\nOperacion candelada.' + Fore.RESET)
                    input(
                        Fore.YELLOW + '\nPulse ENTER para regresar al menu... ' + Fore.RESET)
                    return
            except ValueError:
                print(Fore.GREEN + '\nEntrada no válida.' + Fore.RESET)

            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

        elif opcion == '2':
            print(Fore.BLUE + '\n>== Listado de URLS ==<\n' + Fore.RESET)
            urls = list(self.diccionario['Urls'].keys())

            for indice, url in enumerate(urls, start=1):
                print(Fore.YELLOW + f'{indice} - ' + Fore.RESET + f'{url}')

            try:
                url_idx = int(
                    input(Fore.YELLOW + '\nIntroduce el índice de la URL donde se encuentra el usuario: ' + Fore.RESET))
                if 1 <= url_idx <= len(urls):
                    url = urls[url_idx - 1]

                    print(
                        Fore.BLUE + f'\n== Lista de usuarios almacenados en la URL {url} ==\n' + Fore.RESET)

                    for indice, usuario in enumerate(self.diccionario['Urls'][url], start=1):
                        print(Fore.YELLOW + f'{indice} - ' +
                              Fore.RESET + f'{usuario["Usuario"]}')

                    usuario_idx = int(
                        input(Fore.YELLOW + '\nIntroduce el índice del usuario que deseas eliminar: ' + Fore.RESET))

                    if 1 <= usuario_idx <= len(self.diccionario['Urls'][url]):
                        del self.diccionario['Urls'][url][usuario_idx - 1]
                        print(
                            Fore.GREEN + '\nUsuario eliminado correctamente... ' + Fore.GREEN)
                    else:
                        print(Fore.GREEN + '\nÍndice no válido.')
                else:
                    print(Fore.GREEN + '\nÍndice no válido.')
            except ValueError:
                print(Fore.GREEN + '\nEntrada no válida.')

            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

        else:
            print(Fore.GREEN + '\nOpción no válida.' + Fore.RESET)
            input(Fore.YELLOW + '\nPulse ENTER para regresar al menú... ' + Fore.RESET)

        self.save_to_file()

    def save_to_file(self):
        """Guardar el diccionario de passwords en un archivo JSON encriptado."""

        encrypted_data = self.cipher.encrypt(
            json.dumps(self.diccionario).encode())

        with open(self.file_path, 'wb') as file:
            file.write(encrypted_data)

    def load_from_file(self):
        """
        Carga el diccionario de contraseñas desde un archivo JSON cifrado.

        Esta función verifica si existe el archivo especificado por `self.file_path`. Si existe, abre el archivo en modo binario y lee su contenido. Luego, el contenido cifrado se descifra utilizando el objeto `self.cipher` y los datos descifrados se cargan en el atributo `self.diccionario` como un objeto JSON.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Nada
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            self.diccionario = json.loads(decrypted_data)

    def menu(self):
        """
        Muestra una interfaz de menú para la aplicación de gestión de contraseñas.
        Permite al usuario elegir entre varias opciones, como crear un nuevo registro con una contraseña aleatoria, crear manualmente un nuevo registro, listar registros, buscar una contraseña, eliminar un registro o salir de la aplicación.
        """

        while True:
            self.limpiar_consola()
            print(Fore.RED + r"""
   ___   ________________  ___    ___  ____  ___  ___   _________      ______  ___  ___  ____
  / _ | / __/ __/ __/ __ \/ _ \  / _ \/ __/ / _ \/ _ | / __/ __/ | /| / / __ \/ _ \/ _ \/ __/
 / __ |_\ \/ _/_\ \/ /_/ / , _/ / // / _/  / ___/ __ |_\ \_\ \ | |/ |/ / /_/ / , _/ // /\ \  
/_/ |_/___/___/___/\____/_/|_| /____/___/ /_/  /_/ |_/___/___/ |__/|__/\____/_/|_/____/___/  
""" + Fore.RESET)
            print(Fore.BLUE + '>== Menu Principal ==<\n')
            print(Fore.YELLOW + '[1]' + Fore.RESET +
                  ' Crear un nuevo registro con una contraseña generada aleatoriamente')
            print(Fore.YELLOW + '[2]' + Fore.RESET +
                  ' Crear un nuevo registro de forma manual')
            print(Fore.YELLOW + '[3]' + Fore.RESET + ' Listar registros')
            print(Fore.YELLOW + '[4]' + Fore.RESET + ' Buscar contraseña')
            print(Fore.YELLOW + '[5]' +
                  Fore.RESET + ' Eliminar un registro')
            print(Fore.YELLOW + '[6]' + Fore.RESET + ' Salir\n')

            opcion = input(
                Fore.YELLOW + 'Seleccione una opción: ' + Fore.RESET)

            if opcion == '1':
                self.crear_registro()
            elif opcion == '2':
                self.crear_registro_manual()
            elif opcion == '3':
                self.listar_registros()
            elif opcion == '4':
                self.buscar_password()
            elif opcion == '5':
                self.eliminar_registro()
            elif opcion == '6':
                print(Fore.GREEN + '\nSaliendo del gestor de passwords. Hasta pronto!!')
                break
            else:
                print(
                    Fore.GREEN + '\nOpción no válida, por favor seleccione una opción válida.' + Fore.RESET)
                input(Fore.YELLOW +
                      '\nPulse ENTER para regresar al menú... ' + Fore.RESET)


if __name__ == '__main__':
    generador = GeneradorPassword()  # Crea una instancia de la clase
    generador.limpiar_consola()  # Limpia la consola
    generador.load_from_file()  # Cargar el diccionario de passwords desde el archivo JSON

    # Verifica que la contraseña introducida sea correcta y en ese caso accedemos a la aplicación
    if generador.verificar_contraseña():
        generador.menu()
