# 1009.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 17:14
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1009 立方体的高和表面积

url: http://www.hfoj.net/problem/1009
"""
a, b, v = list(map(int, input().split()))
h = v / a / b

print("%.2f" % h)
print("%.2f" % ((a * b + a * h + b * h) * 2))
