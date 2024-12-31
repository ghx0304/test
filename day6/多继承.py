# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:06
# @Author : guohexing
# @Fire : 多继承.py
# @Software : PyCharm
class A:
    def test(self):
        print("A test")
    def demo(self):
        print("A demo")
class B:
    def test(self):
        print("B test")
    def demo(self):
        print("B demo")

class C(A, B):
    pass

c = C()
c.test()
c.demo()
print(C.__mro__)
