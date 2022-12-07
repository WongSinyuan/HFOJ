# 1046.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 17:09
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1046 统计数字

url: http://www.hfoj.net/problem/1046
"""

num = list(map(int, input().split()))[:-1]
print(len(list(filter(lambda x: x > 0, num))))
print(len(list(filter(lambda x: x < 0, num))))
