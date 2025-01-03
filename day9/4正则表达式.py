# -*- coding = utf-8 -*-
# @Time : 2025/1/3 10:59
# @Author : guohexing
# @Fire : 4正则表达式.py
# @Software : PyCharm
import re


def simple():
    result = re.match('wd', 'wd123456')
    if result:
        print(result.group())


def single():
    '''
    单字符匹配
    :return:
    '''
    result = re.match('.', 'wd123456')
    print(result.group())

    result = re.match('t.o', 'too')
    print(result.group())

    result = re.match('t.o', 'two')
    print(result.group())

    result = re.match('[0-35-9]', '123456789')
    print(result.group())

    result = re.match('[aB]', 'abcde')
    print(result.group())

    result = re.match('嫦娥\d号', '嫦娥1号发射成功')
    print(result.group())


def more():
    '''
    多字符匹配
    :return:
    '''
    result = re.match('w*', 'wwwwwd123456')
    print(result.group())
    result = re.match('[a-zA-Z0-9][a-zA-Z0-9]*', 'wwwwwd123456')
    print(result.group())



if __name__ == '__main__':
   # single()
    more()