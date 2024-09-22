@echo off
REM Überprüfe, ob Python installiert ist
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python ist nicht installiert. Bitte installieren Sie Python von dem MICROSOFT STORE oder der offiziellen Website: https://www.python.org/downloads/
    pause
    exit /b
)

REM Überprüfe, ob Pygame bereits installiert ist
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo Pygame ist nicht installiert. Versuche, es zu installieren...
    pip install pygame
    if %errorlevel% neq 0 (
        echo Fehler beim Installieren von Pygame. Bitte installieren Sie es manuell mit 'pip install pygame'.
        pause
        exit /b
    )
)

REM Starte das Spiel
python Game.py

REM Pause am Ende, falls es Fehler gab
if %errorlevel% neq 0 (
    echo Das Spiel wurde mit einem Fehler beendet.
    pause
)