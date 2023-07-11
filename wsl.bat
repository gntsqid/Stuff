@echo off
powershell -NoExit -Command "& {cd 'G:\Scripts'; echo "Hello"; wsl.exe --set-default docker-desktop; wsl 'ls'; wsl ash 'test.sh'; wsl}"
