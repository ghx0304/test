# -*- coding = utf-8 -*-
# @Time : 2025/1/1 15:08
# @Author : guohexing
# @Fire : 7python传参数.py
# @Software : PyCharm
import sys

#print(type(sys.argv))
#print(sys.argv)
def write(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('hello world')
    file.close()

if __name__ == '__main__':
    write(sys.argv[1])