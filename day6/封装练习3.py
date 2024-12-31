# -*- coding = utf-8 -*-
# @Time : 2024/12/30 20:56
# @Author : guohexing
# @Fire : 封装练习3.py
# @Software : PyCharm
class Gun:
    def __init__(self,model,bullet=0):
        self.model = model
        self.bullet = bullet

    def add_bullet(self,num):
        self.bullet += num

    def shoot(self):
        if self.bullet > 0:
            print("shooting...")
            self.bullet -= 1
        else:
            print("no bullet left")

class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print("no gun")
            return
        print(f"{self.name} han")
        self.gun.add_bullet(10)
        self.gun.shoot()


if __name__ == '__main__':
    gun = Gun("AK-47")
    gun.add_bullet(100)
    soldier1 = Soldier("Tom")
    soldier1.gun = gun
    soldier1.fire()
    soldier2 = Soldier("Jerry")
    soldier2.fire()
    print(soldier1.gun.model)
