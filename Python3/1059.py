# 1059.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 19:16
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1059 整理题库

url: http://www.hfoj.net/problem/1059
"""

print(" ".join(map(str, sorted(
    [list(map(int, input().split())), list(map(int, input().split())) + list(map(int, input().split()))][1]
))))
