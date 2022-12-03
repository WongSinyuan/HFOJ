# 1090.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:56
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1090
url: http://www.hfoj.net/problem/1090
"""


def f(t: list, n=0):
    """
    计算所有大小写方案

    :param t: 初始字符串
    :param n: 字符序号
    :return: 无
    """
    if n == len(t):
        print("".join(t))  # 递归终点
        return
    t[n] = t[n].upper()
    f(t, n + 1)
    if t[n].isalpha():
        t[n] = t[n].lower()
        f(t, n + 1)


f(list(input()))
