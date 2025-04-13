echo off

net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo [!] Нет прав администратора. Перезапуск от имени администратора...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
powershell -Command "A"

pause