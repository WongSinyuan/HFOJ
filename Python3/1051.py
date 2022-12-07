# 1051.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:38
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1051 含k个3的数

url: http://www.hfoj.net/problem/1051
"""
m, n, k = map(int, input().split())

a = m + 7 - m % 7
re = 0
for j in range(a, n + 1, 7):
    if str(j).count("3") == k:
        re += 1

print(re)
