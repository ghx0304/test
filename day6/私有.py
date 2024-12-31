# -*- coding = utf-8 -*-
# @Time : 2024/12/30 21:51
# @Author : guohexing
# @Fire : 私有.py
# @Software : PyCharm

class Women():
    def __init__(self,name):
        self.name = name
        self.__age = 25
    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

xiaoming = Women("小明")
print(xiaoming.get_name())
print(xiaoming.get_age())