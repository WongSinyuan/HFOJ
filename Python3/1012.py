# 1012.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 17:27
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1012
url: http://www.hfoj.net/problem/1012
"""

x, y = list(map(int, input().split()))

print(x - (y - 2 * x) // 2)
print((y - 2 * x) // 2)
