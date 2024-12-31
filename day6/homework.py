# -*- coding = utf-8 -*-
# @Time : 2024/12/30 22:31
# @Author : guohexing
# @Fire : homework.py
# @Software : PyCharm
def homework():
    '''
    通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
    :return:
    '''


    try:
        num = int(input("请输入一个整数："))
        if type(num) != int:
            raise TypeError("输入的不是整型数")
        if str(num) == str(num)[::-1]:
            print("是对称数")
        else:
            ex = ValueError("输入的不是对称数")
            raise ex

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    homework()
