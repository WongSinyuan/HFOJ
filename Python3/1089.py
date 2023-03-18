# 1089.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-03-18 20:57
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1089 分数字2

url: http://www.hfoj.net/problem/1089
"""


def f(a, n, lis):
    if a != 1:
        for i in range((lis[-1] + 1) if lis else 1, a // 2 + 1):
            f(a - i, n - 1, lis + [i])
    if n == 1 and lis[-1:] != [a]:
        print(" ".join(map(str, (lis + [a]))))


f(*(list(map(int, input().split())) + [[]]))
