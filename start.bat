@echo off
set /p choice="Start the web server on port 8000? (Y/N) [Y]: "

if "%choice%"=="" set choice=Y

if /i "%choice%"=="Y" (
    echo Starting web server on port 8000...
    python -m http.server 8000
    goto :EOF
)

set /p port="Enter the port you want to use: "
if not "%port%"=="" (
    echo Starting web server on port %port%...
    python -m http.server %port%
) else (
    echo Invalid input. Exiting.
)

:EOF