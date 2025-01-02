# -*- coding = utf-8 -*-
# @Time : 2025/1/2 16:01
# @Author : guohexing
# @Fire : 3练习sort和sorted.py
# @Software : PyCharm
my_list = "hello world,a,A,sdsaf,g,d,a,f,,y,z,1,2,3,4,5,6,7,8,9,0,Z".split(',')
print(my_list)


# sort()方法对列表进行排序，sort()方法没有返回值，而sorted()函数返回的是一个新的列表。
def change_lower(str_name: str):
    return str_name.lower()


my_list.sort()
print(my_list)

# 可以传递一个key参数，key参数是一个函数，函数的作用是将列表中的元素转换成另一种形式，然后排序。
# 在这里，我们将字符串全部转换成小写字母，然后排序。
# 注意，sorted()函数返回的是一个新的列表，而sort()方法是对原列表进行排序。
print(sorted(my_list, key=change_lower))

# 也可以使用lambda表达式作为key参数。
print(sorted(my_list, key=lambda x: x.lower()))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):# 定义__repr__方法，返回一个新东西
        '''
        相对于__str__方法，__repr__方法返回非字符串的对象，
        :return:
        '''
        return repr((self.name, self.grade, self.age))

students = Student("Alice", 9, 18)
print(students)
my_dict = {"Alice": ['m',7], "Bob": ['f', 8], "Charlie": ['f', 9]}
print(sorted(my_dict.items(), key=lambda x: x[1][1]))