# 1034.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 16:25
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1034 字符串压缩1

url: http://www.hfoj.net/problem/1034
"""

s = input()
j = ""
count = 1
total = []

for i in range(len(s)):
    if s[i] == j:
        count += 1
    else:
        total.append([count, j])
        j = s[i]
        count = 1
    if i == len(s) - 1:
        total.append([count, j])

re = ""
for n, k in total:
    if n == 1 or n == 2:
        re += k * n
    else:
        re += str(n - 1) + k

print(re)
