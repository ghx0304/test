# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:29
# @Author : guohexing
# @Fire : 抛出异常.py
# @Software : PyCharm
def input_num():
    p = input("请输入一个数字：")
    if len(p) >= 8:
        return p
    print("主动抛出异常！")
    ex = Exception("输入的数字长度不够，请重新输入！")
    raise ex


try:
    num = input_num()
    print("输入的数字是：", num)
except Exception as e:
    print("异常信息：", e)
