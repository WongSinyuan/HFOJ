# 1036.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-09-17 18:23
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1036 最小字典序

url: http://www.hfoj.net/problem/1036
"""
s = list(input())

min_index = sum([(x + 1) * (26 ** a) for a, x in zip(range(len(s)),
                                                     ["abcdefghijklmnopqrstuvwxyz".index(n) for n in s[:: -1]])])

change = [-1, -1]

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        u_s = s.copy()
        u_s[i], u_s[j] = u_s[j], u_s[i]
        index = sum([(x + 1) * (26 ** a) for a, x in zip(range(len(u_s)),
                                                         ["abcdefghijklmnopqrstuvwxyz".index(n) for n in u_s[:: -1]])])
        if index < min_index:
            min_index = index
            change = [i, j]

s[change[0]], s[change[1]] = s[change[1]], s[change[0]]
print("".join(s))
