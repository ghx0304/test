# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:27
# @Author : guohexing
# @Fire : 异常的传递.py
# @Software : PyCharm
def func1():
    return  int(input("请输入一个数字："))

def func2():
    return func1()

try:
    print(func2())
except ValueError:
    print("输入的不是数字！")