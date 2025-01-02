# -*- coding = utf-8 -*-
# @Time : 2024/12/31 20:47
# @Author : guohexing
# @Fire : 4文件操作.py
# @Software : PyCharm
import os
def open_r():
    """
    打开文件并读取内容
    :return:
    """
    file = open("file.txt", mode="r+", encoding="utf-8")
    print(file.read())
    file.write("hello world")  # 写到末尾了

    # print(type(file.read()))字符串
    print(file.read())
    file.close()


def open_w():
    """
    打开文件并写入内容
    :return:
    """
    file = open("file3.txt", mode="w+", encoding="utf-8")
    file.write("hello world")
    print(file.read())

    file.close()


def open_a():
    """
    打开文件并追加内容每次写入都会在末尾追加
    :return:
    """
    file = open("file3.txt", mode="a+", encoding="utf-8")
    file.write("hello world")
    print(file.read())
    file.close()


def use_readlines():
    """
    读取文件所有内容并按行读取
    :return:
    """
    file = open("file.txt", mode="r+", encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        print(line, end="")
    file.close()

def use_seek():
    """
    移动文件指针到指定位置读取内容
    :return:
    """
    file = open("file.txt", mode="r+", encoding="utf-8")
    file.seek(0)  # 移动到文件开头
    print(file.read(), end="")
    file.seek(10)  # 移动到第10个字节
    print(file.read(5))  # 读取5个字节
    file.seek(0)  # 移动到文件开头
    print(file.read())
    file.close()




if __name__ == '__main__':
    #open_r()
    open_w()
    #use_readlines()
    #use_seek()
