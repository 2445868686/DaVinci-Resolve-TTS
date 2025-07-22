@echo off
chcp 65001 >nul
setlocal enabledelayedExpansion

rem ======== Variables (modify as needed) ========
set "PYTHON=python"
set "SCRIPT_NAME=DaVinci TTS"
set "WHEEL_DIR=C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\HB\%SCRIPT_NAME%\wheel"
set "TARGET_DIR=C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\HB\%SCRIPT_NAME%\Lib"
rem All required packages
set "PACKAGES=requests azure-cognitiveservices-speech edge-tts pypinyin"
rem Tsinghua mirror for faster downloads (remove if not needed)
set "PIP_MIRROR=-i https://pypi.tuna.tsinghua.edu.cn/simple"
rem =============================================

echo.
echo [%DATE% %TIME%] Starting download and offline installation of dependencies
echo ------------------------------------------------------------

rem 1. Create wheel directory if it does not exist
if not exist "%WHEEL_DIR%" (
    echo [%DATE% %TIME%] Creating wheel download directory: "%WHEEL_DIR%"
    mkdir "%WHEEL_DIR%"
) else (
    echo [%DATE% %TIME%] Wheel download directory already exists: "%WHEEL_DIR%"
)

rem 2. Clear pip cache to avoid potential corruption
echo [%DATE% %TIME%] Clearing pip cache
python -m pip cache purge --disable-pip-version-check

rem 3. Try download from official PyPI first
echo.
echo [%DATE% %TIME%] Attempting to download from official PyPI...
python -m pip download %PACKAGES% --dest "%WHEEL_DIR%" --only-binary=:all: ^
    --use-feature=fast-deps --no-cache-dir -i https://pypi.org/simple
if errorlevel 1 (
    echo [%DATE% %TIME%] WARNING: Failed to download from official PyPI. Trying TUNA mirror...
    python -m pip download %PACKAGES% --dest "%WHEEL_DIR%" --only-binary=:all: ^
        --use-feature=fast-deps --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple
    if errorlevel 1 (
        echo [%DATE% %TIME%] ERROR: Failed to download packages from both sources. Check your network or package names.
        pause & exit /b 1
    ) else (
        echo [%DATE% %TIME%] SUCCESS: Packages downloaded via TUNA mirror to "%WHEEL_DIR%"
    )
) else (
    echo [%DATE% %TIME%] SUCCESS: Packages downloaded via official PyPI to "%WHEEL_DIR%"
)

rem 4. Create target installation directory if it does not exist
if not exist "%TARGET_DIR%" (
    echo [%DATE% %TIME%] Creating target installation directory: "%TARGET_DIR%"
    mkdir "%TARGET_DIR%"
) else (
    echo [%DATE% %TIME%] Target installation directory already exists: "%TARGET_DIR%"
)

rem 5. Perform offline installation of all packages
echo.
echo [%DATE% %TIME%] Installing packages offline into: "%TARGET_DIR%"
python -m pip install %PACKAGES% --no-index --find-links "%WHEEL_DIR%" ^
    --target "%TARGET_DIR%" --upgrade --disable-pip-version-check
if errorlevel 1 (
    echo [%DATE% %TIME%] ERROR: Offline installation failed. Please review the errors above.
    pause & exit /b 1
)

echo.
echo [%DATE% %TIME%] SUCCESS: All packages have been installed successfully!
pause
endlocal