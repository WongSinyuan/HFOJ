# 1019.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:03
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1019 买笔

url: http://www.hfoj.net/problem/1019
"""
m, n, s = list(map(int, input().split()))
print("%.3f" % (s / (m + n / 4)))
