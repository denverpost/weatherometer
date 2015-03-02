@echo off
if %1 == runserver python manage.py runserver :80
if %1 == resetw python manage.py reset forecast
if %1 == resetf python manage.py reset forecaster
if %1 == shell python manage.py shell
if %1 == dump python db_dump.py dump
if %1 == load python db_dump.py load
if %1 == loadw python db_dump.py load forecast
if %1 == loadf python db_dump.py load forecaster
if %1 == update python manage.py updatetempdiff
if %1 == updateacc python manage.py updateaccuracy
if %1 == sync python manage.py syncdb
echo.
echo Done
echo.