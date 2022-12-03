# 1044.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:31
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1044
url: http://www.hfoj.net/problem/1044
"""

n = 1
i = 1
c = 0
for _ in range(int(input())):
    c += n
    if n == i:
        n += 1
        i = 1
    else:
        i += 1

print(c)
