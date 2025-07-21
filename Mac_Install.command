#!/usr/bin/env bash
set -euo pipefail
# 获取管理员权限
if [ "$EUID" -ne 0 ]; then
  echo "Enter Password："
  exec sudo "$0" "$@"
  exit
fi
# ———————— 配置变量 ————————
PYTHON=python3
SCRIPT_NAME="DaVinci TTS"

WHEEL_DIR="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/HB/$SCRIPT_NAME/wheel"
TARGET_DIR="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/HB/$SCRIPT_NAME/Lib"
PACKAGES=(requests azure-cognitiveservices-speech edge-tts pypinyin)
PIP_MIRROR="https://pypi.tuna.tsinghua.edu.cn/simple"

# ———————— 日志函数 ————————
# 用法：log LEVEL "message"
# LEVEL: INFO, WARN, ERROR, SUCCESS
log() {
  local level="$1"; shift
  local msg="$*"
  local ts
  ts=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$ts][$level] $msg"
}

log INFO "Starting Python wheel offline download & installation."

# ———————— 步骤 1：准备 wheel 下载目录 ————————
log INFO "Preparing wheel download directory: $WHEEL_DIR"
mkdir -p "$WHEEL_DIR"

# ———————— 步骤 2：清理 pip 缓存（可选） ————————
log INFO "Clearing pip cache..."
$PYTHON -m pip cache purge >/dev/null 2>&1 || log WARN "pip cache purge failed or already empty."

# ———————— 步骤 3：下载最新版本的包及依赖 ————————
log INFO "Attempting download from official PyPI..."
if $PYTHON -m pip download "${PACKAGES[@]}" \
    --dest "$WHEEL_DIR" \
    --only-binary=:all: \
    --use-feature=fast-deps \
    --no-cache-dir \
    --progress-bar=on \
    -i https://pypi.org/simple; then
  log SUCCESS "Download succeeded using official PyPI."
else
  log WARN "Official PyPI failed. Trying TUNA mirror..."
  if $PYTHON -m pip download "${PACKAGES[@]}" \
      --dest "$WHEEL_DIR" \
      --only-binary=:all: \
      --use-feature=fast-deps \
      --no-cache-dir \
      --progress-bar=on \
      -i "$PIP_MIRROR"; then
    log SUCCESS "Download succeeded using TUNA mirror."
  else
    log ERROR "Download failed from both official and TUNA mirror. Please check your network."
    exit 1
  fi
fi

# ———————— 步骤 4：创建目标目录 & 修复权限 ————————
log INFO "Preparing target installation directory: $TARGET_DIR"
sudo mkdir -p "$TARGET_DIR"
sudo chown -R "$(whoami)" "$TARGET_DIR"
log SUCCESS "Target directory ready and owned by $(whoami)."

# ———————— 步骤 5：离线安装指定的包及其依赖 ————————
log INFO "Installing specified packages offline..."
if $PYTHON -m pip install "${PACKAGES[@]}" \
     --no-index \
     --find-links "$WHEEL_DIR" \
     --target "$TARGET_DIR"; then
  log SUCCESS "Successfully installed specified packages and their dependencies."
else
  log ERROR "Offline installation of specified packages failed. Please check wheels and permissions."
  exit 1
fi

# ———————— 步骤 6：安装汇总 ————————
log INFO "Installation process completed. Please verify modules in $TARGET_DIR."
log SUCCESS "All done."