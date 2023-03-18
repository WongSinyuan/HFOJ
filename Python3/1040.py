# 1040.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:21
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1040 字数统计

url: http://www.hfoj.net/problem/1040
"""

s = input().lower()

for m, n in [(chr(i), s.count(chr(i))) for i in range(97, 123) if s.count(chr(i)) != 0]:
    print(m, n)
