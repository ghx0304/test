# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:01
# @Author : guohexing
# @Fire : test.py
# @Software : PyCharm
class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print(f"{self.num1},{self.__num2}")
    def test(self):
        self.__test()
class B(A):
    def __init__(self):
        super().__init__()
b=B()
b.test()
