# 1033.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022/12/3 15:12
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1033 休息？工作？

url: http://www.hfoj.net/problem/1033
"""

x = int(input())


def is_prime(n: int) -> int:
    """
    判断是否为质数

    :param n: 数
    :return: 一个数
    """
    if n == 2 or n == 3 or n == 5:
        return 1

    if n % 2 == 0:
        return 0
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return 0
    return 1


if 2 <= x <= 20:
    if is_prime(x):
        print(">_<")
    else:
        print("^o^")
else:
    print("=.=")
