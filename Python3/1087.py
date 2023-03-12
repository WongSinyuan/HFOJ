# 1087.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:53
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1087 上台阶1

url: http://www.hfoj.net/problem/1087
"""


def f(a, b):
    if a == 1:
        print(b + "1")
    elif a == 2:
        print(b + "11")
        print(b + "2")
    else:
        f(a - 1, b + "1")
        f(a - 2, b + "2")


f(int(input()), "")
