# -*- coding = utf-8 -*-
# @Time : 2025/1/1 14:21
# @Author : guohexing
# @Fire : 5练习seek.py
# @Software : PyCharm
import os


# 定位到文件开头
def seek_start():
    file = open("file.txt", "r+", encoding="utf-8")
    file.seek(5, os.SEEK_SET)
    text = file.read()
    print(text)
    file.close()


def seek_end():
    file = open("file.txt", "r+", encoding="utf-8")
    file.seek(0, os.SEEK_END)
    text = file.read()
    print(text)
    file.close()


def seek_current():
    file = open("file.txt", "r+", encoding="utf-8")
    file.seek(0, os.SEEK_CUR)
    text = file.read()
    print(text)
    file.close()


def seek_b_current():
    '''
    二进制文件定位,读取文件内容
    :return:
    '''
    file = open("file.txt", "rb+")
    file.seek(6, os.SEEK_CUR)
    file.seek(-4, os.SEEK_CUR)
    file.seek(-1, os.SEEK_END)
    text = file.read()
    print(text)
    file.close()


if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_current()
    seek_b_current()#二进制文件定位

