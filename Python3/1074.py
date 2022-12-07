# 1074.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:47
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1074 比例简化

url: http://www.hfoj.net/problem/1074
"""

a, b, L = list(map(int, input().split()))
s = a / b
re = []
min_ = 1


def gcd(x, y) -> int:
    """
    判断两个数是否互质

    :param x: 一个数
    :param y: 另一个数
    :return: 是否互质
    """
    if x < y:
        x, y = y, x
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y


for i in range(1, L):
    for j in range(1, L):
        if i / j >= s and i / j - s < min_ and gcd(i, j) == 1:  # 贪心算法
            re = [i, j]
            min_ = i / j - s
print(re[0], re[1])
