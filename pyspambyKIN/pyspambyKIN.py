#script by kirieshkainsauce 
#ATTENTION! the author is not responsible for the consequences of using the script on your computer
#made with love <3
import webbrowser
import subprocess
import keyboard
spam = True

def e():
    global spam
    spam = False
keyboard.add_hotkey('Ctrl + D + L + F', e)
   
while spam:
   print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
   subprocess.Popen('C:\\Windows\\System32\\calc.exe') 
   webbrowser.open_new_tab('https://github.com/kirieshkainsauce')