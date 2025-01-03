# -*- coding = utf-8 -*-
# @Time : 2025/1/2 20:09
# @Author : guohexing
# @Fire : 快速排序2.py
# @Software : PyCharm
import random
import time

class QuickSort2():
    '''
    快速排序2.py
    '''
    def __init__(self, length):
        '''
        初始化
        :param length:列表长度
        '''
        self.length = length
        self.arr = [0]*length
        self.generate_random_list()

    def generate_random_list(self):
        '''
        生成随机列表
        :return:
        '''
        for i in range(self.length):
            self.arr[i] = random.randint(0, 1000000)

    def quick_sort(self, left, right):
        '''
        快速排序
        :param left: 左边界
        :param right: 右边界
        :return:
        '''
        if left >= right:
            return
        pivot = self.partition(left, right)
        self.quick_sort(left, pivot-1)
        self.quick_sort(pivot+1, right)

    def partition(self, left, right):
        '''
        分区
        :param left:
        :param right:
        :return:
        '''
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def time_used(self):
        '''
        计算时间
        :return:
        '''
        start_time = time.time()
        self.quick_sort(0, self.length-1)
        end_time = time.time()
        return end_time - start_time

if __name__ == '__main__':
    length = 10000
    quick_sort = QuickSort2(length)
    print("排序前：", quick_sort.arr)
    time_used = quick_sort.time_used()
    print("排序后：", quick_sort.arr)
    print("用时：", time_used)