cd /d %~dp0
cd makescript
python.exe _startme.py

cd ..
::set clientdir=.\mkdata\client\mkdata
::set clienttar=..\..\client\game\assets\script\mkdata
::xcopy %clientdir% %clienttar%  /d /f /s /y

pause
