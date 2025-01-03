# -*- coding = utf-8 -*-
# @Time : 2025/1/2 20:17
# @Author : guohexing
# @Fire : 堆排序.py
# @Software : PyCharm
import random
import time


class Sort():
    def __init__(self, n):
        '''
        初始化排序列表
        :param n: 排序的列表长度
        '''
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 1000)

    def adjust_heap(self, pos, arr_len):
        '''
        调整堆
        :param arr: 需要调整的数组
        :param pos: 堆的根节点
        :param arr_len: 堆的大小
        :return:
        '''
        arr = self.arr
        dad = pos
        son = 2 * pos + 1
        while son < arr_len:  # 左孩子下标小于堆的长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 如果有右孩子且右孩子大于左孩子，则son指向右孩子
                son += 1
            if arr[son] > arr[dad]:  # 如果son节点的值大于dad节点的值，则交换位置
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break


arr1 = Sort(100)
for i in arr1.arr:
    print(i, end=' ')
