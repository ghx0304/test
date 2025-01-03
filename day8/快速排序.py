# -*- coding = utf-8 -*-
# @Time : 2025/1/2 19:55
# @Author : guohexing
# @Fire : 快速排序.py
# @Software : PyCharm
class Solution():
    '''
    快速排序
    '''

    def __init__(self, length):
        '''
        初始化列表
        :param length:
        '''
        self.length = length
        self.arr = [0] * length
        self.random_data()

    def random_data(self):
        '''
        随机生成数据
        :return:
        '''
        import random
        for i in range(self.length):
            self.arr[i] = random.randint(0, 10000)

    def quick_sort(self, left, right):
        '''
        快速排序
        :param left:
        :param right:
        :return:
        '''
        if left >= right:
            return
        pivot = self.partition(left, right)
        self.quick_sort(left, pivot - 1)
        self.quick_sort(pivot + 1, right)

    def partition(self, left, right):
        '''
        划分
        :param left:
        :param right:
        :return:
        '''
        pivot = self.arr[left]
        i = left + 1
        j = right
        while i <= j:
            while i <= j and self.arr[i] <= pivot:
                i += 1
            while i <= j and self.arr[j] >= pivot:
                j -= 1
            if i < j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[left], self.arr[j] = self.arr[j], self.arr[left]
        return j

    def print_arr(self):
        '''
        打印列表
        :return:
        '''
        print(self.arr)

    def time_ues(self):
        '''
        使用快排对列表进行排序，并计算时间
        :return:
        '''
        import time
        start_time = time.time()
        self.quick_sort(0, self.length - 1)
        end_time = time.time()
        print("Time used:", end_time - start_time)


if __name__ == '__main__':
    s = Solution(1000)
    s.print_arr()
    s.time_ues()
    s.print_arr()
