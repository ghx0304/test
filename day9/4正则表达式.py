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
    """
    单字符匹配
    :return:
    """
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

    result = re.match(r'嫦娥\d号', '嫦娥1号发射成功')
    print(result.group())


def more():
    """
    多字符匹配
    :return:
    """
    result = re.match(r'w*', 'wwwwwd123456')
    print(result.group())
    result = re.match(r'[a-zA-Z_][a-zA-Z/d]*', 'wwwwwd123456')
    print(result.group())
    print('-' * 50)
    ret = re.match(r'[1-9]?\d', '07')
    print(ret.group())
    ret = re.match(r'[1-9]?\d', '10')
    print(ret.group())
    print('-' * 50)
    ret = re.match(r'[a-zA-Z\d]{6}', '123dfsdf6')
    print(ret.group())
    # 默认贪婪匹配，尽可能多的匹配
    ret = re.match(r'[a-zA-Z\d]{6,10}', '123dfsdf*41566')
    print(ret.group())
    ret = re.match(r'[a-zA-Z\d]{4,20}@163.com', 'dasdas@163.com')
    print(ret.group())
    ret = re.match(r'[1-9]\d$', '19')
    if ret:
        print(ret.group())
    else:
        print(f'{ret}匹配失败')


def start_end():
    """
    匹配字符串的开始和结束
    :return:
    """
    email_list = ['<EMAIL>', '123456@163.com', '1234567@163.com', '12345678@163.com123', 'a123456@163.com']
    for email in email_list:
        ret = re.match(r'\w{4,20}@163\.com$', email)  # 正则出现\转义$必须在末尾
        if ret:
            print(f'{ret.group()} 匹配成功')
        else:
            print(f'{email} 匹配失败')


def split_group():
    """
    分组匹配
    :return:
    """
    # 匹配0-100之间的数字
    ret = re.match(r'[1-99]?\d$|100', '0')
    if ret:
        print(f'{ret.group()} 匹配成功')
    else:
        print(f'{ret} 匹配失败')

    # 匹配1-100之间的数字
    ret = re.match(r'[1-9]\d$|[1-9]$|100', '100')
    if ret:
        print(f'{ret.group()} 匹配成功')
    else:
        print(f'{ret} 匹配失败')
    print('-' * 50)
    ret = re.match(r'([^-]+)-(\d+)', '010-123456789')
    if ret:
        print(f'{ret.group(1)} 匹配成功')
        print(f'{ret.group(2)} 匹配成功')
    else:
        print(f'{ret} 匹配失败')
    print('-' * 50)
    ret = re.match(r'<[a-zA-Z]*>\w*</[a-zA-Z]*>', '<html>hello</html>')
    if ret:
        print(f'{ret.group()} 匹配成功')
    else:
        print(f'{ret} 匹配失败')
    ret = re.match(r'<([a-zA-Z]*)>\w*</\1>*>', '<html>hello</html>')
    if ret:
        print(f'{ret.group()} 匹配成功')
    else:
        print(f'{ret} 匹配失败')


def other_func():
    """
    其他函数
    :return:
    """
    ret = re.search(r'\d+', '阅读次数9999')
    if ret:
        print(f'{ret.group()} 匹配成功')
    else:
        print(f'{ret} 匹配失败')
    print('-' * 50)
    ret = re.findall(r'\d+', '阅读次数9999，评论次数8888')
    if ret:
        print(f'{ret} 匹配成功')
    else:
        print(f'{ret} 匹配失败')
    print('-' * 50)
    ret = re.sub(r'\d+', lambda x: str(int(x.group()) * 2), '阅读次数9999，评论次数8888')
    print(ret)
    print('-' * 50)

    def add(x):
        return str(int(x.group()) * 2)

    ret = re.sub(r'\d+', add, '阅读次数9999，评论次数8888', count=1)
    print(ret)
    print('-' * 50)


def find_second_match(pattern, text):
    match = re.finditer(pattern, text)
    try:
        next(match)  # 跳过第一个匹配
        second_match = next(match)  # 找到第二个匹配
        return second_match.group()
    except StopIteration:
        print(f'没有找到第二个匹配')
        return None


def use_findall():
    """
    使用findall函数
    :return:
    """
    s = 'hello world,now is2025/1/3 10:59,现在是2025年1月3日10点59分'
    ret_s = re.sub(r'(年|月)', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)


def usb_sub():
    """
    使用sub函数
    :return:
    """
    long_text = '''hello world,now is2025/1/3 10:59,现在是2025年1月3日10点59分'''
    print(long_text)
    ret = re.sub(r"<[^>]*>|&nbsp;|\n|\s+", "", long_text)
    print(ret)


def use_split():
    """
    使用split函数
    :return:
    """
    s = 'hello world,now is2025/1/3 10:59,现在是2025年1月3日10点59分'
    ret = re.split(r' |/', s)
    print(ret)


if __name__ == '__main__':
    # single()
    # more()
    # start_end()
    # split_group()
    # other_func()
    # 匹配第二个数字
    # text = '阅读次数9999，评论次数8888'
    # pattern = r'\d+'
    # second_match = find_second_match(pattern, text)
    # if second_match:
    #     print(f'第二个数字是{second_match}')
    # else:
    #     print('没有找到第二个数字')
    # usb_sub()
    use_split()
