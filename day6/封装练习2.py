# -*- coding = utf-8 -*-
# @Time : 2024/12/30 20:48
# @Author : guohexing
# @Fire : 封装练习2.py
# @Software : PyCharm
class HouseItem:
    def __init__(self, name, areas):
        self.name = name
        self.areas = areas

    def __str__(self):
        return f"{self.name}占地{self.areas}平方米"
class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.items = []

    def __str__(self):
        return f"{self.house_type}房子，占地{self.area}平方米，空闲{self.free_area}平方米"

    def add_item(self,item:HouseItem):
        if item.areas > self.free_area:
            print("房间已满")
            return
        self.free_area -= item.areas
        print(f"添加{item.name}成功")
        self.items.append(item)

if __name__ == '__main__':

    bed = HouseItem("chuang", 2)
    chest = HouseItem("gui", 1)
    table = HouseItem("zi", 1)
    print(bed)
    print(chest)
    print(table)

    house = House("1室1厅", 40)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)

