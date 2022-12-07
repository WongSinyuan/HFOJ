# 1047.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:33
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1047 角谷猜想

url: http://www.hfoj.net/problem/1047
"""
num = int(input())


def compute(n):
    """
    计算角谷猜想

    :param n: 初始数
    :return: 结束
    """
    if n == 1:
        return 1
    if n % 2 == 0:
        re = n // 2
        print(f"{n}/2={re}")
        compute(re)
    else:
        re = n * 3 + 1
        print(f"{n}*3+1={re}")
        compute(re)


compute(num)
print("End")
