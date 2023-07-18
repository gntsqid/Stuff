@echo off
REM hack to wait 17 seconds before attempting to connect by doing empty pings to self
ping localhost -n 18 > nul 
powershell -NoExit -Command "& {cd 'G:\Scripts'; echo "Hello"; wsl.exe --set-default docker-desktop; wsl 'ls'; wsl ash 'test.sh'; wsl}"
