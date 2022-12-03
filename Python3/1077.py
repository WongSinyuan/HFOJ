# 1077.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:49
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1077
url: http://www.hfoj.net/problem/1077
"""

row = [list(map(int, input().split())) for _ in range(5)]
col = []

for x in range(5):
    a = []
    for y in range(5):
        a.append(row[y][x])
    col.append(a)

re = []

for y in range(5):
    for x in range(5):
        if max(row[y]) == min(col[x]):
            re = [y + 1, x + 1, row[y][x]]

if not re:
    print('not found')
else:
    print(" ".join(map(str, re)))
