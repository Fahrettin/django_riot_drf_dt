@echo off
@echo Enter Project name
set /p proj_name=
set building=Building django project %proj_name%
@echo %building%
python ./env/Scripts/django-admin.py startproject %proj_name% .
pause