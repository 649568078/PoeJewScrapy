import os
import re
import configparser
import tkinter as tk
from tkinter import filedialog

def choose_file(): # 选择文件
    selectFileName = tk.filedialog.askopenfilename(title='选择文件',initialdir ='C:\\Users\\Administrator\\PycharmProjects\\pyautogui-poemakegear\\星团珠宝查价\分析表\\')
    return selectFileName

# 初始化ninja价格信息
cp2 = configparser.RawConfigParser()
cp2.read(r'C:\Users\Administrator\PycharmProjects\pyautogui-poemakegear\ninja价格信息.ini', encoding="utf-8-sig")

# 打开分析文件
file = choose_file()
text = open(file, 'r',encoding='utf-8-sig').readlines()

# 定义珠宝价值最低值
make_price = 80
print("入选价格最低为" + str(make_price))

# 开始循环
final_list = []
for each_list in text:
    each_list = eval(each_list)
    # 定义EX比率
    chao_ex = float(cp2.get("Price", "exalted orb"))
    judge_list = []
    for each in eval(each_list[2]):
        if re.search('([\d|.]*)chaos', each):
            each = float(re.search('([\d|.]*)chaos', each).group(1))
            judge_list.append(each)
        elif re.search('([\d|.]*)exalted', each):
            each = float(re.search('([\d|.]*)exalted', each).group(1))
            # 定义货币统一标准
            each = each * chao_ex
            judge_list.append(each)
    # 去掉第一个最低值，后三个值求平均数，如果去掉第一个值
    if len(judge_list) != 0:
        if len(judge_list) >= 4:
            judge_value = (judge_list[1] + judge_list[2] + judge_list[3]) / 3
        elif len(judge_list) == 1:
            judge_value = judge_list[0]
        else:
            judge_value = 0
            for i in range(1, len(judge_list) + 1):
                judge_value += judge_list[i - 1]
            judge_value = judge_value / len(judge_list)


        if make_price < judge_value:
            final_list.append(eval(each_list[0]))
            print("恭喜" + each_list[0] + "成功入选")
            print(each_list[2])
            print(judge_list)
            print(judge_value)
            print("*" * 50)

print(final_list)
print('数量为:'+str(len(final_list)))
