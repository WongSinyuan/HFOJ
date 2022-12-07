# 1024.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:05
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1024 能量摄入

url: http://www.hfoj.net/problem/1024
"""

m, x, y, z = list(map(int, input().split()))
print("%.3f" % (sum(
    [[x, y, z, z]["ABCDEFGHIJ".index(p) // 3] / 100 * int(q)
     for p, q in list(map(
        lambda _: input().split(),
        range(m)))
     ]) / 4.18))
