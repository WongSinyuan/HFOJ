# 1064.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:39
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1064 回型方阵

url: http://www.hfoj.net/problem/1064
"""
n = int(input())
s = [0] * n
t = []
for y in range(n // 2 + n % 2):
    s = s[:y] + [i + 1 for i in s[y:len(s) - y]] + s[len(s) - y:]
    t.append(s)
    print(" ".join(map(str, s)))

for i in t[::-1][n % 2:]:
    print(" ".join(map(str, i)))
