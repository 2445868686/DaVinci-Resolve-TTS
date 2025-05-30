#!/usr/bin/env bash
set -e  # 出错即停

# —— 配色定义 ——  
RED='\033[0;31m'  
GREEN='\033[0;32m'  
YELLOW='\033[1;33m'  
BLUE='\033[1;34m'  
CYAN='\033[0;36m'  
BOLD='\033[1m'  
NC='\033[0m'  # 清除颜色  

# —— 函数：打印标题 ——  
print_header() {  
  echo -e "${CYAN}┌────────────────────────────────────┐${NC}"  
  echo -e " ${BOLD}${BLUE}Debug Information${NC}"  
  echo -e "${CYAN}└────────────────────────────────────┘${NC}"  
}

# —— 函数：打印项目（对齐 15 列） ——  
print_item() {  
  printf " ${YELLOW}%-15s${NC}: %s\n" "$1" "$2"  
}

# —— 检测是否在虚拟环境 ——  
if [ -n "$VIRTUAL_ENV" ]; then  
  echo -e "${RED}✖ 检测到 Python 虚拟环境：${VIRTUAL_ENV}${NC}"  
  echo "  请先退出 (deactivate) 后再运行脚本。"  
  exit 1  
fi  
if [ -n "$CONDA_DEFAULT_ENV" ] && [ "$CONDA_DEFAULT_ENV" != "base" ]; then  
  echo -e "${RED}✖ 检测到 Conda 环境：$CONDA_DEFAULT_ENV${NC}"  
  echo "  请先 conda deactivate 后再运行脚本。"  
  exit 1  
fi

# —— 打印调试信息 ——  
MIRROR_URL="https://pypi.tuna.tsinghua.edu.cn/simple"  
print_header  
print_item "Time"      "$(date '+%Y-%m-%d %H:%M:%S')"  
print_item "User"      "$(whoami)"  
print_item "Python"    "$(which python3 2>/dev/null || which python)"  
print_item "PyVersion" "$(python3 --version 2>&1 || python --version 2>&1)"  
print_item "pip"       "$(python3 -m pip --version 2>&1 || python -m pip --version 2>&1)"  
print_item "Mirror"    "$MIRROR_URL"  
echo

# —— 关闭命令回显，留出清爽进度条 ——  
set +x

# —— 安装依赖 ——  
echo -e "${CYAN}➤ 开始安装（包含所有依赖）…${NC}"  
python3 -m pip install \
    -i "$MIRROR_URL" \
    --default-timeout=120 \
    --progress-bar=on \
    requests azure-cognitiveservices-speech edge_tts pypinyin

# —— 完成提示 ——  
echo  
echo -e "${GREEN}✔ 全部安装完成，包含所有依赖！${NC}"
