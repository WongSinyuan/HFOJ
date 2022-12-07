# 1062.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-11-04 21:05
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1062 素数大酬宾

url: http://www.hfoj.net/problem/1062
"""

n = int(input())

s = list(range(3, n, 2))

i = 0
m = 3

while m <= int(n ** 0.5):
    if s[i]:
        j = (m * m - 3) // 2
        s[j] = 0
        while j < len(s):
            s[j] = 0
            j += m
    i += 1
    m = 2 * i + 3

res = [2] + [x for x in s if x]
print(" ".join(map(str, res)))  # 10ms的时限过于变态
