# -*- coding = utf-8 -*-
# @Time : 2024/12/31 19:00
# @Author : guohexing
# @Fire : 2导入重名问题.py
# @Software : PyCharm
from module1 import test1 as module1_test1
from module2 import test1
import module1

'''
有from使用时不用加前缀，直接使用模块名调用函数
没有from使用时需要加前缀.
'''

test1()  # 调用module2中的test1函数
module1.test1()  # 调用module1中的test1函数
test1()  # 调用module2中的test1函数
module1_test1()  # 调用module1中的test1函数
