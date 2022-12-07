# 1026.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:30
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1026 成绩评价

url: http://www.hfoj.net/problem/1026
"""
n = int(input())
print("Poor" if n < 60 else ["Average", "Good", "Good", "Great", "Great"][(n - 60) // 10])
