# -*- coding = utf-8 -*-
# @Time : 2025/1/2 14:08
# @Author : guohexing
# @Fire : 2排序.py
# @Software : PyCharm
import random


# my_dict = {'name': 'wangdao', 'age': 25, 'gender': 'male'}
# print(my_dict)

# hash的时间复杂度是O(1)
# print(hash('my_dict'))
# print(hash('my_dict'))

# n = 10
# 嵌套循环的时间复杂度是O(n^2)
# for i in range(n):
#   for j in range(n):
#        print(i, j)


# 快速排序的时间复杂度是O(nlogn)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)


class Sort():
    def __init__(self, n):
        '''
        初始化排序列表
        :param n: 排序数的数量
        '''
        self.len = n  # 排序列表的长度
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def qiuck_sort(self, left, right):
        '''
        快速排序算法
        :param left:
        :param right:
        :return:
        '''
        if left >= right:
            return
        pivot = self.partition(left, right)
        self.qiuck_sort(left, pivot - 1)
        self.qiuck_sort(pivot + 1, right)

    def qiuck_sort2(self, left, right):
        '''
        快速排序算法
        :param left: 最左边的索引
        :param right: 最右边的索引
        :return:
        '''
        if left >= right:
            return
        pivot = self.partition2(left, right)
        self.qiuck_sort(left, pivot - 1)
        self.qiuck_sort(pivot + 1, right)

    def partition(self, left, right):
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

    def partition2(self, left, right):
        arr = self.arr
        k = i = left
        for i in range(left, right):
            if arr[i] < arr[right]:  # 某个位置的数比pivot小，则交换到左边
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def adjust_heap(self, i, n):
        '''
        将堆调整大根堆
        :param i: 堆的根节点
        :param n: 堆的大小
        :return:
        '''


    def heap_sort(self):
        '''
        堆排序算法
        :return:
        '''

        pass

if __name__ == '__main__':
    my_sort = Sort(10)
    print(my_sort.arr)
    my_sort.qiuck_sort(0, 9)
    print(my_sort.arr)
    my_sort2 = Sort(10)
    print(my_sort2.arr)
    my_sort2.qiuck_sort2(0, 9)
    print(my_sort2.arr)

