# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:09
# @Author : guohexing
# @Fire : 多态.py
# @Software : PyCharm
class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print(self.name + " is playing with ball")


class XiaoTianQuan(Dog):
    def game(self):
        print(self.name + " is playing with ball and running")


class Penson():
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(f"{self.name} is playing with {dog.name}")
        dog.game()
w = Dog("wangcai")
x = XiaoTianQuan("xiaotianquan")
p = Penson("penson")
p.game_with_dog(w)
p.game_with_dog(x)
