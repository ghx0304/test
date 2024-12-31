# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:22
# @Author : guohexing
# @Fire : 单例模式.py
# @Software : PyCharm
class MusicPlayer:
    instance = None
    def __new__(cls, *args, **kwargs):

        print("创建对象")

        if cls.instance is None:
            instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("初始化对象")


player1 = MusicPlayer()
player2 = MusicPlayer()
print(id(player1))
print(id(player2))
