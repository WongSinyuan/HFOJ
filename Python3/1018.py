# 1018.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 17:58
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1018 小明购物

url: http://www.hfoj.net/problem/1018
"""

m, n, s = list(map(int, input().split()))
print("%.3f" % (s / (m - n * 3)))
