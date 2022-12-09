# 1058.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 19:09
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1058 旗手

url: http://www.hfoj.net/problem/1058
"""

nums = [input(), list(map(int, input().split()))][1]

nums[nums.index(max(nums))], nums[0] = nums[0], nums[nums.index(max(nums))]
print(" ".join(map(str, nums)))
