# 1017.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-16 8:43
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1017 平均环数

url: http://www.hfoj.net/problem/1017
"""

nums = [int(i) for i in input().split(" ")]
print("%.3f" % (sum(nums) / len(nums)))
