#!/usr/bin/env bash
#
# Mac_Install.command
# 将当前目录下 wheel/*.whl 和 wheel/*.tar.gz 安装到指定目录
# 输出格式按要求显示，并屏蔽 pip notice

# 1. 获取脚本所在目录（兼容路径中含空格）
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 2. wheel 包所在目录
WHEEL_DIR="$SCRIPT_DIR/wheel"

# 3. 目标目录 (MODIFIED TO ABSOLUTE PATH)
TARGET_DIR="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/TTS/Lib"

# 4. 查找可用的 Python 解释器
PYTHON_CMD="$(command -v python3 2>/dev/null || command -v python 2>/dev/null)"
if [[ -z "$PYTHON_CMD" ]]; then
    echo "ERROR: 未找到 python3 或 python，请先安装并确保在 PATH 中。"
    exit 1
fi

# 5. 收集所有 .whl 和 .tar.gz 文件到数组
pkg_files=()
# Ensure glob doesn't return literal string if no files match
shopt -s nullglob
for f in "$WHEEL_DIR"/*.whl "$WHEEL_DIR"/*.tar.gz; do
    pkg_files+=("$f")
done
shopt -u nullglob # Revert nullglob

# 6. 输出总数
if [ ${#pkg_files[@]} -eq 0 ]; then
    echo "No .whl or .tar.gz files found in \"$WHEEL_DIR\"."
    exit 0
fi
echo "Found ${#pkg_files[@]} package files (whl/tar.gz)."
echo

# 7. 确保目标目录存在
mkdir -p "$TARGET_DIR"
if [ $? -ne 0 ]; then
    echo "ERROR: 创建目标目录失败: $TARGET_DIR"
    echo "请检查权限或路径是否正确。"
    exit 1
fi
echo "[*] Target directory: \"$TARGET_DIR\""
echo

# 8. 按指定格式逐个安装
for pkg in "${pkg_files[@]}"; do
    name="$(basename "$pkg")"
    printf "Installing [%s] ...\n" "$name"
    if "$PYTHON_CMD" -m pip install "$pkg" \
            --no-deps --target="$TARGET_DIR" \
            --disable-pip-version-check -q >/dev/null 2>&1; then
        printf "  [ OK ] %s\n\n" "$name"
    else
        printf "  [FAIL] %s\n\n" "$name"
        echo "   >> 请检查错误日志，或尝试手动安装:"
        echo "   >> $PYTHON_CMD -m pip install \"$pkg\" --no-deps --target=\"$TARGET_DIR\""
    fi
done

echo "All done."
exit 0
