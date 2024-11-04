set dir=%APPDATA%\dcalc\Cache
echo %dir%
rd /s /Q %dir%
netsh winsock reset
pause