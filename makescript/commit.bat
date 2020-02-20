cd /d %~dp0
TortoiseProc.exe /command:commit /path:"."  /logmsg:"no log message engine" /closeonend:1
::TortoiseProc.exe /command:commit /path:"E:\code\work\svn-root\game\allgame\tafang\server\skynet\tools\py_serverlua_makescript"  /logmsg:"no log message engine" /closeonend:1

TortoiseProc.exe /command:update /path:"."  /logmsg:"no log message engine" /closeonend:1