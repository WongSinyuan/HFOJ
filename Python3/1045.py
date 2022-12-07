# 1045.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:33
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1045 数字累加

url: http://www.hfoj.net/problem/1045
"""
n = int(input())
t = (1 + n) * (n // 2)
t += n // 2 + 1 if n % 2 != 0 else 0
print(t)
