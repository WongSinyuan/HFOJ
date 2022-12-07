# 1043.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:29
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1043 最大公约数

url: http://www.hfoj.net/problem/1043
"""

m, n = list(map(int, input().split()))

for i in range(min([m, n]), 0, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        break
