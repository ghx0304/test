# -*- coding = utf-8 -*-
# @Time : 2024/12/31 20:37
# @Author : guohexing
# @Fire : 3使用包.py
# @Software : PyCharm
import  wd_message
'''
使用包的方法
'''

s =wd_message.send_message.send_message("hello world")
txt = wd_message.receive_message.receive_message(s)
print(txt)