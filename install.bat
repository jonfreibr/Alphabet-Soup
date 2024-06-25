@echo off
echo Installing Python 3.11.5
python-3.11.5-amd64.exe /passive
echo upgrading pip
%LocalAppData%\Programs\Python\Python311\python.exe -m pip install --upgrade pip
echo Adding package requients
%LocalAppData%\Programs\Python\Python311\Scripts\pip.exe install -r requirements.txt
echo Copying files
if not exist %USERPROFILE%\ASoup md %USERPROFILE%\ASoup
copy /y alphasoup.py %USERPROFILE%\ASoup
copy /y AlphaSoup.lnk %USERPROFILE%\Desktop
echo Done with installation
rem pause
rem exit