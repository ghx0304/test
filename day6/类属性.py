# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:20
# @Author : guohexing
# @Fire : 类属性.py
# @Software : PyCharm
class Tool:
    count = 0  # 类属性
    def __init__(self, name):
        self.name=name
        Tool.count += 1  # 类属性的操作
t1 = Tool("刀")
t2 = Tool("锤子")
print(Tool.count)  # 2
print(t1.count)  # 2
print(t2.count)  # 2