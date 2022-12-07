# 1053.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 17:37
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1053 圆周率

url: http://www.hfoj.net/problem/1053
"""

pi, i, j = 0, 1, 0
while True:
    if 1 / i < 10 ** -6:
        break
    pi += (-1) ** j * (1 / i)
    i += 2
    j += 1

print("%.8f" % (pi * 4))
