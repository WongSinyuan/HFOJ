# 1072.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:41
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1072
url: http://www.hfoj.net/problem/1072
"""

print(list(map(
    lambda n, m: "{:.2f}".format(
        len(list(map(
            lambda p1, p2: [1 for x in range(n) for y in range(m) if p1[y][x] == p2[y][x]],
            [[list(map(int, input().split())) for _ in range(m)]],
            [[list(map(int, input().split())) for _ in range(m)]]))[0]) / (m * n) * 100),
    *list(map(lambda x: [int(x)], input().split()))))[0])  # 说实话，咱也不愿意看这又臭又长的代码
