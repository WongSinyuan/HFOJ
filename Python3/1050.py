# 1050.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:38
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1050 最大跨度

url: http://www.hfoj.net/problem/1050
"""
input()
nums = list(map(int, input().split()))

print(max(nums) - min(nums))
