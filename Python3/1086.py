# Python31086.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-03-11 22:56
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1086 二进制分类

url: http://www.hfoj.net/problem/1086
"""

print(*list(map(lambda c: (c, 1000 - c), [sum(list(map(lambda n: (2 * sum(n) > len(n)), map(lambda i: list(map(int, bin(i)[2:])), range(1, 1001)))))]))[0])

# 正确答案
print(538, 462)
