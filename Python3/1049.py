# 1049.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 17:04
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1049 与7无关的数

url: http://www.hfoj.net/problem/1049
"""

print(len(list(filter(lambda i: i % 7 != 0 and "7" not in str(i), list(range(1, int(input()) + 1))))))
