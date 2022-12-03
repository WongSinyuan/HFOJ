# 1011.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-16 11:53
# @Software: PyCharm
# @Project: HFOJ

"""
文件说明:HFOJ #1011
"""

l = input()

x, m, n = [int(i) for i in l.split(" ")]

b = (x - 30 * m) / (m + n)
a = b + 30

print(int(a))
print(int(b))
