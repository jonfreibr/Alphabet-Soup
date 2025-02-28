@echo off
echo Installing Python 3.11.5
%~dp0\python-3.11.5-amd64.exe /passive
echo upgrading pip
%LocalAppData%\Programs\Python\Python311\python.exe -m pip install --upgrade pip -q
echo Adding package requients
%LocalAppData%\Programs\Python\Python311\Scripts\pip.exe install -r %~dp0\requirements.txt -q
%LocalAppData%\Programs\Python\Python311\Scripts\pip.exe install -i https://PySimpleGUI.net/install PySimpleGUI -q
echo Copying files
if not exist %USERPROFILE%\ASoup md %USERPROFILE%\ASoup
copy /y %~dp0\alphasoup.py %USERPROFILE%\ASoup
copy /y %~dp0\AlphaSoup.lnk %USERPROFILE%\Desktop
start $USERPROFILE%\Desktop\AlphaSoup.lnk