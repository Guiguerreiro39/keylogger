@echo off

copy "%CD%/main.exe" "%USERPROFILE%\Start Menu\Programs\Startup"
cd "%USERPROFILE%\Start Menu\Programs\Startup"
start main