cd /d %~dp0
set tar=
copy *.pyc %tar%
cd %tar%
TortoiseProc.exe /command:commit /path:"."  /logmsg:"no log message engine" /closeonend:1
pause