# 1023.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-16 8:54
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1023
url: http://www.hfoj.net/problem/1023
"""

s = [letter for letter in input()]
t = [letter for letter in input()]

if sorted(s) == sorted(t):
    print("YES")
else:
    print("NO")
