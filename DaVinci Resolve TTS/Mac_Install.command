#!/usr/bin/env bash
set -euo pipefail

# ———————— 配置变量 ————————
PYTHON=python3
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WHEEL_DIR="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/TTS/wheel"
TARGET_DIR="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/TTS/Lib"
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
log INFO "Downloading packages: ${PACKAGES[*]} ..."
$PYTHON -m pip download "${PACKAGES[@]}" \
    --dest "$WHEEL_DIR" \
    --only-binary=:all: \
    --use-feature=fast-deps \
    --no-cache-dir \
    --progress-bar=on \
    -i "$PIP_MIRROR" \
  || { log ERROR "Download failed. Check network or mirror settings."; exit 1; }

log SUCCESS "Download completed. Wheels saved to: $WHEEL_DIR"

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
