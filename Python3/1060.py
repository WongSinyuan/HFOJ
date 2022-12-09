# 1060.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 19:19
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1060 数字统计

url: http://www.hfoj.net/problem/1060
"""

nums = list(map(lambda _: int(input()), range(int(input()))))
for i in sorted(list(set(nums))):
    print(i, nums.count(i))  # 时限问题
