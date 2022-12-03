# 1040.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:21
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1040
url: http://www.hfoj.net/problem/1040
"""

s = input().lower()

for j in [(i, s.count(i)) for i in "abcdefghijklmnopqrstuvwxyz" if s.count(i) != 0]:
    print(j[0], j[1])
