# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:04
# @Author : guohexing
# @Fire : 单继承.py
# @Software : PyCharm
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + " is eating")
    def run(self):
        print(self.name + " is running")
class Dog(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def bark(self):
        print(self.name + " is barking")

if __name__ == '__main__':
    dog = Dog("Wangcai",'huang')
    print(dog.name)
    print(dog.color)
    dog.eat()
    dog.run()
    dog.bark()