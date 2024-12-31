# -*- coding = utf-8 -*-
# @Time : 2024/12/30 21:58
# @Author : guohexing
# @Fire : 继承.py
# @Software : PyCharm
class Animal:
    def eat(self):
        print("动物吃东西")

    def drink(self):
        print("动物喝水")

    def run(self):
        print("动物跑")

    def sleep(self):
        print("动物睡觉")


class Dog(Animal):
    def bark(self):
        print("狗叫")

    def eat(self):
        print("狗吃骨头")


class XiaoTianQuan(Dog):
    def fly(self):
        print("xiaotianquan飞")

    def bark(self):
        print("xiaotianquan叫")
        super().bark()



wangcai = Dog()
wangcai.bark()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
xiaotianquan = XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.bark()
