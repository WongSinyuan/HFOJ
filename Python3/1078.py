# 1078.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:52
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1078
url: http://www.hfoj.net/problem/1078
"""

s = input().split()

for i in range(len(s)):
    for j in ['er', 'ly', 'ing']:
        if j in s[i][-3:]:
            s[i] = s[i][:-len(j)]
            break

print(" ".join(s))
