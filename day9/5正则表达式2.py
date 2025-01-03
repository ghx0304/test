# -*- coding = utf-8 -*-
# @Time : 2025/1/3 16:19
# @Author : guohexing
# @Fire : 5正则表达式2.py
# @Software : PyCharm
import re


# 贪婪匹配
# 正则表达式匹配到尽可能多的字符，直到不能再匹配为止。
def use_greedy():
    s = 'this is a number 123-456-789'
    ret = re.match(r'.+(\d+-\d+-\d+)', s)
    if ret:
        print(ret.group(1))
    else:
        print('No match')


# 非贪婪匹配
# 正则表达式匹配到尽可能少的字符，直到不能再匹配为止。
def use_nongreedy():
    s = 'this is a number 123-456-789'
    ret = re.match(r'.*?(\d+-\d+-\d+)', s)
    if ret:
        print(ret.group(1))
    else:
        print('No match')


def use_option():
    print(re.match(r'\w*', 'adc爱思', flags=re.A).group())
    print(re.match(r'A*', 'aAdc爱思', flags=re.I).group())
    print(re.match(r'.*', 'adc爱思\n123', flags=re.S).group())


if __name__ == '__main__':
    # use_greedy()
    # use_nongreedy()
    use_option()
