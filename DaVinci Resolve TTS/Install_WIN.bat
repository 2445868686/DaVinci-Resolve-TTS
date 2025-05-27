@echo off
color 0A
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "WHEEL_DIR=%SCRIPT_DIR%wheel"
for %%I in ("%SCRIPT_DIR%..\..\..\TTS\Lib") do set "TARGET_DIR=%%~fI"

if not exist "%TARGET_DIR%" (
    echo [*] Creating target directory: "%TARGET_DIR%"
    mkdir "%TARGET_DIR%"
)

rem 扫描
set /A total=0
for %%F in ("%WHEEL_DIR%\*.whl") do set /A total+=1
if !total! equ 0 (
    color 0C
    echo [!] No .whl files found.
    pause
    exit /b 1
)
echo Found !total! wheel files.
echo.

rem 安装
set /A success=0
set /A failed=0
set "failed_list="
for %%F in ("%WHEEL_DIR%\*.whl") do (
    set "fname=%%~nxF"
    echo Installing [%%~nxF] ...
    python -m pip install "%%~fF" --no-deps --target "%TARGET_DIR%" >nul 2>&1
    if errorlevel 1 (
        color 0C
        echo   [FAIL] %%~nxF
        set /A failed+=1
        set "failed_list=!failed_list! %%~nxF"
    ) else (
        color 0A
        echo   [ OK ] %%~nxF
        set /A success+=1
    )
)

echo.
color 0B
echo Summary: Total=!total!  OK=!success!  Fail=!failed!
if !failed! gtr 0 (
    color 0C
    echo Failed packages: !failed_list!
) else (
    color 0A
    echo All succeeded!
)
pause
endlocal
