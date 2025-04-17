@echo off
echo -------------------------------------
echo  COMPILANDO EJECUTABLE PDF TO IMAGE
echo -------------------------------------
echo.

REM Comprueba que pyinstaller esté instalado
where pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo PyInstaller no está instalado. Instalándolo ahora...
    pip install pyinstaller
)

REM Ejecuta la compilación
pyinstaller --onefile --windowed main.py

echo.
echo -------------------------------------
echo  COMPILACIÓN COMPLETA
echo  El ejecutable se encuentra en: dist\main.exe
echo -------------------------------------
pause
