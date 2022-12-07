# 1038.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 16:28
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1038 游客观光

url: http://www.hfoj.net/problem/1038
"""

n, m, W = list(map(int, input().split()))

c = {i: w for i, w in zip(list(range(1, n + 1)), [int(input()) for _ in range(n)])}
ship_w = []
ship_i = []
max_w = 0
for _ in range(m):
    i = int(input())
    if i in ship_i:
        ship_i.pop(ship_i.index(i))
        ship_w.pop(ship_w.index(c[i]))
    else:
        ship_i.append(i)
        ship_w.append(c[i])

    if sum(ship_w) > W:
        print("Oh, My God!")
        break
    elif sum(ship_w) > max_w:
        max_w = sum(ship_w)
else:
    print(max_w)
