"""
这是一个执行循环打印功能的程序，虽然没什么用
This is a program that performs circular printing function,It's useless, though

Author: ReWhite
Date: 2023.10.22
"""

import time
import sys
import select
from datetime import datetime, timedelta

# ANSI 转义序列，用于设置文本颜色
YELLOW = "\033[33m"
RESET = "\033[0m"

print(f"{YELLOW}程序启动中...{RESET}", end="")
sys.stdout.flush()  # 确保及时显示

time.sleep(1)  # 延迟一秒

print(f"{YELLOW}完成{RESET}")
sys.stdout.flush()  # 确保及时显示

is_running = True
count = 0
sleep_interval = 3  # 默认打印间隔
text = "Hello World"  # 默认打印内容
end_count = None

while is_running:
    count += 1
    current_time = (datetime.utcnow() + timedelta(hours=8)).strftime("%H:%M:%S")  # 当前时间（UTC+8），只显示时分秒
    
    print(f"{count}. {text} - {current_time}")
    sys.stdout.flush()  # 刷新输出缓冲区，确保及时显示
    
    time.sleep(sleep_interval)
    
    if end_count is not None and count >= end_count:
        print(f"{YELLOW}已达到指定循环次数 {end_count} 次，程序结束{RESET}")
        break
    
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.readline().strip()
        
        if user_input.lower() == "stop":
            print(f"{YELLOW}已停止运行{RESET}")
            is_running = False
        
        elif user_input.lower() == "reload":
            print(f"{YELLOW}正在重新载入...{RESET}")
            exec(open(__file__).read())  # 重新执行当前文件
            sys.exit()  # 终止当前程序的执行
        
        elif user_input.startswith("sleep"):
            _, _, argument = user_input.partition(' ')
            try:
                sleep_interval = float(argument)
                print(f"{YELLOW}已设置打印间隔为 {sleep_interval} 秒{RESET}")
            except ValueError:
                print(f"{YELLOW}无效的参数，请输入一个数字{RESET}")
        
        elif user_input.startswith("text"):
            _, _, argument = user_input.partition(' ')
            text = argument
            print(f"{YELLOW}已设置打印内容为 '{text}'{RESET}")
        
        elif user_input.startswith("end"):
            _, _, argument = user_input.partition(' ')
            try:
                end_count = int(argument)
                print(f"{YELLOW}已设置循环次数为 {end_count} 次{RESET}")
            except ValueError:
                print(f"{YELLOW}无效的参数，请输入一个整数{RESET}")
        
        elif user_input.lower() == "list":
            print(f"{YELLOW}可用命令列表：{RESET}")
            print(f"{YELLOW}｜{RESET}1. stop - 停止运行程序")
            print(f"{YELLOW}｜{RESET}2. reload - 重新载入程序")
            print(f"{YELLOW}｜{RESET}3. sleep 参数 - 设置打印间隔（单位为秒）")
            print(f"{YELLOW}｜{RESET}4. text 参数 - 设置打印内容（参数为文本）")
            print(f"{YELLOW}｜{RESET}5. end 参数 - 设置循环次数（参数为整数）")
            print(f"{YELLOW}｜{RESET}6. list - 列出命令列表")
