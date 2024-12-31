# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:26
# @Author : guohexing
# @Fire : 异常.py
# @Software : PyCharm
try:
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    c = a / b
    print("结果为：", c)
except ZeroDivisionError:
    print("除数不能为0！")
except ValueError:
    print("输入的不是数字！")
except Exception as e:
    print("未知错误！", e)
