# Python31117.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-02-24 23:19
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1117 火车编组

url: http://www.hfoj.net/problem/1117
"""

_, i = int(input()), 1
for j in list(map(int, input().split())):
    for i in range(i + 1, j + 2):
        print("A", end="")
    print("B", end="")
