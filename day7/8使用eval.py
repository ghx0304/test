# -*- coding = utf-8 -*-
# @Time : 2025/1/1 15:14
# @Author : guohexing
# @Fire : 8使用eval.py
# @Software : PyCharm
def read_conf():
    '''
    读取配置文件
    :return:
    '''
    file = open('file6', 'r+', encoding='utf-8')
    text = file.read()
    file.close()
    text = eval(text)
    print(type(text))
    print(text.keys())
    print(text)


if __name__ == '__main__':
    read_conf()
