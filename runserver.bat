@echo off
setlocal

set port=1111
set url=http://127.0.0.1:%port%/

start "" "%url%"

call Scripts\activate.bat

python manage.py runserver %port%

pause
