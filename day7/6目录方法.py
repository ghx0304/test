# -*- coding = utf-8 -*-
# @Time : 2025/1/1 14:35
# @Author : guohexing
# @Fire : 6目录方法.py
# @Software : PyCharm
import os
from time import strftime
from time import gmtime

def use_rename():
    '''
    重命名文件
    :return:
    '''
    os.rename('file3.txt', 'file4.txt')


def use_dir_func():
    '''
    获取当前目录下的文件列表
    :return:
    '''
    file_list = os.listdir('.')
    print(file_list)
    print(os.getcwd())


def scan_dir(width, current_path):
    '''
    深度优先遍历目录
    :param path:
    :return:
    '''
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' ' * width + file)
        new_path = current_path + '/' + file
        if os.path.isdir(new_path):
            scan_dir(width + 4, new_path)
def use_stat(file_path):
    '''
    获取文件信息
    :return:
    '''
    file_info = os.stat(file_path)
    print(file_info)
    gmt_time = gmtime(file_info.st_mtime)
    print(strftime('%Y-%m-%d %H:%M:%S', gmt_time))


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    #scan_dir(0, '.')
    use_stat('file.txt')
    #os.listdir('.')
    #os.path.isdir('.')
