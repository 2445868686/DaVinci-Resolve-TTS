@echo off
color 0A
setlocal enabledelayedexpansion

rem -------- 配置目录 --------
set "SCRIPT_DIR=%~dp0"
set "WHEEL_DIR=%SCRIPT_DIR%wheel"
for %%I in ("%SCRIPT_DIR%..\..\..\TTS\Lib") do set "TARGET_DIR=%%~fI"

if not exist "%TARGET_DIR%" (
    echo [*] Creating target directory: "%TARGET_DIR%"
    mkdir "%TARGET_DIR%"
)

rem -------- 扫描 .whl 和 .tar.gz 包 --------
set /A total=0
for %%F in ("%WHEEL_DIR%\*.whl" "%WHEEL_DIR%\*.tar.gz") do (
    if exist "%%~fF" (
        set /A total+=1
    )
)
if !total! equ 0 (
    color 0C
    echo [!] No .whl or .tar.gz files found in "%WHEEL_DIR%".
    pause
    exit /b 1
)
echo Found !total! package files (.whl/.tar.gz).
echo.

rem -------- 安装循环 --------
set /A success=0
set /A failed=0
set "failed_list="

for %%F in ("%WHEEL_DIR%\*.whl" "%WHEEL_DIR%\*.tar.gz") do (
    if exist "%%~fF" (
        set "fname=%%~nxF"
        echo Installing [!fname!] ...
        python -m pip install "%%~fF" --no-deps --target "%TARGET_DIR%" --disable-pip-version-check >nul 2>&1
        if errorlevel 1 (
            color 0C
            echo   [FAIL] !fname!
            set /A failed+=1
            set "failed_list=!failed_list! !fname!"
        ) else (
            color 0A
            echo   [ OK ] !fname!
            set /A success+=1
        )
    )
)

rem -------- 安装汇总 --------
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
