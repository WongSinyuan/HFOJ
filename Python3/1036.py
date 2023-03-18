# 1036.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-09-17 18:23
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1036 最小字典序

url: http://www.hfoj.net/problem/1036
"""
s = (input())
m = s

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        _s = s[:i] + s[j] + s[i + 1: j] + s[i] + s[j + 1:]
        if _s < m:
            m = _s
print(m)
