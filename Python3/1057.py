# 1057.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 18:33
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1057 高个子人数

url: http://www.hfoj.net/problem/1057
"""

nums = [input(), list(map(int, input().split()))][1]
adv = sum(nums) / len(nums)
print(len(list(filter(lambda x: x > adv, nums))))
