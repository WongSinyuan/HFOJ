# 1039.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 16:45
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1039 桶排序

url: http://www.hfoj.net/problem/1039
"""
print(" ".join(list(map(str, sorted([input(), list(map(int, input().split()))][1])))))
# 用sorted算不算作弊啊……（小声bb
