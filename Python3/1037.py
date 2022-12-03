# 1037.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:13
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1037
url: http://www.hfoj.net/problem/1037
"""

print("\n".join(
    list(
        map(lambda nums: [str(len(nums)), " ".join(map(str, nums))],
            [input(), [sorted(list(set(map(int, input().split()))))]][1]))[0]))
