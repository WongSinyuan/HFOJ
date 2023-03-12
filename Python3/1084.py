# Python31084.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-03-11 23:02
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1084 数字全排列

url: http://www.hfoj.net/problem/1084
"""


def f(a, b):
    if len(a) == 1:
        print(" ".join(list(map(str, b + a))) + " ")  # 最坑的末尾加空格
    else:
        for i in range(len(a)):
            f(a[:i] + a[i + 1:], b + [a[i]])


f(list(range(1, int(input()) + 1)), [])
