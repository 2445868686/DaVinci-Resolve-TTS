@echo off
REM -----------------------------------------------------
REM  Python wheel Offline Download & Installation Script
REM  1. Download latest packages and dependencies
REM  2. Install into Fusion TTS directory
REM -----------------------------------------------------

:: —— Variables ——  
setlocal enabledelayedExpansion
set "SCRIPT_DIR=%~dp0"
set "WHEEL_DIR=%SCRIPT_DIR%wheel"
set "TARGET_DIR=C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\TTS\Lib"
set "PACKAGES=requests azure-cognitiveservices-speech edge-tts pypinyin"
set "PIP_MIRROR=-i https://pypi.tuna.tsinghua.edu.cn/simple"

:: —— Helper: log with timestamp and level ——  
rem Usage: echo [%DATE% %TIME%][LEVEL] Message
:: —— Start ——  
echo.
echo [%DATE% %TIME%][INFO] Python wheel offline download & installation started.
echo.

:: —— Step 1: Prepare wheel directory ——  
if not exist "%WHEEL_DIR%" (
    echo [%DATE% %TIME%][INFO] Creating wheel download directory: "%WHEEL_DIR%"
    mkdir "%WHEEL_DIR%"
) else (
    echo [%DATE% %TIME%][INFO] Wheel directory already exists: "%WHEEL_DIR%"
)

:: —— Step 2: Purge pip cache ——  
echo [%DATE% %TIME%][INFO] Clearing pip cache to avoid corrupted files...
python -m pip cache purge >nul 2>&1

:: —— Step 3: Download packages with progress bar ——  
echo.
echo [%DATE% %TIME%][INFO] Downloading packages: %PACKAGES% ...
python -m pip download %PACKAGES% --no-cache-dir --dest "%WHEEL_DIR%" ^
    --only-binary=:all: --use-feature=fast-deps --disable-pip-version-check ^
    --progress-bar=on %PIP_MIRROR%
if errorlevel 1 (
    echo [%DATE% %TIME%][ERROR] Download failed. Check network or mirror settings.
    pause
    exit /b 1
) else (
    echo [%DATE% %TIME%][SUCCESS] Download completed. Wheels saved to "%WHEEL_DIR%".
)

:: —— Step 4: Prepare target install directory ——  
echo.
echo [%DATE% %TIME%][INFO] Preparing installation directory: "%TARGET_DIR%"
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
    echo [%DATE% %TIME%][INFO] Created "%TARGET_DIR%".
) else (
    echo [%DATE% %TIME%][INFO] Directory already exists.
)

:: —— Step 5: Count wheel files ——  
set /A total=0
for %%F in ("%WHEEL_DIR%\*.whl") do set /A total+=1
if !total! equ 0 (
    echo [%DATE% %TIME%][ERROR] No .whl files found in "%WHEEL_DIR%". Aborting.
    pause
    exit /b 1
)
echo [%DATE% %TIME%][INFO] Found !total! wheel package(s) to install.
echo.

:: —— Step 6: Offline install each wheel ——  
set /A success=0, failed=0
set "failed_list="
for %%F in ("%WHEEL_DIR%\*.whl") do (
    set "fname=%%~nxF"
    echo [%DATE% %TIME%][INFO] Installing !fname! ...
    python -m pip install "%%~fF" --no-deps --target "%TARGET_DIR%" --disable-pip-version-check >nul 2>&1
    if errorlevel 1 (
        echo [%DATE% %TIME%][ERROR] Failed to install !fname!
        set /A failed+=1
        set "failed_list=!failed_list! !fname!"
    ) else (
        echo [%DATE% %TIME%][SUCCESS] Installed !fname!
        set /A success+=1
    )
)

:: —— Step 7: Summary ——  
echo.
echo [%DATE% %TIME%][INFO] Installation summary: Total=!total!  Success=!success!  Failed=!failed!
if !failed! gtr 0 (
    echo [%DATE% %TIME%][WARN] Failed packages:!failed_list!
) else (
    echo [%DATE% %TIME%][SUCCESS] All packages installed successfully!
)
pause
endlocal
