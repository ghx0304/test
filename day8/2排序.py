# -*- coding = utf-8 -*-
# @Time : 2025/1/2 14:08
# @Author : guohexing
# @Fire : 2排序.py
# @Software : PyCharm
import random
import time

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
            self.arr[i] = random.randint(0, 100000)

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

    def adjust_heap(self, pos, arr_len):
        '''
        将堆调整大根堆
        :param pos: 堆的根节点
        :param n: 堆的大小
        :return:
        '''
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:#左孩子小于列表长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 判断右孩子存在且大于左孩子
                son += 1
            if arr[dad] < arr[son]:  # 父节点小于子节点，则交换
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        '''
        把堆调整成大根堆，然后依次取出堆顶元素，放入排序列表
        :return:
        '''

        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust_heap(i, self.len)
            #print(self.arr)
        for i in range(self.len - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]#把堆顶元素放到最后，然后调整堆
            self.adjust_heap(0, i)

    def test_time_use(self,sort_func,*args,**kwargs):
        '''
        测试排序算法的时间复杂度
        回调函数
        :param sort_func:
        :return:
        '''
        start_time = time.time()
        sort_func(*args,**kwargs)
        end_time = time.time()
        print('用时：', end_time - start_time)



if __name__ == '__main__':
    count = 1000
    #start_time = time.time()
    #my_sort = Sort(count)
    #print(my_sort.arr)
    #my_sort.qiuck_sort(0, count - 1)
    #print(my_sort.arr)
    #end_time = time.time()
    #print('用时：', end_time - start_time)
   # my_sort2 = Sort(10)
    #print(my_sort2.arr)
    #my_sort2.qiuck_sort2(0, 9)
    #print(my_sort2.arr)
    my_sort3 = Sort(count)
    #start_time = time.time()
    #print(my_sort3.arr)
    #my_sort3.heap_sort()
    #print(my_sort3.arr)
    #end_time = time.time()
    #print('用时：', end_time - start_time)
    my_sort3.test_time_use(my_sort3.heap_sort)
    my_sort3.test_time_use(my_sort3.qiuck_sort2,0,count-1)
