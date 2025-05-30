@echo off
REM =============== 出错即停 ===============
setlocal enabledelayedexpansion

REM =============== 配色定义 ===============
for /f "delims=" %%A in ('echo prompt $E ^| cmd') do set "ESC=%%A"
set "RED=%ESC%[31m"
set "GREEN=%ESC%[32m"
set "YELLOW=%ESC%[33m"
set "BLUE=%ESC%[34m"
set "CYAN=%ESC%[36m"
set "BOLD=%ESC%[1m"
set "NC=%ESC%[0m"

REM ===== 检测是否在虚拟环境或 Conda 环境 =====
if defined VIRTUAL_ENV (
  echo %RED%✖ 检测到 Python 虚拟环境： %VIRTUAL_ENV% %NC%
  echo   请先退出 (deactivate) 后再运行脚本。
  exit /b 1
)
if defined CONDA_DEFAULT_ENV (
  if not "%CONDA_DEFAULT_ENV%"=="base" (
    echo %RED%✖ 检测到 Conda 环境： %CONDA_DEFAULT_ENV% %NC%
    echo   请先 conda deactivate 后再运行脚本。
    exit /b 1
  )
)

REM =============== 打印调试信息 ===============
set "MIRROR_URL=https://pypi.tuna.tsinghua.edu.cn/simple"

echo %CYAN%┌────────────────────────────────────┐%NC%
echo  %BOLD%%BLUE%Debug Information%NC%
echo %CYAN%└────────────────────────────────────┘%NC%

call :print_item Time      "%DATE% %TIME%"
call :print_item User      "%USERNAME%"

REM 获取 python 可执行路径
for /f "delims=" %%p in ('where python 2^>nul') do (
  set "PYTHON_PATH=%%p"
  goto :got_python
)
:got_python
call :print_item Python    "%PYTHON_PATH%"

REM 获取 Python 版本
for /f "delims=" %%v in ('"%PYTHON_PATH% --version"') do set "PY_VER=%%v"
call :print_item PyVersion "%PY_VER%"

REM 获取 pip 版本
for /f "delims=" %%v in ('"%PYTHON_PATH% -m pip --version"') do set "PIP_VER=%%v"
call :print_item pip       "%PIP_VER%"

call :print_item Mirror    "%MIRROR_URL%"
echo.

REM =============== 安装依赖 ===============
echo %CYAN%➤ 开始安装（包含所有依赖）…%NC%
"%PYTHON_PATH%" -m pip install ^
    -i "%MIRROR_URL%" ^
    --default-timeout=120 ^
    --progress-bar=on ^
    requests azure-cognitiveservices-speech edge_tts pypinyin

echo.
echo %GREEN%✔ 全部安装完成，包含所有依赖！%NC%

endlocal
goto :EOF

:print_item
REM %1=标签, %2=内容，标签宽度固定15字符
setlocal DisableDelayedExpansion
set "name=%~1"
set "value=%~2"
set "pad=               "  REM 15个空格
set "padded=%name%%pad%"
set "padded=%padded:~0,15%"
endlocal & set "padded=%padded%"
echo  %YELLOW%%padded%%NC%: %value%
goto :EOF
