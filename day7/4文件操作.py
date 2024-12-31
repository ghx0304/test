# -*- coding = utf-8 -*-
# @Time : 2024/12/31 20:47
# @Author : guohexing
# @Fire : 4文件操作.py
# @Software : PyCharm
def open_r():
    """
    打开文件并读取内容
    :return:
    """
    file = open("file.txt", mode="r+", encoding="utf-8")
    print(file.read())
    file.write("hello world")#写到末尾了

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
    打开文件并追加内容
    :return:
    """
    file = open("file3.txt", mode="a+", encoding="utf-8")
    file.write("hello world")
    print(file.read())
    file.close()


if __name__ == '__main__':
    #open_r()
    open_w()