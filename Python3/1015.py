# 1015.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 17:30
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1015
url: http://www.hfoj.net/problem/1015
"""

s, x, y = list(map(int, input().split()))

print("%d" % (2 * (s - 10 * x) / (x + y) + 10))
