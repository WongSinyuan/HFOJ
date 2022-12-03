# 1087.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:53
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1087
url: http://www.hfoj.net/problem/1087
"""


def df(x: int) -> list:
    """
    所有上台阶的方案

    :param x: 总级数
    :return: 方案
    """
    if x == 1:
        return [[1]]
    elif x == 2:
        return [[1, 1], [2]]
    else:
        return [i + [1] for i in df(x - 1)] + [j + [2] for j in df(x - 2)]


for k in sorted(df(int(input()))):  # 不知道怎么按字典序输出QAQ
    print("".join(map(str, k)))
