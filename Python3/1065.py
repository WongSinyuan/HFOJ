# 1065.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:40
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1065
url: http://www.hfoj.net/problem/1065
"""
n = int(input())

re = []

for i in range(0, n):
    a = []
    if i == 0:
        a = [1]
    elif i == 1:
        a = [1, 1]
    else:
        for j in range(i + 1):
            if j == 0 or j == i:
                a.append(1)
            else:
                a.append(re[i - 1][j - 1] + re[i - 1][j])
    re.append(a)
    print(" ".join(map(str, a)))
