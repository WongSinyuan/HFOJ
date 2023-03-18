# Python31088.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-03-11 23:11
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1088 分数字1

url: http://www.hfoj.net/problem/1088
"""


def f(a, lis):
    if a != 1:
        for i in range(lis[-1] if lis else 1, a // 2 + 1):
            f(a - i, lis + [i])
    print(" ".join(map(str, lis + [a])) + " ")  # 又是这该死的空格


f(int(input()), [])
