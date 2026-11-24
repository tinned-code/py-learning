# ============================================
# 第四课：虚拟环境 + pip
#
# 跑法（在你的终端里）：
#   cd E:\deep\py-learning
#   $env:PATH = "E:\deep\py-learning\.venv\Scripts;$env:PATH"
#   python lesson4.py
# ============================================

# colorama 是我们刚用 pip 装进来的第三方包
# 它不是 Python 自带的，全局环境里没有，只在这个 .venv 里
from colorama import Fore, Style, init

# Windows 上必须调用 init()，否则终端不认颜色代码
init()

print(Fore.MAGENTA + "这行是洋红色的")
print(Fore.GREEN + "这行是绿色的")
print(Fore.YELLOW + "这行是黄色的")
print(Fore.BLUE + "这行是蓝色的（Git 实验加的一行）")
print(Fore.CYAN + "这行是青色")
print(Style.RESET_ALL + "颜色关掉了，恢复正常")

# Fore.XXX 就是一个特殊的字符串，终端看到它就换颜色
# Style.RESET_ALL 是"别再染色了"