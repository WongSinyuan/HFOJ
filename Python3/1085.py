# Python31085.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-02-24 22:52
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1085 奶牛探路

url: http://www.hfoj.net/problem/1085
"""

n, k = list(map(int, input().split()))


def f(num):
    a = (num + k) / 2
    b = a - k
    if int(a) == a and b > 0:
        return f(a) + f(b)
    else:
        return 1


print(f(n))
