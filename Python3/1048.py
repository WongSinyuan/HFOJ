# 1048.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:36
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1048 数字反转

url: http://www.hfoj.net/problem/1048
"""
n = int(input())
print(("" if n >= 0 else "-") + str(int(str(n)[(0 if n >= 0 else 1):][::-1])))
