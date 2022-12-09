# 1055.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 18:30
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1055 计数问题

url: http://www.hfoj.net/problem/1055
"""

n, x = list(map(int, input().split()))
x = str(x)
print(sum(list(map(lambda s: str(s).count(x), list(range(1, n + 1))))))
