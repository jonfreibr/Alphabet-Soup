@echo off
setlocal enabledelayedexpansion
title Install Alphabet Soup Acronym Tool
echo Sourcing from: %~dp0

set "TARGET_VER=3.11.5"
set "PYTHON_SOURCE_DIR=Python311"

:: Prevent early exit on errors
set "ERRORFLAG=0"

echo Checking for existing Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found.
    set "INSTALL=TRUE"
) else (
    for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set "VERSION=%%a"
    if !VERSION! equ !TARGET_VER! (
	echo Python %TARGET_VER% already installed
	set "INSTALL=FALSE"
    ) else (
	echo Python !VERSION! installed. Installing required version %TARGET_VER%
	set "INSTALL=TRUE"
    )
)

if "%INSTALL%" equ "TRUE" (
	"%~dp0\python-%TARGET_VER%-amd64.exe" /passive
	set "PYTHON_PATH=%LocalAppData%\Programs\Python\%PYTHON_SOURCE_DIR%\python.exe"
)

set "PROJECT_DIR=%USERPROFILE%\ASoup"
set "VENV_DIR=%PROJECT_DIR%\venv"
set "DESKTOP_DIR=%USERPROFILE%\Desktop"

echo Creating project folder...
if not exist "%PROJECT_DIR%" md "%PROJECT_DIR%"

echo Creating virtual environment...
call "%PYTHON_PATH%" -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment.
    set "ERRORFLAG=1"
    goto :END
)
echo Virtual environment created at: %VENV_DIR%

echo Activating virtual environment and upgrading pip...
call "%VENV_DIR%\Scripts\activate.bat"
call python -m pip install --upgrade pip

if exist "%~dp0\requirements.txt" (
    echo Installing required Python packages in venv...
    call python -m pip install -r "%~dp0\requirements.txt"
    call python -m pip install -i https://PySimpleGUI.net/install PySimpleGUI
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install dependencies.
        set "ERRORFLAG=1"
        goto :END
    )
) else (
    echo No requirements.txt found — skipping dependency install.
)

echo Copying files
copy /y "%~dp0\alphasoup.py" %PROJECT_DIR%
echo Finished copying files

echo Deactivating virtual environment...
call deactivate

echo Creating desktop shortcut...
set "SHORTCUT_PATH=%USERPROFILE%\Desktop\AlphaSoup.lnk"
set "TARGET_PATH=%PROJECT_DIR%\alphasoup.py"
set "WORKING_DIR=%PROJECT_DIR%"
set "ICON_PATH=%~dp0\icon.ico"

powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command ^
  "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT_PATH%');" ^
  "$s.TargetPath='%VENV_DIR%\Scripts\pythonw.exe';" ^
  "$s.Arguments='\"%TARGET_PATH%\"';" ^
  "$s.WorkingDirectory='%WORKING_DIR%';" ^
  "if (Test-Path '%ICON_PATH%') {$s.IconLocation='%ICON_PATH%'};" ^
  "$s.Save()"
if %errorlevel% neq 0 (
    copy /y "%~dp0\AlphaSoup.lnk" "%DESKTOP_DIR%"
    :: echo WARNING: Could not create desktop shortcut.
    echo Shortcut copied.
) else (
    echo Shortcut created successfully.
)
echo.

echo Launching Insurance Query Tool...
start "" "%SHORTCUT_PATH%"
echo.

:END
if %ERRORFLAG% neq 0 (
    echo.
    echo ===============================
    echo   INSTALLATION FAILED 
    echo ===============================
    pause
) else (
    echo.
    echo ===============================
    echo   INSTALLATION COMPLETE 
    echo ===============================
    timeout /t 5
)
