# -*- coding = utf-8 -*-
# @Time : 2024/12/31 18:53
# @Author : guohexing
# @Fire : 1子类用父类的方法.py
# @Software : PyCharm
class A():
    def __init__(self):
        self.__age = 50

    def get_age(self):
        print("A的年龄是：", self.__age)
        return self.__age


class B(A):
    pass


if __name__ == '__main__':
    b = B()
    b.get_age()
