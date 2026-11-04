@echo off
title Tarhadi Digital Gram Server
echo ===================================================
echo     Tarhadi Digital Gram - Starting Server...
echo ===================================================
echo.

cd /d "%~dp0"

if exist "venv\Scripts\python.exe" (
    echo Opening browser at http://127.0.0.1:8000/ ...
    start http://127.0.0.1:8000/
    echo Starting Django server...
    echo Press Ctrl+C to stop the server.
    echo.
    .\venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000
) else (
    echo Error: Virtual environment (venv) not found!
    pause
)
