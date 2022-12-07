# 1022.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:05
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1022 校验码生成

url: http://www.hfoj.net/problem/1022
"""

print(list(map(
    lambda n: sum(list(map(
        lambda i, w: i * w,
        n,
        [1, 2, 3] * (len(n) // 3 + 1)))),
    [list(map(int, input()))]))[0] % 55)
