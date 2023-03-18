# 1041.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:22
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1041 数字反转

url: http://www.hfoj.net/problem/1041
"""

s = (input())
print(s[len(s) // 2 + len(s) % 2:] + s[len(s) // 2: len(s) // 2 + len(s) % 2] + s[:len(s) // 2])
