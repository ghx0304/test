# -*- coding = utf-8 -*-
# @Time : 2025/1/3 9:46
# @Author : guohexing
# @Fire : 2深拷贝与浅拷贝.py
# @Software : PyCharm
import copy


# 浅拷贝    对于不可变对象，浅拷贝只拷贝引用，对于可变对象，浅拷贝只拷贝引用，不会拷贝对象本身
# 对于不可变对象，浅拷贝和深拷贝的区别在于，浅拷贝只拷贝引用，不会拷贝对象本身，因此，浅拷贝不会影响原对象，而深拷贝会影响原对象
# 对于可变对象，浅拷贝只拷贝引用，不会拷贝对象本身，因此，浅拷贝不会影响原对象，而深拷贝会影响原对象
def use_list_copy():
    a = [1, 2, 3, 4, [5, 6, 7]]
    b = a.copy()
    b[0] = 100
    print(a)
    print(b)


def use_copy():
    '''
    使用copy模块的copy方法进行深拷贝
    :return:
    '''
    c = [1, 2, 3, 4, 5]
    d = copy.copy(c)
    d[0] = 100
    print(c)
    print(d)
    print(id(c))
    print(id(d))


def use_copy2():
    '''
    copy是浅拷贝
    :return:
    '''
    a = [1, 2, 3, 4, [5, 6, 7]]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    print(f'c: {c}')
    print(f'd: {d}')
    a[0] = 100
    print(f'c: {c}')
    print(f'd: {d}')


def use_deepcopy():
    '''
    使用copy模块的deepcopy方法进行深拷贝
    :return:
    '''
    a = [1, 2, 3, 4, [5, 6, 7]]
    b = [3, 4]

    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    print(f'c: {c}')
    print(f'd: {d}')
    a[0] = 100
    print(f'c: {c}')
    print(f'd: {d}')

class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipments = ['鞋子','盔甲']

def use_deepcopy_own_obj():
    old = Hero('Tom', 90)
    new = copy.deepcopy(old)
    new.blood = 80
    print(old.blood)
    print(new.blood)
    new.equipments.append('项链')
    print(old.equipments)
    print(new.equipments)



if __name__ == '__main__':
    # use_copy()
    # use_copy2()
    # use_deepcopy()
    use_deepcopy_own_obj()
