# -*- coding = utf-8 -*-
# @Time : 2024/12/30 20:43
# @Author : guohexing
# @Fire : 1_封装练习.py
# @Software : PyCharm
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}的体重为{self.weight}kg"

    def run(self):
        self.weight -= 1
        print(f"{self.name}正在奔跑体重为{self.weight}kg")

    def eat(self):
        self.weight += 1
        print(f"{self.name}正在吃东西体重为{self.weight}kg")


daxiang = Person("大象", 50)
print(daxiang)
daxiang.run()
daxiang.eat()
laohu = Person("老虎", 60)
print(laohu)
laohu.run()
laohu.eat()
